# Code review and safe change 6: Trace the code

**Lesson ID:** `luigi-batch-etl-orchestrator-module-06-lesson-02`  
**Module ID:** `luigi-batch-etl-orchestrator-module-06`  
**Source focus:** `tests/test_pipeline.py` → `test_a_task_knows_what_it_needs_and_where_its_output_is`

## Purpose and learning objectives

Trace `test_a_task_knows_what_it_needs_and_where_its_output_is` in `tests/test_pipeline.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Code review and safe change 6.

## Beginner explanation

In plain language, code review and safe change 6 is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `tests/test_pipeline.py` and locate `test_a_task_knows_what_it_needs_and_where_its_output_is`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`, `web/api_impl.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: call graph; failure cases; safe extension

**Excerpt:** `tests/test_pipeline.py` at lines 14–34. Source code was not executed during refinement.

### main.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### src/pipeline.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### tests/test_pipeline.py

The excerpt below is the selected implementation focus.
### web/api_impl.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```py
assert capsys.readouterr().out.strip()


def test_a_task_knows_what_it_needs_and_where_its_output_is(tmp_path):
    task = Extract(base=str(tmp_path))
    assert isinstance(task.requires(), list)
    assert "extract" in str(task.output())


def test_the_tasks_run_in_the_order_of_the_dependencies(tmp_path):
    done = []
    execute(Load(base=str(tmp_path)), done)
    assert done == ["extract", "clean", "aggregate", "load"]


def test_a_task_runs_the_tasks_it_needs_first(tmp_path):
    done = []
    execute(Aggregate(base=str(tmp_path)), done)
    assert done.index("extract") < done.index("clean") < done.index("aggregate")
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

call graph; failure cases; safe extension The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-06.md`](../exercises/exercise-06.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `test_a_task_knows_what_it_needs_and_where_its_output_is` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `test_a_task_knows_what_it_needs_and_where_its_output_is` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
