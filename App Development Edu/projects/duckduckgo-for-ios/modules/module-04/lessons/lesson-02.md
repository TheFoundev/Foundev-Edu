# Content rules and private-mode clearing: Trace the source

**Lesson ID:** `duckduckgo-for-ios-04-tracker-rules-and-privacy-mode-lesson-02`  
**Module ID:** `duckduckgo-for-ios-04-tracker-rules-and-privacy-mode`  
**Source focus:** `Sources/Core.swift` → `Core`

## Purpose and learning objectives

Open `Sources/Core.swift` and locate `Core`. Read the signature, guards, transformation, and return/state update in that order. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

In everyday terms, the code path behind **Content rules and private-mode clearing** is like following one item through a workshop: locate the input, see what changes, then find the output. A rule list is a set of instructions sent to WebKit’s content blocker. Follow its JSON shape and how settings select it, then examine tests for private-mode cleanup and tracker counts.

### Step toward the implementation

Open `Sources/Core.swift` and locate `Core`. Read the signature, guards, transformation, and return/state update in that order. The source files for this module are `Sources/Core.swift`, `Sources/Models.swift`, `Sources/Screens/SettingsView.swift`, `Tests/BrowserCoreTests.swift`.

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

The lesson should produce a source-backed explanation of **Content rules and private-mode clearing**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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
