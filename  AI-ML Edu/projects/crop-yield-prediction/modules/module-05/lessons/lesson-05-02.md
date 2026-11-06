# Training, Checkpoints, and Prediction: Inspect the project implementation of training, checkpoints, and prediction

**Lesson ID:** `lesson-05-02`  
**Module:** Training, Checkpoints, and Prediction  
**Source focus:** `run.py` → `_train`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by YieldSight: County-Level Crop Yield Prediction. By the end, you can describe run.py workflow and county-year inference, trace the training, checkpoints, and prediction implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about run.py workflow and county-year inference. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `_train` in `cyp/models/base.py`. Use the excerpt below to trace the actual inputs, transformation, and output for run.py workflow and county-year inference. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The workflow needs Earth Engine exports and large raster data not included in the package. Optional error-map dependencies are missing from the declared environment; results require spatially honest evaluation.

## Step-by-step source investigation

1. Open `cyp/models/base.py` and inspect `_train`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `cyp/models/base.py` (not executed during package generation):

```python
def _train(
        self,
        train_images,
        train_yields,
        train_steps,
        batch_size,
        starter_learning_rate,
        weight_decay,
        l1_weight,
        patience,
    ):
        """Defines the training loop for a model"""

        # split the training dataset into a training and validation set
        total_size = train_images.shape[0]
        # "Learning rates and stopping criteria are tuned on a held-out
        # validation set (10%)."
        val_size = total_size // 10
        train_size = total_size - val_size
        print(
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For training, checkpoints, and prediction, use the repository's own output format and the available test fixture where possible.

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

You can now inspect the project implementation of training, checkpoints, and prediction, identify its source location, and state a limitation. The key project-specific fact is: The source-specific focus for this module is `_train` in `cyp/models/base.py`. Use the excerpt below to trace the actual inputs, transformation, and output for run.py workflow and county-year inference. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
