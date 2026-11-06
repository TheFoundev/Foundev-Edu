# Classification Pipeline: Understand legacy pipeline scripts and intended classifier stages

**Lesson ID:** `lesson-03-01`  
**Module:** Classification Pipeline  
**Source focus:** `pipeline/__4_Generate_Features.py` → `Classifier`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by DEWS: Student Dropout Risk Prediction. By the end, you can describe legacy pipeline scripts and intended classifier stages, trace the classification pipeline implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about legacy pipeline scripts and intended classifier stages. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `Classifier` in `pipeline/__5_Classifier.py`. Use the excerpt below to trace the actual inputs, transformation, and output for legacy pipeline scripts and intended classifier stages. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The UI is a demo; the historical pipeline scripts are documented as mostly broken/legacy. Labels are an administrative rule. Risk scores must support voluntary services, not punitive decisions.

## Step-by-step source investigation

1. Open `pipeline/__5_Classifier.py` and inspect `Classifier`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `pipeline/__5_Classifier.py` (not executed during package generation):

```python
from sklearn.neighbors import KNeighborsClassifier


#Boosting and Bagging
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier

#Time
import time
from threading import Timer
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For classification pipeline, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-03-01.md`](../exercises/exercise-03-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand legacy pipeline scripts and intended classifier stages, identify its source location, and state a limitation. The key project-specific fact is: Understand legacy pipeline scripts and intended classifier stages. In this repository, the claim must be grounded in the documented behavior and source paths: pipeline/__4_Generate_Features.py; pipeline/__5_Classifier.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
