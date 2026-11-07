# Render navigation through WebKit: Check behavior and limits

**Lesson ID:** `firefox-for-ios-03-webkit-browser-wrapper-lesson-03`  
**Module ID:** `firefox-for-ios-03-webkit-browser-wrapper`  
**Source focus:** `Sources/WebView.swift` → `WebView`

## Purpose and learning objectives

Use `Sources/WebView.swift` at `WebView` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

A feature is only reliable within the cases it handles. In plain terms, **Render navigation through WebKit** means: The app’s native controls sit around a WebKit page. Follow a selected URL into the wrapper and understand which behavior is delegated to Apple’s WebKit engine. Today we trace one normal path and one boundary.

### Step toward the implementation

Use `Sources/WebView.swift` at `WebView` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. The source files for this module are `Sources/WebView.swift`, `Sources/Screens/BrowserScreen.swift`.

## Source evidence

Excerpt from [`Sources/WebView.swift`](../../../../../../App%20Development/firefox-for-ios/Sources/WebView.swift); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```swift
import SwiftUI
import WebKit

struct WebView: UIViewRepresentable {
    let url: URL
    /// True when the trackers are blocked.
    var blockTrackers: Bool = true
    /// The level of the tracking protection.
    var protectionLevel: BrowserCore.ProtectionLevel = .standard
    /// The trackers the user blocks by hand.
    var customTrackers: [String] = BrowserCore.customTrackers
    /// True when the tab is in the private mode.
    var privateMode: Bool = false

    func makeCoordinator() -> Coordinator {
        Coordinator()
    }

    func makeUIView(context: Context) -> WKWebView {
        let configuration = WKWebViewConfiguration()

        // A private tab keeps its data in a store of its own, which is thrown
        // away when the app closes.
```

### Read it step by step

1. Find the focus cue `WebView` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Render navigation through WebKit**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `WebView` in `Sources/WebView.swift`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/firefox-for-ios/Sources/WebView.swift)
