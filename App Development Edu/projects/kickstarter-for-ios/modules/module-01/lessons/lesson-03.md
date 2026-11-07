# A project card starts with a project record: Check behavior and limits

**Lesson ID:** `kickstarter-for-ios-01-project-records-and-sample-catalogue-lesson-03`  
**Module ID:** `kickstarter-for-ios-01-project-records-and-sample-catalogue`  
**Source focus:** `Sources/Models.swift` → `Models`

## Purpose and learning objectives

Use `Sources/Models.swift` at `Models` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

A feature is only reliable within the cases it handles. In plain terms, **A project card starts with a project record** means: A crowdfunding card is a view of a project record. Read fields such as goal and pledged amount, then follow computed progress into the reusable card UI. Today we trace one normal path and one boundary.

### Step toward the implementation

Use `Sources/Models.swift` at `Models` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. The source files for this module are `Sources/Models.swift`, `Sources/Components.swift`.

## Source evidence

Excerpt from [`Sources/Models.swift`](../../../../../../App%20Development/kickstarter-for-ios/Sources/Models.swift); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```text
Source excerpt unavailable; inspect this source path and locate the focus symbol before teaching this module.
```

### Read it step by step

1. Find the focus cue `Models` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **A project card starts with a project record**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

## Practical exercise

Complete [`exercise-01.json`](../exercises/exercise-01.json). Add an input or edge case, cite the source, and write the expected result before changing code.

## Common mistakes and debugging

- Inferring feature behavior from the product name or screen alone.
- Skipping the caller, model/state layer, or error path.
- Treating local sample data or a mock response as a real service result.
- Debug by tracing input → validation → transformation → output and then checking the relevant test.

## Best practices and security

Protect credentials and personal data, validate untrusted inputs, request only necessary device permissions, and keep provider/device behavior explicitly unverified until tested in an authorized environment.

## Summary

You began with the module’s plain meaning, traced `Models` in `Sources/Models.swift`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/kickstarter-for-ios/Sources/Models.swift)
