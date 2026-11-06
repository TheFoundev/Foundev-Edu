# Architecture — Note Sense: Currency Note Recognition

## Component map

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

    E -. "same files/ folder; no runtime link" .- M
    J -. "same audio/ folder" .- U[detect.py audio/<note>.mp3 (commented out)]
```

---

## Data and control flow

### 9.1 Detection data flow

```mermaid
flowchart TD
    A["files/test_200_1.jpg (hardcoded)"] -->|cv2.imread via read_img| B[test_img BGR]
    B -->|resize_img 0.4| C["display('original') -> OpenCV window, waitKey(0)"]
    B -->|orb.detectAndCompute| D["kp1, des1 (test keypoints + descriptors)"]

    E["training_set (6 reference JPGs)"] -->|cv2.imread| F[train_img]
    F -->|orb.detectAndCompute| G["kp2, des2"]

    D --> H["BFMatcher().knnMatch(des1, des2, k=2)"]
    G --> H
    H --> I{"m.distance < 0.789 * n.distance ?"}
    I -->|yes| J["good.append([m])"]
    I -->|no| K[discard ambiguous match]
    J --> L{"len(good) > max_val ?"}
    L -->|yes| M[max_val = len(good); max_pt = i; max_kp = kp2]
    L -->|no| N[print per-reference count]
    M --> N
    N --> O{"max_val != 8 ?"}
    O -->|no| P["print 'No Matches'"]
    O -->|yes| Q["note = training_set[max_pt][6:-4]"]
    Q --> R["print 'Detected denomination: Rs. <note>'"]
    R --> S["cv2.drawMatchesKnn -> img3"]
    S --> T[plt.imshow(img3); plt.show()]
