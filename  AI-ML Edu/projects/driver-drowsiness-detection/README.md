# Cockpit: Driver Drowsiness Detection

## Overview and purpose

Cockpit — Fatigue Monitor (interface) / Driver Drowsiness Detection System (project) driver-drowsiness-detection Drowsy driving is a leading cause of road accidents. A driver who is falling asleep at the wheel cannot be relied on to notice their own deterioration — and a passenger is often asleep too. Measure eye openness continuously from a camera, detect the moment the eyes stay closed long enough to mean "micro-sleep", and sound an alarm that is loud enough to wake the driver. Long-haul drivers; drivers on night shifts; drivers on medication; road-safety researchers; students studying EAR-based fatigue detection. A live video window with eye landmarks and a blink counter, a ! ! ! DROWSINE

## Real-world context and scope

Blink rate and eye-closure duration are the cheapest physiological proxies for mental
fatigue that a camera can read. A driver's eyes are open almost all the time while
awake; as fatigue sets in, blinks get longer and more frequent, and eventually the eyes
stay closed for a fraction of a second — a *micro-sleep*. The critical quantity is
therefore not "is the eye closed" but "how long has the eye been closed", because a
100 ms blink is normal and a 1.5 s closure is a hazard.

The engineering requirements that follow:

1. **Measure eye openness robustly on cheap hardware.** No GPU, no model download, no
   cloud — a laptop webcam must be enough.
2. **Distinguish a blink from a doze.** A fixed threshold on the frame count cannot do
   this, because the time one frame represents depends on the machine's speed. The
   detector must first *measure its own frame rate* and convert durations into frame
   counts.
3. **Alert loudly enough to be useful.** A visual overlay alone is useless if the driver
   is asleep; an audio alarm is mandatory.
4. **Never cry wolf.** A detector that alarms on every blink is switched off within a
   day, so short closures must be classified as false blinks.
5. **Keep the video local.** Face images of drivers are sensitive; processing must happen
   on the device.

The upstream code satisfies all five; the Cockpit page exists to make the *thresholds and
the mathematics* legible to someone who wants to understand or re-tune the system.

---

The material describes the repository as supplied. **Implemented behavior** is summarized from the source overview and entry points; **proposed or missing functionality** is listed separately below. Do not infer production readiness from a polished interface or project title.

### Verified implementation notes

Read PROJECT_OVERVIEW.md in the source repository for the implementation inventory.

### Proposed, absent, or uncertain behavior

- **No MAR (mouth aspect ratio)** — despite `project-metadata.json` advertising
  "EAR/MAR eye-mouth ratio". Only EAR exists in the code.
- **No trip report** — the metadata mentions one; the only report is the console summary.
- **No session history persistence** — `Sesssion_analysis.py` is a 17-line Tkinter stub
  with two empty `ttk.Frame`s.
- **No trained model** — `models/ML_Models/` contains two empty folders
  (`ResNET+CNN (Tranfer Learning)`, `Using Transformers`) and no weights.
- **No HTTP API** — nothing to call from a browser or a mobile app.
- **No multi-face handling** — only `rects[0]` is tracked.
- **No glasses/sunglasses handling, no head pose, no gaze tracking, no PERCLOS**.
- **No calibration per driver** — one global threshold.
- **No adaptive thresholding** — the value is a hand-tuned constant.
- **`models/ML_Models/` is not loaded by any script** in the repository.

---

## Technology stack

- `opencv-python>=4.5.0,<5.0.0`
- `dlib>=19.22.0,<20.0.0`
- `numpy>=1.19.0,<2.0.0`
- `scipy>=1.7.0,<2.0.0`
- `playsound>=1.2.2,<2.0.0`
- `playsound; platform_system == "Windows"  # For compatibility on Windows`
- `matplotlib>=3.3.0,<4.0.0`
- `streamlit>=1.25.0,<2.0.0`
- `streamlit-webrtc>=0.45.0,<1.0.0`
- `mediapipe>=0.10.0,<1.0.0`
- `Pillow>=8.0.0,<11.0.0`
- `aiofiles>=0.7.0,<1.0.0  # For async file serving`

