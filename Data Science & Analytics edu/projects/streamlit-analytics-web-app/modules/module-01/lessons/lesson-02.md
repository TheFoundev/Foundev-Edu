# App and Main: Trace the code

**Lesson ID:** `streamlit-analytics-web-app-module-01-lesson-02`  
**Module ID:** `streamlit-analytics-web-app-module-01`  
**Source focus:** `app.py` → `read_subscriptions`

## Purpose and learning objectives

Trace `read_subscriptions` in `app.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: App and Main.

## Beginner explanation

In plain language, app and main is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `app.py` and locate `read_subscriptions`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `app.py`, `main.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `app.py` at lines 25–45. Source code was not executed during refinement.

### app.py

The excerpt below is the selected implementation focus.
### main.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```py
@st.cache_data(ttl=300)
def read_subscriptions(data_dir: str) -> pd.DataFrame:
    """The subscriptions, cached so the page is quick."""
    return load(data_dir)


st.title("Subscription analytics")
st.caption(
    "The MRR is the monthly fee of the subscriptions that are running in the month. "
    "The average fee is the MRR of the month divided by the number of active "
    "subscriptions, the churn is the share of the running subscriptions that "
    "ended in the month, and the net revenue retention says how much the "
    "customers that were already there brought in."
)

frame = read_subscriptions(str(DATA_DIR))

with st.sidebar:
    st.header("Filters")
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-01.md`](../exercises/exercise-01.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `read_subscriptions` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `read_subscriptions` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