```

### 9.2 Web-UI data flow

```mermaid
flowchart LR
    subgraph Browser
        U1[User picks JPG/PNG] --> U2[acceptFile: type check]
        U2 --> U3[URL.createObjectURL preview]
        U3 --> U4[Identify note]
        U4 --> U5["Banner: 'Requires backend'"]
        U5 --> U6[speechSynthesis.speak]
        U7[files/*.jpg on disk] --> U8[buildGallery: 44 buttons]
        U8 --> U9[Lightbox: captions + role labels]
        U10[audio/*.mp3 on disk] --> U11[HTMLAudioElement playback]
    end
    U5 -.->|no fetch() call exists| X[(No server / no API)]
```

---

## Algorithm/model details

> This project contains **no trained model**. It uses a classical computer-vision algorithm
> (**ORB feature matching**) with a nearest-neighbour ratio test. There is no training data, no
> loss function and no evaluation in the repository.

### 7.1 ORB — Oriented FAST + Rotated BRIEF

`cv2.ORB_create()` produces a detector + descriptor in one object (the source comment notes it is
“an alternative to SIFT”, which is patent-free and CPU-only):

- **Detector (FAST):** finds *corners* — pixels brighter/darker than a circular ring of 16
  neighbours. FAST is fast because it can early-exit on the first disqualifying pixel.
- **Orientation:** the intensity centroid of the patch around each keypoint gives a dominant
  gradient direction, so the descriptor is rotation-invariant.
- **Descriptor (rBRIEF):** the orientation is used to steer a *rotated* BRIEF sampling pattern, and
  the 256 sampled intensity pairs are compared in a cascaded fashion for speed.

The result is a list of keypoints (`kp`: position, size, angle, response) and a
`des` array of binary descriptors (one 256-bit string per keypoint).

### 7.2 Brute-force matching with `k = 2`

`cv2.BFMatcher()` with ORB descriptors compares **every** test descriptor against **every**
reference descriptor (Hamming distance on the binary strings) and returns the two nearest for each
query. The second-nearest is what makes the ratio test possible.

### 7.3 Lowe's ratio test at 0.789

```python
for (m, n) in all_matches:
    if m.distance < 0.789 * n.distance:
        good.append([m])
```

A match is kept only if the best candidate is **at least ~21 % better** than the runner-up
(`1 − 0.789 ≈ 0.211`). This rejects *ambiguous* points — texture that looks similar to several
places on the reference note — which is exactly the failure mode of texture-matching approaches.
The source itself calls `0.789` “an arbitrary number”, i.e. it is a hand-tuned constant, not a
learned parameter.

### 7.4 Winner-takes-all voting

The number of surviving matches is a vote for that reference. Because the test photo and the
reference are photographs of the *same physical design* (same printing, same guilloche, same
portrait), the keypoints are largely repeatable, so the correct reference accumulates far more
consistent matches than the wrong ones.

The decision rule is `len(good) > max_val` with `max_val` initialised to **8**, so a reference
must produce **more than 8** good matches to be accepted — otherwise the script prints
`No Matches`.

### 7.5 Deriving the label from the filename

```python
note = str(training_set[max_pt])[6:-4]   # 'files/200.jpg' -> '200'
```

The denomination is *not* read from the image; it is sliced out of the winning reference path
(`'files/'` is 6 characters, `'.jpg'` is 4). Elegant, and also the main fragility: a reference file
named anything else yields a wrong label.

### 7.6 Complexity

Let `n` = test keypoints, `m` = reference keypoints:

- Descriptor extraction: `O(n)` and `O(m)`.
- BF matching: `O(n·m)` descriptor comparisons per reference — with a few hundred keypoints per
  photo and six references this is milliseconds to a few hundred milliseconds.
- Memory: `O(n + m)` descriptors of 256 bits each.

No GPU, no network, no model file. That is precisely why this stack suits an offline,
low-resource assistive tool.

### 7.7 What is *not* here

- No CNN/transfer learning (the upstream metadata mentions "CNN" as a stack keyword, but no neural
  network exists in this repository).
- No training, no validation split, no reported accuracy.
- No mouth/face analysis, no OCR, no orientation rectification.

---

## Source inventory

| Path | Role | Key symbols / details |
|---|---|---|
| `index.html` | Note Sense UI markup | 3-step layout, `#drop-zone`, `#note-photo`, `#identify-btn`, `#result-banner` (`data-state`), `#sample-audio`, `#gallery-grid`, `#lightbox`; loads `css/style.css` and `js/app.js`; Google Fonts *Atkinson Hyperlegible* |
| `css/style.css` | UI styling | High-contrast palette, oversized buttons, `prefers-reduced-motion` handling |
| `js/app.js` | UI logic (ES5 IIFE) | `BASE`, `FILES_DIR`, `AUDIO_DIR`, `TRAINING`, `HARDCODED`, `FILES` (44 names), `roleFor()`, `speak()`, `stopSpeaking()`, `acceptFile()`, `resetPhoto()`, `buildGallery()`, `openLightbox()`, `renderLightbox()`, `copyText()`, `BACKEND_BODY` |
| `Currency Detection using OpenCV in ML/detect.py` | **Main detector** | `max_val`/`max_pt`/`max_kp`, `orb = cv2.ORB_create()`, `test_img = read_img('files/test_200_1.jpg')`, `training_set` (6 paths), `bf.knnMatch(des1, des2, k=2)`, ratio test `0.789`, `note = str(...)[6:-4]`, `cv2.drawMatchesKnn` |
| `Currency Detection using OpenCV in ML/utils.py` | Image helpers | `read_img`, `resize_img`, `img_to_gray`, `img_to_gaussian_gray`, `img_to_neg`, `binary_thresh`, `adaptive_thresh`, `sobel_edge`, `sobel_edge2`, `canny_edge`, `laplacian_edge`, `find_contours`, `median_blur`, `dilate_img`, `close`, `harris_edge`, `histogram`, `fourier`, `display` (1440×900 window, `cv2.waitKey(0)`) |
| `Currency Detection using OpenCV in ML/try.py` | Experiment sandbox | Same ORB idea with a **10-image** training set (`20/50/100/500/100/200/2000/10/20_3/10_3`); large blocks of commented-out contour/warp code; TODOs: four-point transform, warping, webcam input |
| `Currency Detection using OpenCV in ML/requirements.txt` | 2020-era pins | `opencv-python==4.4.0.46`, `numpy==1.19.4`, `matplotlib==3.3.2`, `Pillow==8.0.1` + transitive pins |
| `Currency Detection using OpenCV in ML/run.bat` | Windows launcher | `python detect.py runserver` — the extra word is ignored by `detect.py` (no argument parsing) |
| `Currency Detection using OpenCV in ML/README.md` | Upstream note | “To run do `python3 detect.py`” |
| `Currency Detection using OpenCV in ML/files/` | **Reference + test set** | 44 JPGs: `20.jpg`, `50.jpg`, `100.jpg`, `200.jpg`, `500.jpg`, `2000.jpg`, `10.jpg`, plus `*_2/_3` variants and `test_*` photos |
| `Currency Detection using OpenCV in ML/audio/` | Announcements | `20.mp3`, `50.mp3`, `100.mp3` (no 200/500 clip) |
| `Images/currency_images/` | Secondary reference set | `100_rs.jpg`, `200_rs.jpg`, `20_rs.jpg`, `500_rs.jpg`, `50_rs.jpg` (+ `100_rs (2).jpg`) — **not read by the code** |
| `Images/testing_images/` | Extra test photos | 21 images incl. `Euro-500.png`, `test_dollar_1.jpg`, `test_dollar_100.jpg` |
| `project-metadata.json` | Repo metadata | upstream URL, `entry: "Currency Detection using OpenCV in ML/detect.py"`, `license: "Unknown"` |

---

## Implemented versus proposed

Implemented behavior is limited to the source entry points and code paths described above.

- There is no trained CNN or connected web API: the detector uses ORB matching against reference images; the page is static. README claims about server/detector paths conflict with the actual tree. Hard-coded paths and optional speech dependencies require repair/review.
