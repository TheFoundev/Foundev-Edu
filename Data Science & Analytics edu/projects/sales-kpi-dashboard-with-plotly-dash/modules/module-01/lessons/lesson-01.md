# App and Main: Begin with the concept

**Lesson ID:** `sales-kpi-dashboard-with-plotly-dash-module-01-lesson-01`  
**Module ID:** `sales-kpi-dashboard-with-plotly-dash-module-01`  
**Source focus:** `app.py` → `index`

## Purpose and learning objectives

Explain app and main in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: App and Main.

## Beginner explanation

In plain language, app and main is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `app.py` and locate `index`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `app.py`, `main.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `app.py` at lines 45–65. Source code was not executed during refinement.

### app.py

The excerpt below is the selected implementation focus.
### main.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```py
@app.route("/demo")
def index():
    kpis = json.loads(Path("artifacts/kpis.json").read_text())
    return render_template_string(PAGE, kpis=kpis)


@app.route("/chart")
def chart():
    return send_file(Path("artifacts/revenue_trend.png"), mimetype="image/png")


# ------------------------------------------------------------------ #
# The web layer of the project                                        #
# ------------------------------------------------------------------ #

@app.route("/")
def site_index():
    """The home page of the site of the project."""
    return send_from_directory(WEB, "index.html")
```

First read the signature/declared data shape; then follow the code and caller.

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

You moved from a plain-language model to `index` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `index` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
