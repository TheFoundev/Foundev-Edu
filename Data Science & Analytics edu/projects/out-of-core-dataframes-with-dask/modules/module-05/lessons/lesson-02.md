# Documented goals mapped to implementation: Trace the code

**Lesson ID:** `out-of-core-dataframes-with-dask-module-05-lesson-02`  
**Module ID:** `out-of-core-dataframes-with-dask-module-05`  
**Source focus:** `src/pipeline.py` → `write_partitions`

## Purpose and learning objectives

Trace `write_partitions` in `src/pipeline.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Documented goals mapped to implementation.

## Beginner explanation

In plain language, documented goals mapped to implementation is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `src/pipeline.py` and locate `write_partitions`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `README.md`, `main.py`, `src/pipeline.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: documentation claims; implementation mapping; limitations

**Excerpt:** `src/pipeline.py` at lines 5–25. Source code was not executed during refinement.

### README.md

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### main.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### src/pipeline.py

The excerpt below is the selected implementation focus.

```py
import pandas as pd


def write_partitions(base, chunks=4, rows_per_chunk=2000, seed=42):
    rng = np.random.default_rng(seed)
    input_dir = base / "input"
    input_dir.mkdir(parents=True, exist_ok=True)
    regions = np.array(["north", "south", "east", "west"])
    products = np.array(["widget", "gadget", "cable", "stand", "sensor"])
    for chunk in range(chunks):
        frame = pd.DataFrame({
            "order_id": np.arange(chunk * rows_per_chunk, (chunk + 1) * rows_per_chunk),
            "region": rng.choice(regions, rows_per_chunk),
            "product": rng.choice(products, rows_per_chunk),
            "quantity": rng.integers(1, 8, rows_per_chunk),
            "unit_price": np.round(rng.uniform(3, 45, rows_per_chunk), 2),
        })
        frame["revenue"] = (frame["quantity"] * frame["unit_price"]).round(2)
        frame.to_csv(input_dir / f"part-{chunk:03d}.csv", index=False)
    return sorted(input_dir.glob("part-*.csv"))
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

documentation claims; implementation mapping; limitations The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

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

You moved from a plain-language model to `write_partitions` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `write_partitions` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
