# Data Acquisition and Feature Building: Validate outputs and identify limitations for data acquisition and feature building

**Lesson ID:** `lesson-02-03`  
**Module:** Data Acquisition and Feature Building  
**Source focus:** `src/data/update_data.py` → `update_daily`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by TrendCast: Stock Price Trend Research. By the end, you can describe update_data, make_dataset, and Google Trends, trace the data acquisition and feature building implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about update_data, make_dataset, and Google Trends. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `update_daily` in `src/data/update_data.py`. Use the excerpt below to trace the actual inputs, transformation, and output for update_data, make_dataset, and Google Trends. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The source is research-oriented and the UI is static; historical signals do not establish future returns. Avoid look-ahead leakage and never present outputs as investment advice.

## Step-by-step source investigation

1. Open `src/data/update_data.py` and inspect `update_daily`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/data/update_data.py` (not executed during package generation):

```python
def update_daily():
    """
    Updates the daily Google Trends data.
    """

    with open('src/data/keywords.txt', 'r') as f:
        for line in f:
            keyword = line.strip()
            keyword_url = keyword.replace(' ', '%20')
            keyword_file = keyword.replace(' ', '_')

            current = pd.read_csv(f'data/raw/daily/{keyword_file}.csv')

            start_date = datetime.datetime.strptime(
                current.loc[len(current)-1, 'Date'], '%Y-%m-%d').date()
            end_date = datetime.date.today()

            token = get_token(keyword, f'{start_date} {end_date}')

            url = 'https://trends.google.com/trends/api/widgetdata/multilin' \
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For data acquisition and feature building, use the repository's own output format and the available test fixture where possible.

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

You can now validate outputs and identify limitations for data acquisition and feature building, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for data acquisition and feature building. In this repository, the claim must be grounded in the documented behavior and source paths: src/data/update_data.py; src/data/make_dataset.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
