# Find projects in a local catalogue: Begin with the idea

**Lesson ID:** `kickstarter-for-ios-02-discovery-search-and-categories-lesson-01`  
**Module ID:** `kickstarter-for-ios-02-discovery-search-and-categories`  
**Source focus:** `Sources/Core.swift` → `Core`

## Purpose and learning objectives

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Basic programming and a way to read the source project.Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

Imagine **Find projects in a local catalogue** as a small part of a phone app: it receives a value or action and helps produce a result. This module’s plain-language model is: Search and category controls narrow the sample catalogue. Follow the selected filter into the store/core and verify how the view receives the filtered projects.

### Step toward the implementation

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. The source files for this module are `Sources/Core.swift`, `Sources/Screens/DiscoverView.swift`, `Tests/ProjectCoreTests.swift`.

## Source evidence

Excerpt from [`Sources/Core.swift`](../../../../../../App%20Development/kickstarter-for-ios/Sources/Core.swift); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```swift
import Foundation

/// The rules of the app, without any SwiftUI in them, so they can be tested
/// on their own.
public enum ProjectCore {

    // MARK: - The categories

    /// The categories the projects are grouped in.
    public static let categories = ["Technology", "Food", "Design", "Community", "Music", "All"]

    /// The projects of a category.
    public static func projects(in category: String, from projects: [ProjectInfo]) -> [ProjectInfo] {
        if category == "All" || category.isEmpty { return projects }
        return projects.filter { $0.category == category }
    }

    /// The projects that match a search.
    ///
    /// The title, the blurb and the creator are searched.
    public static func search(_ projects: [ProjectInfo], query: String) -> [ProjectInfo] {
        let needle = query.trimmingCharacters(in: .whitespacesAndNewlines).lowercased()
        guard !needle.isEmpty else { return projects }
        return projects.filter {
```

### Read it step by step

1. Find the focus cue `Core` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Find projects in a local catalogue**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `Core` in `Sources/Core.swift`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/kickstarter-for-ios/Sources/Core.swift)
