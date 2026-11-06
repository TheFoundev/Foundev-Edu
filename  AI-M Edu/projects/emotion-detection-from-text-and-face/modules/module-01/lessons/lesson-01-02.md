# Emotion Labels and Modalities: Inspect the project implementation of emotion labels and modalities

**Lesson ID:** `lesson-01-02`  
**Module:** Emotion Labels and Modalities  
**Source focus:** `backend/app.py` → `predict`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by MoodTunes: Emotion Detection and Music Recommendation. By the end, you can describe text versus face input and label interpretation, trace the emotion labels and modalities implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about text versus face input and label interpretation. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### The face classifier (custom CNN)

- **Architecture:** the repository does not contain the training code for the shipped
  weights, and `models/emotion_model.h5` is not in the repository. What the code *does*
  tell us is precise: the input is a single RGB tensor of shape `(1, 224, 224, 3)`
  (`preprocess_face()`), the output is a 7-element vector (`backend/app.py:129` iterates
  over 7 classes and `emotion_labels.json` contains exactly 7 entries), and the class
  order is fixed by `emotion_labels.json`:
  `angry=0, disgust=1, fear=2, happy=3, neutral=4, sad=5, surprise=6`.
- **Preprocessing contract:** BGR→RGB (`cv2.COLOR_BGR2RGB`) → `cv2.resize(rgb, (224,224))`
  → `astype("float32") / 255.0` → `reshape(1, 224, 224, 3)`. No mean/std normalisation is
  applied, so the model expects plain `[0,1]` scaling.
- **Decision rule:** a plain arg-max over the softmax output. `predicted_idx = int(
  np.argmax(predictions))`; the label comes from `idx_to_label` (falling back to
  `"neutral"` for an out-of-range index) and the confidence is that entry rounded to 4
  decimals. There is no thre

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `backend/app.py` and the source focus `predict`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The expected face weights are absent and training provenance is unavailable. Facial/text emotion labels are uncertain and sensitive; no mood inference should be treated as fact.

## Step-by-step source investigation

1. Open `backend/app.py` and inspect `predict`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `backend/app.py` (not executed during package generation):

```python
async def predict(file: UploadFile = File(...), language: str = Form("Any")):
    """Upload a face image → DeepFace fallback → custom CNN emotion → YouTube songs."""

    tmp_path = None
    try:
        contents = await file.read()

        # Decode image bytes
        npimg = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        if img is None:
            raise HTTPException(status_code=400, detail="Invalid image file")

        # Save to temp file for DeepFace
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
            tmp_path = tmp.name
            cv2.imwrite(tmp_path, img)

        # ── Step 1: Use DeepFace (Lazy Import) ──────
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For emotion labels and modalities, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-01-02.md`](../exercises/exercise-01-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of emotion labels and modalities, identify its source location, and state a limitation. The key project-specific fact is: ### The face classifier (custom CNN)

- **Architecture:** the repository does not contain the training code for the shipped
  weights, and `models/emotion_model.h5` is not in the repository. What the code *does*
  tell us is precise: the input is a single RGB tensor of shape `(1, 224, 224, 3)`
  (`preprocess_face()`), the output is a 7-element vector (`backend/app.py:129` iterates
  over 7 classes and `emotion_labels.json` contains exactly 7 entries), and the class
  order is fixed by `emotion_labels.json`:
  `angry=0, disgust=1, fear=2, happy=3, neutral=4, sad=5, surprise=6`.
- **Preprocessing contract:** BGR→RGB (`cv2.COLOR_BGR2RGB`) → `cv2.resize(rgb, (224,224))`
  → `astype("float32") / 255.0` → `reshape(1, 224, 224, 3)`. No mean/std normalisation is
  applied, so the model expects plain `[0,1]` scaling.
- **Decision rule:** a plain arg-max over the softmax output. `predicted_idx = int(
  np.argmax(predictions))`; the label comes from `idx_to_label` (falling back to
  `"neutral"` for an out-of-range index) and the confidence is that entry rounded to 4
  decimals. There is no thre

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `backend/app.py` and the source focus `predict`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
