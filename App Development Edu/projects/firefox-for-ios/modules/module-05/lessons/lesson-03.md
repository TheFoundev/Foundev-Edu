# Share browser state across screens: Check behavior and limits

**Lesson ID:** `firefox-for-ios-05-state-and-screen-composition-lesson-03`  
**Module ID:** `firefox-for-ios-05-state-and-screen-composition`  
**Source focus:** `Sources/ContentView.swift` → `ContentView`

## Purpose and learning objectives

Use `Sources/ContentView.swift` at `ContentView` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

A feature is only reliable within the cases it handles. In plain terms, **Share browser state across screens** means: A shared store lets multiple screens show the same browser state. Trace initialization and environment injection before following a tap into a state-changing method. Today we trace one normal path and one boundary.

### Step toward the implementation

Use `Sources/ContentView.swift` at `ContentView` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. The source files for this module are `Sources/ContentView.swift`, `Sources/Screens/TabsView.swift`, `Sources/Screens/HomeView.swift`, `Sources/Screens/SettingsView.swift`.

## Source evidence

Excerpt from [`Sources/ContentView.swift`](../../../../../../App%20Development/firefox-for-ios/Sources/ContentView.swift); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var store = FirefoxStore()

    var body: some View {
        TabView {
            HomeView()
                .tabItem { Label("Home", systemImage: "house") }
            TabsView()
                .tabItem { Label("Tabs", systemImage: "square.on.square") }
            SettingsView()
                .tabItem { Label("Settings", systemImage: "gearshape") }
        }
        .tint(.accentColor)
        .environmentObject(store)
    }
}

#Preview {
    ContentView()
}
```

### Read it step by step

1. Find the focus cue `ContentView` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Share browser state across screens**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `ContentView` in `Sources/ContentView.swift`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/firefox-for-ios/Sources/ContentView.swift)
