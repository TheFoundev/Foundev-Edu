# Text Inference Pipeline: Validate outputs and identify limitations for text inference pipeline

**Lesson ID:** `lesson-02-03`  
**Module:** Text Inference Pipeline  
**Source focus:** `backend/app.py` → `predict_text`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by MoodTunes: Emotion Detection and Music Recommendation. By the end, you can describe preprocessing, backend route, and model output, trace the text inference pipeline implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about preprocessing, backend route, and model output. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### The text classifier (DistilBERT)

- **Checkpoint:** `bhadresh-savani/distilbert-base-uncased-emotion`, loaded through
  `transformers.pipeline("text-classification", framework="pt")`.
- **Decision rule:** `results[0]` — the highest-scoring label — is used directly, and its
  score becomes the confidence.
- **Label mapping:** `joy→happy`, `sadness→sad`, `anger→angry`, `fear→fear`,
  `surprise→surprise`, `love→happy`; anything else (notably `neutral` and `disgust`,
  which this checkpoint never emits) falls through to `"neutral"`. This is why the text
  path can never return `disgust`, even though the shared vocabulary contains it.
- **Language caveat:** `distilbert-base-uncased-*` is an English model. The `language`
  field changes only the *music query*, never the text understanding.

Connect this explanation to `backend/app.py` and the source focus `predict_text`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The expected face weights are absent and training provenance is unavailable. Facial/text emotion labels are uncertain and sensitive; no mood inference should be treated as fact.

## Step-by-step source investigation

1. Open `backend/app.py` and inspect `predict_text`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `backend/app.py` (not executed during package generation):

```python
async def predict_text(request: TextRequest):
    """Analyze emotion from text using a Transformer model → YouTube songs."""
    try:
        text = request.text.strip()
        if not text:
            raise HTTPException(status_code=400, detail="Text cannot be empty")

        # Transformer Inference (Lazy Load)
        pipe = get_text_pipeline()
        results = pipe(text)
        # Result example: [{'label': 'joy', 'score': 0.99}]
        raw_label = results[0]["label"]
        confidence = round(float(results[0]["score"]), 4)

        # Map Transformer labels to our system emotions
        label_map = {
            "joy": "happy",
            "sadness": "sad",
            "anger": "angry",
            "fear": "fear",
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For text inference pipeline, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-02-03.md`](../exercises/exercise-02-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for text inference pipeline, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for text inference pipeline. In this repository, the claim must be grounded in the documented behavior and source paths: backend/app.py; backend/model_loader.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
