# Note Sense: Currency Note Recognition

## Overview and purpose

Note Sense currency-note-recognition-for-visually-impaired A visually impaired person cannot reliably identify an Indian banknote by sight, and cannot read the printed value. Cashiers and family members are often unavailable to help. Identify the denomination of a photographed note offline, on a CPU-only machine, with no model download and no network round-trip — and present the result in a voice-first, high-contrast, keyboard-navigable interface. Visually impaired users handling cash; the caregivers and shop assistants who support them; students studying OpenCV feature matching. Detected denomination: Rs. <value> on the console plus a match-visualisation window; in the web UI, a spoken anno

## Real-world context and scope

Banknotes in India carry their value in several places — the numeral on the front, the
numeral on the reverse, and the raised intaglio numerals for the blind — but none of these
are reliably perceivable without sight, and a partially worn note can be ambiguous even for
sighted users. The practical need is:

1. **Decide the denomination of one note quickly** (a shop counter, a till, a wallet).
2. **Do it without a cloud service** — the note is sensitive and connectivity is unreliable.
3. **Do it without a heavy ML stack** — a phone or a low-end laptop should run it.
4. **Hear the answer** — the result must be spoken, not only printed.

An ORB-based matcher satisfies 2–4 naturally: ORB is patent-free, CPU-only, ships inside
`opencv-python`, needs no weights and no GPU, and matching against a handful of reference
photographs is a per-image operation that finishes in seconds.

The web layer then has a second, equally important requirement: **it must not lie**. A page
that showed a random denomination with a confidence bar would be worse than useless for the
target user. So the page states plainly that recognition happens in the local script and
prints nothing it did not actually receive.

---

The material describes the repository as supplied. **Implemented behavior** is summarized from the source overview and entry points; **proposed or missing functionality** is listed separately below. Do not infer production readiness from a polished interface or project title.

### Verified implementation notes

| # | Capability | Implementation |
|---|---|---|
| F1 | ORB keypoint + descriptor extraction | `detect.py:14` `orb = cv2.ORB_create()`, `orb.detectAndCompute(img, None)` |
| F2 | Brute-force 2-nearest-neighbour matching | `detect.py:41-42` `cv2.BFMatcher().knnMatch(des1, des2, k=2)` |
| F3 | Lowe's ratio filter (0.789) | `detect.py:47-49` `if m.distance < 0.789 * n.distance` |
| F4 | Winner selection with a minimum-match floor (8) | `detect.py:10`, `51-54` |
| F5 | Denomination derived from the winning file name | `detect.py:65` `note = str(training_set[max_pt])[6:-4]` |
| F6 | Match visualisation | `detect.py:63` `cv2.drawMatchesKnn(...)` + `plt.imshow(img3), plt.show()` |
| F7 | On-screen preview window before matching | `detect.py:25-26` → `utils.display()` (`cv2.waitKey(0)`) |
| F8 | Broad image-processing toolbox (Canny, Sobel, Laplacian, Harris, FFT, contours, gamma, histogram equalisation) | `utils.py` — `canny_edge`, `sobel_edge`, `sobel_edge2`, `laplacian_edge`, `find_contours`, `harris_edge`, `fourier`, `gamma_correction`… |
| F9 | Voice-first accessible UI with read-aloud | `js/app.js` `speak()` / `stopSpeaking()`, `localStorage` key `notesense:voice` |
| F10 | Honest “Requires backend” result state | `js/app.js` `BACKEND_KICKER`, `BACKEND_TITLE`, `BACKEND_BODY` |
| F11 | Real pre-recorded announcements | `audio/20.mp3`, `50.mp3`, `100.mp3` played through `<audio id="sample-audio">` |
| F12 | Reference gallery with per-image role labels | `js/app.js` `FILES`, `TRAINING`, `HARDCODED`, `roleFor()` |
| F13 | Accessible lightbox (focus trap, `Esc`/arrows) | `js/app.js` `openLightbox`, `closeLightbox`, `renderLightbox`, keydown handler |

### Future / not implemented

