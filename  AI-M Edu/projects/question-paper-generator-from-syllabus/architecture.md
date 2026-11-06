# Architecture — ExamForge: Syllabus-Based Question Generation

## Component map

```
                    ┌──────────────────────────────────────────────┐
   Teacher's        │            Flask process (app.py)            │
   browser  ◄─────►│  routes → prompts → model calls → renderers │
                    └───┬──────────────┬──────────────┬───────────┘
                        │              │              │
            ┌───────────▼───┐   ┌──────▼──────┐  ┌────▼─────────────┐
            │ Pragament API │   │  Ollama     │  │  Filesystem      │
            │ allbooks.json │   │  (llama2)   │  │  structured_data │
            │ page_attr.json│   │  CLI + SDK  │  │  textbook_content│
            └───────────────┘   └─────────────┘  │  static/svgs     │
                                                 │  paper.json      │
        ┌────────────────────────────────────────┴─────────────────┐
        │  renderers: fpdf (paper, study material)                 │
        │            reportlab (prereq tree, FIB)                  │
        │            Pillow (corner markers)                       │
        └──────────────────────────────────────────────────────────┘
```

**Layers**

| Layer | Modules | Responsibility |
|---|---|---|
| Presentation | `templates/*.html`, `static/css/qp-style.css`, `static/js/qp-style.js` | ExamForge UI, mode cards, selection form, chapter tree, review screen, results |
| Routing / orchestration | `app.py` (2790 lines) | 28 routes, prompt construction, model invocation, PDF assembly, session state |
| Configuration | `config.py` | Paths and the API base URL, each overridable by an environment variable |
| Content generation | `content_generate.py` | 12 study-material content types, one JSON object per chapter |
| Reusable generators | `generator.py`, `utils.py`, `omr_pdf.py`, `OMR_Template.py`, `svg.py` | FIB content + worksheet builder, PDF/DOCX writers, prerequisite tree, OMR sheet, SVG pipeline |
| External services | Pragament API, GitHub `json_data`, Wikimedia Commons, Ollama | Catalogue, topic lists, diagrams, LLM |
| Companion apps | `fib_app.py`, `omr_generator_app.py` | Standalone FIB and OMR Flask apps on the same port |
| History / packaging | `app_last.py`, `app_test.py`, `app-test.py`, `app_fib.py`, `flask_app_installer/` | Earlier snapshots and the Windows installer build |

---

## Data and control flow

```
Pragament allbooks.json ──▶ load_cached_textbooks() ──▶ structured_data/textbook_cache.json
                                                        └──▶ index.html (board/class/subject)

board + class + subject
        │
        ▼  /select
page_attributes/<book_id>.json ──▶ split by type ──▶ sort by order
        │                            └──▶ prefix-link topics/subtopics
        ▼
structured_data/list_of_all_chapters_for_selected_class.json
        │
        ├──▶ templates/select.html  (subject_chapter_map)
        │
        ├──▶ /generate_questions_no_prereq ──▶ prompts ──▶ ollama run llama2
        │                                               │  (JSON + sanitiser)
        │                                               ▼
        │                       paper.json + Question.pdf ◀── review_questions.html
        │                                               │      (selected_indexes)
        ├──▶ /recursive_prereq/1..3 ──▶ prerequisite tree ──▶ Prerequisite_Tree.pdf
        ├──▶ /generate_study_material ──▶ content_<ts>/*.json ──▶ study material PDF
        ├──▶ /run_fib_generation ──▶ paragraph + word bank ──▶ student PDF + answer key PDF
        └──▶ /run_svg_generation ──▶ Wikimedia ──▶ static/svgs/*.svg + *_explanation.md
```

**State on disk (all global, single-user):** `structured_data/textbook_cache.json`,
`structured_data/list_of_all_chapters_for_selected_class.json`,
`structured_data/prepared_selected_data.json`, `structured_data/prepared_selected_data_direct.json`,
`paper.json`, `Question.pdf`, `textbook_content/`, `static/svgs/`, and the Flask session for
`processed_svgs`.

**Notable data-flow detail.** `app.py` imports `TEXTBOOKS_API` from `config.py` and then
overwrites it on line 54 with the same hard-coded URL, so that constant ignores the environment
variable; the other five `config.py` constants are honoured because they are read at import time.

---

## Algorithm/model details

ExamForge contains **no trained model and no classical ML algorithm**. The "intelligence" is a
general-purpose LLM used in a constrained, verifiable way.

**Prompting contract.** Each generation route builds a `system_prompt` that pins the output shape:

- *MCQ*: one object per topic with `question`, `options` (exactly four), `correct_option`,
  `class`, `subject`, `chapter`, `topic`, `subtopic`.
- *Study material*: a single JSON object keyed by content type — `chaptersummaries1`,
  `definitionbank1`, `formulasheet1`, `importantpoints1`, `solvedexamples2`, plus quiz, FIB,
  true/false, HOTS and real-life-application sections.
- *FIB*: `paragraph`, `concepts` (8, ≤9 letters), `word_bank`, `questions` (8, each containing
  `______`), `answers` (8).

**Output sanitising.** `sanitize_ollama_json()` strips Markdown fences, removes trailing commas and
repairs a malformed `"answers"` block before `json.loads()`. If the result still fails to parse, the
UI shows "The AI model returned a malformed JSON object that could not be repaired."

