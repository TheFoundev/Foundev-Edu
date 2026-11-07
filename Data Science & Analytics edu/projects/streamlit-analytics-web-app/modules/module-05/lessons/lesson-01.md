# Declared dependencies and runtime configuration: Begin with the concept

**Lesson ID:** `streamlit-analytics-web-app-module-05-lesson-01`  
**Module ID:** `streamlit-analytics-web-app-module-05`  
**Source focus:** `app.py` → `read_subscriptions`

## Purpose and learning objectives

Explain declared dependencies and runtime configuration in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: Declared dependencies and runtime configuration.

## Beginner explanation

In plain language, declared dependencies and runtime configuration is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `app.py` and locate `read_subscriptions`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `requirements.txt`, `app.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: declared dependencies; configuration keys; safe setup

**Excerpt:** `app.py` at lines 25–45. Source code was not executed during refinement.

### requirements.txt

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### app.py

The excerpt below is the selected implementation focus.

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

First read the signature/declared data shape; then follow the code and caller.

## Expected behavior and limits

declared dependencies; configuration keys; safe setup The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-05.md`](../exercises/exercise-05.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

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
