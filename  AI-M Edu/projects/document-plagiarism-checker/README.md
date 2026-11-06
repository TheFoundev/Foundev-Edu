# Similarity Radar: Document Similarity Checking

## Overview and purpose

Similarity Radar document-plagiarism-checker A student, teacher or writer has no quick way to find out whether a passage or a submitted document already exists on the public web. Turnitin-style tools are paid, closed and unreachable from a classroom laptop. Turn a pasted passage or an uploaded PDF into an evidence list: which exact sentences already appear online, at which URLs, and what share of the document that represents. Students checking an essay before submission; teachers spot-checking a suspicious paragraph; writers verifying that a paragraph of theirs is not already published. A similarity index (matched ÷ total sentences) × 100, the list of matched sentences, and the source URL of

## Real-world context and scope

Plagiarism checks are usually presented as an oracle: paste a document, receive a
percentage, feel informed. In practice that oracle is opaque, often unavailable, and
sometimes paid per submission. A student on a budget, in a country where institutional
licenses are scarce, needs something they can actually run — and something they can
**audit**.

The concrete requirements that follow from that:

1. **Zero-friction input.** The two realistic inputs are a pasted paragraph and a
   submitted PDF. Both must work; nothing else is needed.
2. **No paid service, no API key.** A Google results page is the largest freely searchable
   corpus available to a laptop.
3. **Evidence, not just a number.** A percentage without the matched sentences and their
   sources is not actionable — the reader has to be able to check the claim.
4. **Noise control.** A quoted sentence about, say, a hiring process will match LinkedIn
   and Instagram profiles constantly. Those hits are technically "the same words" but
   useless as evidence of copying, so they must be filtered out.
5. **Honesty.** The tool must state its method and its blind spots (paraphrase, top-10
   window, exact phrase only) instead of implying it can see semantic similarity.

The upstream project satisfies 1–4 in a single 232-line file. The UI layer added later
satisfies 5 — the current `templates/index.html` opens with a "Method, honestly" note and
closes every result with an *explainer* that spells out the four steps and their li

[Excerpt shortened; consult the cited source guide for full detail.]

The material describes the repository as supplied. **Implemented behavior** is summarized from the source overview and entry points; **proposed or missing functionality** is listed separately below. Do not infer production readiness from a polished interface or project title.

### Verified implementation notes

Read PROJECT_OVERVIEW.md in the source repository for the implementation inventory.

### Proposed, absent, or uncertain behavior

- **No local corpus, no TF-IDF, no n-gram fingerprinting** — despite what
  `project-metadata.json` advertises. The only corpus is the live web.
- **No semantic / paraphrase-aware matching** (no embeddings, no sentence-transformers).
- **No JSON API** — HTML only.
- **No accounts, no persistence of results, no report export** (PDF/CSV).
- **No batch upload, no DOCX/PPTX/plain-text upload.**
- **No configurable blocked-domain list, no configurable TLD, no per-query timeout.**
- **No rate-limit handling or back-off** beyond the fixed `pause=2`.

---

## Technology stack

- `beautifulsoup4==4.11.1`
- `click==8.1.3`
- `Flask==2.2.2`
- `googlesearch-python>=1.2.0`
- `ddgs>=9.0.0`
- `importlib-metadata==5.0.0`
- `itsdangerous==2.1.2`
- `Jinja2==3.1.2`
- `MarkupSafe==2.1.1`
- `PyPDF2>=2.11.1`
- `soupsieve==2.3.2.post1`
- `typing-extensions==4.4.0`
- `Werkzeug==2.2.2`
- `zipp==3.10.0`

## System requirements and setup

Use a supported Python environment appropriate to the source dependency pins. Some projects also require data files, trained weights, external APIs, cameras, GPU resources, a database, or an LLM runtime. These are identified in `setup-guide.md`; they are not assumed to be included. Follow the source `WORKFLOW.md` carefully and do not paste real credentials into tracked files.

## Architecture and important components

Four real components, one of which is an external service:

```
┌───────────────────────────────────────────────────────────────────────────┐
│  Browser                                                                  │
│  templates/index.html (Jinja)  +  static/js/app.js  +  static/css/style.css │
│  ├─ input desk: text tab / PDF tab, counters, dropzone                    │
│  ├─ scanning overlay                                                    │
│  └─ results: gauge, stamp, matched sentences, sources, explainer          │
└───────────────▲───────────────────────────────────────┬───────────────────┘
                │ 302 → /plagiarism/<name>#hasil          │ form POST
                │ (multipart/form-data: text, file)      │ GET /  → 200 HTML
┌───────────────┴───────────────────────────────────────▼───────────────────┐
│  Flask app (app.py)  — binds 0.0.0.0:5000, debug off                      │
│  ├─ index()          : POST validation, word.txt / uploads/ persistence   │
│  ├─ plagiarism(name) : PyPDF2 extraction, sentence split, scoring        │
│  ├─ render_template  : one HTML template for desk and results             │
│  └─ flash()          : session cookie messages (SECRET_KEY = 'super …')    │
└───────────────▲───────────────────────────────────────┬───────────────────┘
                │ search(query, tld='co.id', num=10, stop=10, pause=2)      │
                │ (2 calls per sentence, ~4 s each)                           │
┌───────────────┴───────────────────────────────────────▼───────────────────┐
│  Google search results page  ── external service, no API key              │
│  scraped by the `googlesearch` package (google==3.0.0) + BeautifulSoup    │
│  cookie jar: $HOME/.google-cookie → $USERHOME/.google-cookie → ./.google-cookie │
└───────────────────────────────────────────────────────────────────────────┘

Files touched on disk:  word.txt (last pasted text)   uploads/<file>.pdf (last uploads)
```

There is **no database** and **no background worker** — a scan is a blocking HTTP request
whose duration is dominated by the Google round-trips.

```mermaid
flowchart TD
    subgraph Browser["Browser (no framework)"]
        A1[Index page: input desk] --> A2{Tab: text or PDF?}
        A2 -->|text| A3[textarea + live counters]
        A2 -->|PDF| A4[dropzone: extension + 16 MB check]
        A3 --> A5[POST / multipart/form-data]
        A4 --> A5
        A5 --> A6[Scanning overlay shown]
    end

    subgraph Flask["Flask app.py on 0.0.0.0:5000"]
        B1[POST /] --> B2{text filled AND no file?}
        B2 -->|yes| B3[write word.txt]
      

[Excerpt shortened; consult the cited source guide for full detail.]

## Directory structure

Source paths central to the learning material:

- `.github/FUNDING.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/dependency-review.yml`
- `.github/workflows/docker-image.yml`
- `.github/workflows/docker-publish.yml`
- `.github/workflows/main.yml`
- `.github/workflows/python-app.yml`
- `PROJECT_OVERVIEW.md`
- `README.md`
- `WORKFLOW.md`
- `app.py`
- `project-metadata.json`
- `requirements.txt`
- `static/js/app.js`
- `templates/index.html`
- `test_app.py`

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
