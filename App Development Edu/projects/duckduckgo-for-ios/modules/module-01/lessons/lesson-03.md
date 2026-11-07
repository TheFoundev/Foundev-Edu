# Decide whether text is a web address or a search: Check behavior and limits

**Lesson ID:** `duckduckgo-for-ios-01-browser-core-and-url-routing-lesson-03`  
**Module ID:** `duckduckgo-for-ios-01-browser-core-and-url-routing`  
**Source focus:** `Sources/Core.swift` → `Core`

## Purpose and learning objectives

Use `Sources/Core.swift` at `Core` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

A feature is only reliable within the cases it handles. In plain terms, **Decide whether text is a web address or a search** means: A browser address box has two jobs: open a likely URL or search ordinary words. Read the core decision function and tests for empty text, scheme insertion, and selected engine behavior. Today we trace one normal path and one boundary.

### Step toward the implementation

Use `Sources/Core.swift` at `Core` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. The source files for this module are `Sources/Core.swift`, `Tests/BrowserCoreTests.swift`.

## Source evidence

Excerpt from [`Sources/Core.swift`](../../../../../../App%20Development/duckduckgo-for-ios/Sources/Core.swift); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```swift
import Foundation

/// The rules of the browser, without any SwiftUI or WebKit in them, so they
/// can be tested on their own.
public enum BrowserCore {

    // MARK: - Search

    /// A search engine the browser knows.
    public struct SearchEngine: Identifiable, Equatable {
        public let id: String
        public let name: String
        public let template: String

        public init(id: String, name: String, template: String) {
            self.id = id
            self.name = name
            self.template = template
        }

        /// The url of a search.
        public func url(for query: String) -> String {
            template.replacingOccurrences(of: "{query}", with: query)
        }
```

### Read it step by step

1. Find the focus cue `Core` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Decide whether text is a web address or a search**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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
- [Source file](../../../../../../App%20Development/duckduckgo-for-ios/Sources/Core.swift)
