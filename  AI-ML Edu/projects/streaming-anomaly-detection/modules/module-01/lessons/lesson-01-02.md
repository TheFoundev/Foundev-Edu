# Task, Input Contract, and Source Scope: Inspect the project implementation of task, input contract, and source scope

**Lesson ID:** `lesson-01-02`  
**Module:** Task, Input Contract, and Source Scope  
**Source focus:** `README.md` → `main`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Streaming Anomaly Detection. By the end, you can describe Think of Streaming Anomaly Detection as a small workshop: the input is prepared, a method transforms it, and a result is checked. The brief and the implementation may describe different levels of ambition., trace the task, input contract, and source scope implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about Think of Streaming Anomaly Detection as a small workshop: the input is prepared, a method transforms it, and a result is checked. The brief and the implementation may describe different levels of ambition.. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `main` in `main.py`. Use the excerpt below to trace the actual inputs, transformation, and output for Think of Streaming Anomaly Detection as a small workshop: the input is prepared, a method transforms it, and a result is checked. The brief and the implementation may describe different levels of ambition.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The stream is generated, not read from NAB.

## Step-by-step source investigation

1. Open `main.py` and inspect `main`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `main.py` (not executed during package generation):

```python
args = parser.parse_args()

    if args.command == "info":
        print('Detect anomalies in a streaming numeric signal.')
        print("Run `python main.py train` to fit the model, or `demo` for a sample.")
        return

    data = load_data(seed=args.seed, quick=args.quick)
    if args.command == "demo":
        demo(data)
        return

    model, metrics = train(data, quick=args.quick)
    out = Path("artifacts")
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For task, input contract, and source scope, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-01-02.md`](../exercises/exercise-01-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of task, input contract, and source scope, identify its source location, and state a limitation. The key project-specific fact is: The source-specific focus for this module is `main` in `main.py`. Use the excerpt below to trace the actual inputs, transformation, and output for Think of Streaming Anomaly Detection as a small workshop: the input is prepared, a method transforms it, and a result is checked. The brief and the implementation may describe different levels of ambition.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository `README.md` and cited code files (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
