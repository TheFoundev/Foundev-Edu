# Use XCTest and XcodeGen to check the sample: Begin with the idea

**Lesson ID:** `kickstarter-for-ios-06-tests-and-platform-build-lesson-01`  
**Module ID:** `kickstarter-for-ios-06-tests-and-platform-build`  
**Source focus:** `Tests/ProjectCoreTests.swift` → `ProjectCoreTests`

## Purpose and learning objectives

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Basic programming and a way to read the source project.Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

Imagine **Use XCTest and XcodeGen to check the sample** as a small part of a phone app: it receives a value or action and helps produce a result. This module’s plain-language model is: Tests isolate rules and persistence using controlled defaults. The XcodeGen file describes build targets; on macOS, generate and run the simulator suite before calling it verified.

### Step toward the implementation

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. The source files for this module are `Tests/ProjectCoreTests.swift`, `project.yml`, `README.md`.

## Source evidence

Excerpt from [`Tests/ProjectCoreTests.swift`](../../../../../../App%20Development/kickstarter-for-ios/Tests/ProjectCoreTests.swift); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```swift
import XCTest
@testable import Kickstarter

final class ProjectCoreTests: XCTestCase {

    private func project(
        id: String = "p1",
        title: String = "A project",
        creator: String = "Someone",
        blurb: String = "A blurb",
        category: String = "Design",
        pledged: Int = 100,
        goal: Int = 1000,
        backers: Int = 10,
        daysLeft: Int = 5,
        status: String = "live"
    ) -> ProjectInfo {
        ProjectInfo(
            id: id, title: title, creator: creator, blurb: blurb, category: category,
            pledged: pledged, goal: goal, backers: backers, daysLeft: daysLeft, status: status
        )
    }
```

### Read it step by step

1. Find the focus cue `ProjectCoreTests` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Use XCTest and XcodeGen to check the sample**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `ProjectCoreTests` in `Tests/ProjectCoreTests.swift`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/kickstarter-for-ios/Tests/ProjectCoreTests.swift)
