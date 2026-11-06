# Metrics and Population Analysis: Validate outputs and identify limitations for metrics and population analysis

**Lesson ID:** `lesson-04-03`  
**Module:** Metrics and Population Analysis  
**Source focus:** `pipeline/__6_Evaluate.py` → `plot_precision_recall_n`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by DEWS: Student Dropout Risk Prediction. By the end, you can describe precision/recall, subgroup plots, and evaluation limits, trace the metrics and population analysis implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about precision/recall, subgroup plots, and evaluation limits. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `plot_precision_recall_n` in `pipeline/precision_recall_population graph.py`. Use the excerpt below to trace the actual inputs, transformation, and output for precision/recall, subgroup plots, and evaluation limits. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The UI is a demo; the historical pipeline scripts are documented as mostly broken/legacy. Labels are an administrative rule. Risk scores must support voluntary services, not punitive decisions.

## Step-by-step source investigation

1. Open `pipeline/precision_recall_population graph.py` and inspect `plot_precision_recall_n`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `pipeline/precision_recall_population graph.py` (not executed during package generation):

```python
def plot_precision_recall_n(y_true, y_prob, model_name):
	# Weird because precision & recall curves have n_thresholds + 1 values. Their last values are fixed so throw away last value.
	y_score = y_prob
	from sklearn.metrics import precision_recall_curve
	precision_curve, recall_curve, pr_thresholds = precision_recall_curve(y_true, y_score)
	precision_curve = precision_curve[:-1]
	recall_curve = recall_curve[:-1]

	pct_above_per_thresh = []
	number_scored = len(y_score)
	for value in pr_thresholds:
		num_above_thresh = len(y_score[y_score>=value])
		pct_above_thresh = num_above_thresh / float(number_scored)
		pct_above_per_thresh.append(pct_above_thresh)
	pct_above_per_thresh = np.array(pct_above_per_thresh)
	plt.clf()
	fig, ax1 = plt.subplots()
	ax1.plot(pct_above_per_thresh, precision_curve, 'b')
	ax1.set_xlabel('percent of population')
	ax1.set_ylabel('precision', color='b')
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For metrics and population analysis, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-04-03.md`](../exercises/exercise-04-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for metrics and population analysis, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for metrics and population analysis. In this repository, the claim must be grounded in the documented behavior and source paths: pipeline/__6_Evaluate.py; pipeline/precision_recall_population graph.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
