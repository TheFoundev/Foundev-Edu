# Convert untrusted response data into movie records: Begin with the idea

**Lesson ID:** `movieswiftui-02-api-response-mapping-lesson-01`  
**Module ID:** `movieswiftui-02-api-response-mapping`  
**Source focus:** `Sources/Core.swift` → `Core`

## Purpose and learning objectives

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Basic programming and a way to read the source project.Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

Imagine **Convert untrusted response data into movie records** as a small part of a phone app: it receives a value or action and helps produce a result. This module’s plain-language model is: A mapper is a translator between an external shape and the app’s model. Follow the function that accepts a generic response and the test that rejects incomplete fields.

### Step toward the implementation

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. The source files for this module are `Sources/Core.swift`, `Tests/MovieCoreTests.swift`.

## Source evidence

Excerpt from [`Sources/Core.swift`](../../../../../../App%20Development/movieswiftui/Sources/Core.swift); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```swift
import Foundation

/// The rules of the app, without any SwiftUI in them, so they can be tested
/// on their own.
public enum MovieCore {

    // MARK: - The catalogue

    /// The answer of the API of the films, in the shape the app uses.
    ///
    /// The API of TMDB answers with a dictionary per film, and the fields
    /// are named the way the API names them.
    public static func movie(from json: [String: Any]) -> MovieInfo? {
        guard let id = number(json["id"]) else { return nil }
        guard let title = json["title"] as? String else { return nil }

        let genres = (json["genres"] as? [[String: Any]] ?? [])
            .compactMap { $0["name"] as? String }
        let posterPath = (json["poster_path"] as? String) ?? ""
        let release = json["release_date"] as? String ?? ""

        return MovieInfo(
            id: id,
            title: title,
```

### Read it step by step

1. Find the focus cue `Core` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Convert untrusted response data into movie records**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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
- [Source file](../../../../../../App%20Development/movieswiftui/Sources/Core.swift)
