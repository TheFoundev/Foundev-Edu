# Notebook Models and Visualization: Inspect the project implementation of notebook models and visualization

**Lesson ID:** `lesson-04-02`  
**Module:** Notebook Models and Visualization  
**Source focus:** `notebooks/02-cpj-research-model.ipynb` → `sns.lineplot`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by TrendCast: Stock Price Trend Research. By the end, you can describe research notebooks and exploration boundary, trace the notebook models and visualization implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about research notebooks and exploration boundary. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

**The core signal — `research()` (Preis et al. 2014)**

```
research(series, length=3) = series - series.rolling(length).mean().shift(1)
```

i.e. today's keyword interest minus the moving average of the previous *n* periods. The `.shift(1)` is what makes it usable: it is the deviation from trend known *before* today's observation, so the feature never leaks the current value. A positive value means search interest for the keyword is running above its own recent norm.

**The label — `target_binary(series)`**

The DJIA close series is converted to a percentage change and binarised: `1` when the index rose, `0` when it fell. This is a *direction* target — no magnitude information is modelled.

**The other engineered features**

| Function | Definition | Role |
| --- | --- | --- |
| `sma(series, length=6)` | rolling mean | Trend baseline |
| `ema(series, length=6)` | exponential moving average, `span=length`, `adjust=False` | Faster-reacting trend baseline |
| `delta(series, length=3)` | `series.diff(length)` | Absolute change over *n* periods |
| `pct_change(series, length=3)` | percen

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `notebooks/03-cpj-visualisation.ipynb` and the source focus `sns.lineplot`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The source is research-oriented and the UI is static; historical signals do not establish future returns. Avoid look-ahead leakage and never present outputs as investment advice.

## Step-by-step source investigation

1. Open `notebooks/03-cpj-visualisation.ipynb` and inspect `sns.lineplot`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `notebooks/03-cpj-visualisation.ipynb` (not executed during package generation):

```python
sns.set_style("whitegrid", {"font.sans_serif": "Liberation Sans"})
sns.set_context("notebook")

fig, ax = plt.subplots(1, 1, figsize = (7, 5), dpi=300)

sns.lineplot(data=unadjusted_data.monthly[1096:1826]/100, color="black")

ax.set_ylabel("")
ax.set_xlabel("")
ax.text(x=0.5, y=1.1, s="Actual Monthly Data", fontsize=16, weight='bold', ha='center', va='bottom', transform=ax.transAxes)
ax.text(x=0.5, y=1.05, s="The actual monthly data for this timespan, ", fontsize=8, alpha=0.75, ha='center', va='bottom', transform=ax.transAxes, )



# fig.savefig("graph1.png")
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For notebook models and visualization, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-04-02.md`](../exercises/exercise-04-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of notebook models and visualization, identify its source location, and state a limitation. The key project-specific fact is: **The core signal — `research()` (Preis et al. 2014)**

```
research(series, length=3) = series - series.rolling(length).mean().shift(1)
```

i.e. today's keyword interest minus the moving average of the previous *n* periods. The `.shift(1)` is what makes it usable: it is the deviation from trend known *before* today's observation, so the feature never leaks the current value. A positive value means search interest for the keyword is running above its own recent norm.

**The label — `target_binary(series)`**

The DJIA close series is converted to a percentage change and binarised: `1` when the index rose, `0` when it fell. This is a *direction* target — no magnitude information is modelled.

**The other engineered features**

| Function | Definition | Role |
| --- | --- | --- |
| `sma(series, length=6)` | rolling mean | Trend baseline |
| `ema(series, length=6)` | exponential moving average, `span=length`, `adjust=False` | Faster-reacting trend baseline |
| `delta(series, length=3)` | `series.diff(length)` | Absolute change over *n* periods |
| `pct_change(series, length=3)` | percen

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `notebooks/03-cpj-visualisation.ipynb` and the source focus `sns.lineplot`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