## System requirements and setup

Use a supported Python environment appropriate to the source dependency pins. Some projects also require data files, trained weights, external APIs, cameras, GPU resources, a database, or an LLM runtime. These are identified in `setup-guide.md`; they are not assumed to be included. Follow the source `WORKFLOW.md` carefully and do not paste real credentials into tracked files.

## Architecture and important components

Three independent programs plus one static page. They share the *idea*, not a runtime:

```
┌────────────────────────┐   ┌─────────────────────────┐   ┌────────────────────────┐
│  blinkDetect.py        │   │  streamlit_app/         │   │  index.html + js/app.js│
│  dlib 68 landmarks     │   │  streamlit_app.py       │   │  Cockpit HUD           │
│  cv2.VideoCapture(0)   │   │  MediaPipe FaceMesh     │   │  simulated EAR signal  │
│  → OpenCV window       │   │  streamlit-webrtc       │   │  gauge + strip chart   │
│  → alarm.wav           │   │  → port 8501            │   │  → static file server  │
│  needs models/…68…dat │   │  → alarm.mp3            │   │    (no camera access)  │
└───────────┬────────────┘   └────────────┬────────────┘   └────────────┬───────────┘
            │                             │                             │
            │  cv2 + dlib                 │  mediapipe + av            │  browser JS only
            ▼                             ▼                             ▼
      ┌───────────┐                ┌───────────┐                 (no network I/O)
      │  Webcam 0 │                │  Browser  │
      └───────────┘                │  WebRTC   │
                                   └───────────┘

Shared assets:  models/haarcascade_frontalface_default.xml (present)
                models/shape_predictor_68_face_landmarks.dat (MISSING — download required)
                alarm.wav (root)  ·  streamlit_app/alarm.mp3
```

```mermaid
flowchart TD
    subgraph Desktop["Desktop path (dlib)"]
        A1["cv2.VideoCapture(0)"] --> A2["read frame"]
        A2 --> A3["resize to height 460"]
        A3 --> A4["histogram_equalization"]
        A4 --> A5["getLandmarks(): downscale 1/1.5 -> dlib frontal_face_detector -> shape_predictor 68 pts"]
        A5 --> A6{face found?}
        A6 -->|no| A7["overlay 'Unable to detect face' + continue"]
        A6 -->|yes| A8["checkEyeStatus(): hull of eye points -> EAR per eye -> mean"]
        A8 --> A9["eyeStatus = 1 if EAR >= 0.27 else 0"]
        A9 --> A10["checkBlinkStatus(): state counter -> blink / drowsy / alert"]
        A10 --> A11["draw landmark dots + overlay"]
        A11 --> A12{drowsy?}
        A12 -->|yes| A13["alarm thread: playsound('alarm.wav') + DROWSINESS ALERT"]
        A12 -->|no| A14["overlay 'Blinks : N'"]
        A13 --> A15["vid_writer.write(frame) -> output-low-light-2.avi"]
        A14 --> A15
        A7 --> A2
    end

    subgraph Web["Web path (MediaPipe)"]
        B1["streamlit-webrtc: browser camera frames"] --> B2["DrowsinessDetector.transform()"]
        B2 --> B

[Excerpt shortened; consult the cited source guide for full detail.]

## Directory structure

Source paths central to the learning material:

- `.github/workflows/issue-create-automate-message.yml`
- `.github/workflows/pr-create-automate-message.yml`
- `PROJECT_OVERVIEW.md`
- `README.md`
- `Sesssion_analysis.py`
- `WORKFLOW.md`
- `blinkDetect.py`
- `face-try.py`
- `index.html`
- `js/app.js`
- `lanedetection.py`
- `main.py`
- `project-metadata.json`
- `requirements.txt`
- `streamlit_app/.streamlit/config.toml`
- `streamlit_app/generate_icons.py`
- `streamlit_app/manifest.json`
- `streamlit_app/offline.html`
- `streamlit_app/streamlit_app.py`
- `streamlit_app/streamlit_app_pwa.py`
- `streamlit_app/sw.js`
- `streamlit_app/test_pwa_setup.py`
- `ui.py`

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
