# Legacy Training Versus Browser Heuristic: Inspect the project implementation of legacy training versus browser heuristic

**Lesson ID:** `lesson-05-02`  
**Module:** Legacy Training Versus Browser Heuristic  
**Source focus:** `index.html` → `demoSeverity`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Underwriting Desk: Loan Default Risk Modeling. By the end, you can describe train_predict.py/models.py and disconnected demo UI, trace the legacy training versus browser heuristic implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about train_predict.py/models.py and disconnected demo UI. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 6. The browser heuristic (and why it is not the model)

`js/app.js` scores a case as `sigmoid(DEMO_INTERCEPT + Σ wᵢ·xᵢ)` with `DEMO_INTERCEPT = -1.6` and 15 `DEMO_FACTORS` covering DTI, delinquency counts, derogatory reports, credit lines, APR, term, amount, age, income, missingness, and the three `comb` projections (compressed by `tanh(x/40)` and scaled by the blend sliders). The weights are hand-authored for illustration; they were not fitted to any data. The severity formula mirrors `PartialRegressor`'s `exp` + clip, and the `0.6` gate mirrors `train_predict.py` — but the probability is a different function entirely.

Connect this explanation to `js/app.js` and the source focus `demoSeverity`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The web UI is a heuristic demo, not the trained pipeline. The legacy training path requires missing CSV inputs and porting; no model artifact is supplied. Credit decisions need rigorous fairness, calibration, and legal review.

## Step-by-step source investigation

1. Open `js/app.js` and inspect `demoSeverity`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `js/app.js` (not executed during package generation):

```javascript
function demoSeverity(res, v) {
    var logSev = 0.85 + 1.9 * res.p + 0.4 * (v.dti / 50) + 0.35 * v.late90 + 0.25 * v.derog;
    return clamp(Math.exp(logSev), 1, 100);
  }

  /* Verdict bands. Decline cut informed by train_predict.py's 0.60 cut. */
  function verdictOf(p) {
    if (p > LOSS_CUT) return 'decline';
    if (p >= 0.45) return 'review';
    return 'approve';
  }
  function bandOf(p) {
    if (p > LOSS_CUT) return 'D';
    if (p >= 0.45) return 'C';
    if (p >= 0.3) return 'B';
    return 'A';
  }
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For legacy training versus browser heuristic, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-05-02.md`](../exercises/exercise-05-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of legacy training versus browser heuristic, identify its source location, and state a limitation. The key project-specific fact is: ### 6. The browser heuristic (and why it is not the model)

`js/app.js` scores a case as `sigmoid(DEMO_INTERCEPT + Σ wᵢ·xᵢ)` with `DEMO_INTERCEPT = -1.6` and 15 `DEMO_FACTORS` covering DTI, delinquency counts, derogatory reports, credit lines, APR, term, amount, age, income, missingness, and the three `comb` projections (compressed by `tanh(x/40)` and scaled by the blend sliders). The weights are hand-authored for illustration; they were not fitted to any data. The severity formula mirrors `PartialRegressor`'s `exp` + clip, and the `0.6` gate mirrors `train_predict.py` — but the probability is a different function entirely.

Connect this explanation to `js/app.js` and the source focus `demoSeverity`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
