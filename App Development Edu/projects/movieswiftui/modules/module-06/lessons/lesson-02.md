# Read test evidence and plan runtime checks: Trace the source

**Lesson ID:** `movieswiftui-06-tests-and-mini-project-release-lesson-02`  
**Module ID:** `movieswiftui-06-tests-and-mini-project-release`  
**Source focus:** `Tests/MovieCoreTests.swift` → `MovieCoreTests`

## Purpose and learning objectives

Open `Tests/MovieCoreTests.swift` and locate `MovieCoreTests`. Read the signature, guards, transformation, and return/state update in that order. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

In everyday terms, the code path behind **Read test evidence and plan runtime checks** is like following one item through a workshop: locate the input, see what changes, then find the output. The tests exercise core functions and model persistence, not visual correctness or a provider. Use the project spec to run them on macOS and add screen-level checks.

### Step toward the implementation

Open `Tests/MovieCoreTests.swift` and locate `MovieCoreTests`. Read the signature, guards, transformation, and return/state update in that order. The source files for this module are `Tests/MovieCoreTests.swift`, `project.yml`, `README.md`.

## Source evidence

Excerpt from [`Tests/MovieCoreTests.swift`](../../../../../../App%20Development/movieswiftui/Tests/MovieCoreTests.swift); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```swift
import XCTest
@testable import MoviesSwiftUI

final class MovieCoreTests: XCTestCase {

    private func info(
        id: Int = 1,
        title: String = "A film",
        year: Int = 2020,
        genres: [String] = ["Drama"],
        overview: String = "An overview",
        rating: Double = 7.5,
        runtime: Int = 120,
        posterURL: String = ""
    ) -> MovieInfo {
        MovieInfo(
            id: id, title: title, year: year, genres: genres, overview: overview,
            rating: rating, runtime: runtime, posterURL: posterURL
        )
    }

    // MARK: - The answer of the API
```

### Read it step by step

1. Find the focus cue `MovieCoreTests` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Read test evidence and plan runtime checks**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `MovieCoreTests` in `Tests/MovieCoreTests.swift`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/movieswiftui/Tests/MovieCoreTests.swift)
