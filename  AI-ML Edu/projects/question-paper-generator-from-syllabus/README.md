# ExamForge: Syllabus-Based Question Generation

## Overview and purpose

ExamForge is a Flask web application that turns a school syllabus into ready-to-print teaching material. A teacher picks board, class and subject; the app fetches the real textbook catalogue from a public API, resolves the chapter / topic / subtopic tree, and then uses a local Ollama llama2 model to identify prerequisite chapters, draft one multiple-choice question per topic, verify the answers, and export the result as a PDF question paper, a CSV sheet, a prerequisite-tree PDF, a study-material PDF, a fill-in-the-blanks worksheet (student sheet + answer key) or an SVG diagram set with AI explanations. A separate OMR sheet generator and a set of SVG/OMR helper scripts round out the toolset.

## Real-world context and scope

A teacher preparing a chapter test faces three recurring problems:

1. **Syllabus alignment.** The chapter/topic structure must match the specific board, class and
   subject book — generic AI output usually drifts away from the prescribed syllabus.
2. **Prerequisite depth.** Students often lack the concepts from earlier chapters that the current
   topic depends on, and identifying that chain by hand is slow.
3. **Assembly overhead.** Turning AI output into a printable paper, a student worksheet, an answer
   key, an OMR sheet and a diagram set means reformatting the same content five different ways.

ExamForge targets all three: the structure comes from the real textbook catalogue rather than from
the model, prerequisites are surfaced explicitly and can be confirmed by the teacher, and one
generation pass is rendered into every output format the class actually needs.

---

The material describes the repository as supplied. **Implemented behavior** is summarized from the source overview and entry points; **proposed or missing functionality** is listed separately below. Do not infer production readiness from a polished interface or project title.

### Verified implementation notes

Read PROJECT_OVERVIEW.md in the source repository for the implementation inventory.

### Proposed, absent, or uncertain behavior

- The app depends on remote curriculum catalogue and a local Ollama llama2 service; question correctness is not guaranteed. Requirements omit dependencies noted in workflow; teacher review is mandatory.

## Technology stack

- `flask`
- `fpdf`
- `requests`
- `python-dotenv`
- `Pillow`
- `reportlab`

## System requirements and setup

Use a supported Python environment appropriate to the source dependency pins. Some projects also require data files, trained weights, external APIs, cameras, GPU resources, a database, or an LLM runtime. These are identified in `setup-guide.md`; they are not assumed to be included. Follow the source `WORKFLOW.md` carefully and do not paste real credentials into tracked files.

## Architecture and important components

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

## Directory structure

Source paths central to the learning material:

- `OMR_Template.py`
- `PROJECT_OVERVIEW.md`
- `README.md`
- `Sample/template.json`
- `WORKFLOW.md`
- `app-test.py`
- `app.py`
- `app_fib.py`
- `app_last.py`
- `app_test.py`
- `config.py`
- `content_generate.py`
- `fib_app.py`
- `flask_app_installer/README.md`
- `flask_app_installer/flask_app/app.py`
- `flask_app_installer/flask_app/config.py`
- `flask_app_installer/flask_app/static/js/script.js`
- `flask_app_installer/flask_app/templates/index.html`
- `flask_app_installer/scripts/build_exe.py`
- `generator.py`
- `omr_generator_app.py`
- `omr_pdf.py`
- `project-metadata.json`
- `requirements.txt`
- `static/js/qp-style.js`
- `svg.py`
- `templates/fib_results.html`
- `templates/index.html`
- `templates/next_step.html`
- `templates/recursive_prereq.html`
- `templates/result.html`
- `templates/review_questions.html`
- `templates/select.html`
- `templates/select_fib_topics.html`
- `templates/select_prereq.html`
- `templates/show_selected_chapters.html`
- `templates/study_material.html`
- `templates/svg_generator.html`
- `templates/svg_results.html`
- `templates/tree_checkbox.html`
- `templates/view_svg.html`
- `textbook_content/content_20250917_103031/chaptersummaries1.json`
- `textbook_content/content_20250917_103031/definitionbank1.json`
- `textbook_content/content_20250917_103031/formulasheet1.json`
- `textbook_content/content_20250917_103031/importantpoints1.json`
- `textbook_content/content_20250917_103718/chaptersummaries2.json`
- `textbook_content/content_20250917_103718/definitionbank2.json`
- `textbook_content/content_20250917_103718/formulasheet2.json`
- `textbook_content/content_20250917_103718/importantpoints2.json`
- `textbook_content/content_20250917_103718/solvedexamples2.json`
- `utils.py`

## Installation, environment, and database

See [`setup-guide.md`](setup-guide.md) for repository-specific commands, environment variables, optional services, and data/model requirements. Database setup is only applicable when the source workflow documents a database.

## Testing

Use only tests and checks present in the source repository. This learning package has not run the source application or trained a model. Expected test behavior and missing coverage are described in the source workflow and lessons.

## Security, privacy, and responsible use

Treat credentials, uploaded data, biometric data, student/financial records, and generated outputs as sensitive where relevant. Apply data minimization, consent and access controls, retention limits, secure secret handling, documented error handling, and human review. For consequential decisions, model outputs are educational signals only. Project-specific hazards appear in the final project guide and source review report.

## Troubleshooting

Start with missing assets and dependency versions, then validate input shape/schema, check configured API/database/model services, inspect logs, and compare observed behavior with the exact source path described in `architecture.md`. Many repositories contain a static UI or stub that is not wired to the model.

## Expected outcome

Complete the final project to explain and reproduce the repository's actual data-to-output path, demonstrate a tested source-aligned extension, and document its limitations.

## Further learning

See `references.json` for official framework references and the source repository's `PROJECT_OVERVIEW.md`, `WORKFLOW.md`, and README for implementation details.