**Answer verification by agreement.** `verify_answer_with_models()` re-queries the model with a
reduced prompt asking only for the option number, collects the answers, and marks the question
`verified: True` only when at least two of them agree. This is a self-consistency / majority-vote
check rather than a ground-truth check.

**Prerequisite inference by prompt.** For each selected chapter the model is asked to name chapters
of the previous class that the current one depends on, returning `prerequisite_chapters`, a
`reason` for each and a `for` target. The output is advisory — the teacher confirms every entry
before it enters the paper.

**Diagram selection.** For the SVG pipeline the pipeline uses Wikimedia Commons' search API
(`action=query&list=search&srsearch=…`) to find candidate diagrams for a topic, downloads the
original file, and applies a structural validation (`<svg` prefix) before enhancing and explaining
it. That is retrieval, not generation.

**Textbook parsing (deterministic).** Chapter structuring is pure parsing: records are grouped by
their `type` field, sorted by `order`, and linked by dotted-numeric prefixes (`1.2` belongs to `1`).
The deterministic layer is what makes the syllabus output trustworthy.

---

## Source inventory

| File | Role | Key elements |
|---|---|---|
| `app.py` | Main Flask app — routes, prompts, model calls, PDF writers | 28 routes; `generate_questions()`, `verify_answer_with_models()`, `generate_pdf()`, `build_prerequisite_tree()`, `generate_prerequisite_pdf()`, `generate_fib_content()`, `generate_fib_pdf_v2()`, `enhance_svg()`, `load_cached_textbooks()`, `normalize_subject()`, `normalize_class()`; `app.run(debug=True)` |
| `config.py` | Paths and API base URL | `TEXTBOOKS_API`, `DATA_DIR`, `TEXTBOOK_PAGES_DIR`, `FONTS_DIR`, `CONTENT_DIR`, `TEXT_LIMIT` — all env-overridable |
| `content_generate.py` | Study-material engine | `generate_educational_content()`, `prepare_chapter_for_generation()`, 12 content-type prompts, `ollama.list()` availability probe |
| `generator.py` | FIB helpers | `generate_fib_content()`, `generate_fib_pdf()`, `draw_markers()` |
| `utils.py` | Shared helpers | Chapter structuring, PDF/DOCX writers, prerequisite-tree rendering |
| `svg.py` | Standalone SVG pipeline | `fetch_topics()`, `process_topic()`, `enhance_svg()` — search → download → validate → enhance → explain |
| `omr_pdf.py` | OMR sheet writer | `class OMRGenerator(FPDF)` — bubble grid, option layout, marker placement |
| `OMR_Template.py` | OMR scoring template builder | PDF → image → `template.json` pipeline |
| `fib_app.py` | Standalone FIB Flask app | Minimal `/` GET + POST; needs `fib_index.html` / `ifib_index.html` (**absent**) |
| `omr_generator_app.py` | Standalone OMR Flask app | Inline `FORM_HTML`, subject count inputs, returns the PDF |
| `app_fib.py` | Earlier standalone FIB app | Historical snapshot |
| `app_last.py`, `app_test.py`, `app-test.py` | Earlier snapshots of the main app | 2079 / 2370 / 301 lines — historical, not the live entry point |
| `requirements.txt` | Declared dependencies | `flask`, `fpdf`, `requests`, `python-dotenv`, `Pillow`, `reportlab` — **omits `ollama` and `tenacity`** |
| `templates/` | Jinja templates | `index.html` (ExamForge home), `select.html` (chapter tree), `review_questions.html`, `result.html`, `recursive_prereq.html`, `select_fib_topics.html`, `fib_results.html`, `study_material.html`, `svg_generator.html`, `svg_results.html`, `view_svg.html`, plus `*.html.bak` backups of the originals |
| `static/css/qp-style.css`, `static/js/qp-style.js` | ExamForge styling and behaviour | Shared stylesheet/script for the redesign |
| `static/img1.jpg` | FIB corner marker | Stamped on the student worksheet |
| `static/svgs/` | Generated diagrams | SVG + `_placeholder.svg` + `_explanation.md` |
| `fonts/DejaVuSans.ttf` | PDF font | **Required** by `generate_pdf()`; Bold/Oblique variants **absent** |
| `structured_data/` | Runtime state | `textbook_cache.json`, `list_of_all_chapters_for_selected_class.json`, `prepared_selected_data*.json` |
| `textbook_content/` | Generated outputs | Study-material PDFs, `content_<timestamp>/*.json`, FIB PDFs |
| `Sample/` | OMR samples | `omr_sheet.pdf`, `template.json`, `converted_omr.png`, `marker.png` |
| `flask_app_installer/` | Windows installer build | `build_exe.py`, `installer_script.nsi`, `setup/` |
| `project-metadata.json` | Upstream catalogue entry | Points at `app_fib.py` as the entry, upstream repo URL |
| `LICENSE` | AGPL-3.0 | Upstream terms |

---

## Implemented versus proposed

Implemented behavior is limited to the source entry points and code paths described above.

- The app depends on remote curriculum catalogue and a local Ollama llama2 service; question correctness is not guaranteed. Requirements omit dependencies noted in workflow; teacher review is mandatory.