- No webcam capture, no video loop, no batch directory processing.
- No OCR of the printed numeral, no perspective rectification of a tilted note.
- No HTTP backend (no `/recognize`-style endpoint exists).
- No per-detection text-to-speech (the `gTTS`/`playsound` calls in `detect.py` are commented out).
- No accuracy benchmark, no unit tests, no CI.

---

### Proposed, absent, or uncertain behavior

- No webcam capture, no video loop, no batch directory processing.
- No OCR of the printed numeral, no perspective rectification of a tilted note.
- No HTTP backend (no `/recognize`-style endpoint exists).
- No per-detection text-to-speech (the `gTTS`/`playsound` calls in `detect.py` are commented out).
- No accuracy benchmark, no unit tests, no CI.

---

## Technology stack

- `See source project dependency manifest and setup guide`

## System requirements and setup

Use a supported Python environment appropriate to the source dependency pins. Some projects also require data files, trained weights, external APIs, cameras, GPU resources, a database, or an LLM runtime. These are identified in `setup-guide.md`; they are not assumed to be included. Follow the source `WORKFLOW.md` carefully and do not paste real credentials into tracked files.

## Architecture and important components

Two **independent** components that share files but not a runtime:

```
┌──────────────────────────────┐        ┌──────────────────────────────────────────────┐
│  Note Sense web UI (static)  │        │  OpenCV detector (desktop script)            │
│  index.html / css / js/app.js│        │  detect.py + utils.py                        │
│  • local file preview        │        │  • reads hardcoded files/test_200_1.jpg      │
│  • Web Speech read-aloud     │        │  • ORB descriptors                           │
│  • gallery + lightbox        │        │  • BFMatcher + Lowe ratio 0.789              │
│  • plays audio/*.mp3         │        │  • prints "Detected denomination: Rs. …"      │
│  • "Requires backend" banner │        │  • opens match map window                    │
└──────────────┬───────────────┘        └───────────────────┬──────────────────────────┘
               │                                            │
               │ reads (static assets)                      │ reads (image files)
               ▼                                            ▼
    Currency Detection using OpenCV in ML/files/*.jpg   files/*.jpg  (44 images)
    Currency Detection using OpenCV in ML/audio/*.mp3   audio/*.mp3  (3 files)
```

- **No HTTP client** exists in `js/app.js` — the page never contacts a server.
- **No server** exists in the repository — `detect.py` is a top-level script.
- The shared dependency is the **file system**: both components read the same `files/` and
  `audio/` directories relative to their own location.

```mermaid
flowchart TD
    subgraph UI["Note Sense web UI (static, no server)"]
        A[Open index.html] --> B[Step 1: choose / drop a photo]
        B --> C[Local preview via URL.createObjectURL]
        C --> D[Step 2: press Identify note]
        D --> E["Result banner: Requires backend (honest state)"]
        E --> F[Read this aloud via Web Speech API]
        G[Gallery: 44 images in files/] --> H[Lightbox with role labels]
        I[Play rupee sample] --> J["audio/20.mp3, 50.mp3, 100.mp3"]
    end

    subgraph DET["detect.py (OpenCV, local)"]
        K[read_img files/test_200_1.jpg] --> L[orb.detectAndCompute -> kp1, des1]
        M[training_set of 6 reference JPGs] --> N[orb.detectAndCompute -> kp2, des2]
        L --> O[BFMatcher.knnMatch k=2]
        N --> O
        O --> P[Lowe ratio test m.distance < 0.789 * n.distance]
        P --> Q["best reference (must exceed 8 good matches)"]
        Q --> R["note = path[6:-4] -> 'Detected denomination: Rs. …'"]
        Q --> S[cv2.drawMatchesKnn + matplotlib window]
    end

    E

[Excerpt shortened; consult the cited source guide for full detail.]

## Directory structure

Source paths central to the learning material:

- `Currency Detection using OpenCV in ML/README.md`
- `Currency Detection using OpenCV in ML/detect.py`
- `Currency Detection using OpenCV in ML/requirements.txt`
- `Currency Detection using OpenCV in ML/try.py`
- `Currency Detection using OpenCV in ML/utils.py`
- `PROJECT_OVERVIEW.md`
- `README.md`
- `WORKFLOW.md`
- `detector.py`
- `index.html`
- `js/app.js`
- `project-metadata.json`
- `server.py`

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
