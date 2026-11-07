# Compose discovery, detail, and reusable poster views: Begin with the idea

**Lesson ID:** `movieswiftui-05-detail-and-view-composition-lesson-01`  
**Module ID:** `movieswiftui-05-detail-and-view-composition`  
**Source focus:** `Sources/ContentView.swift` → `ContentView`

## Purpose and learning objectives

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Basic programming and a way to read the source project.Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

Imagine **Compose discovery, detail, and reusable poster views** as a small part of a phone app: it receives a value or action and helps produce a result. This module’s plain-language model is: SwiftUI composes reusable views around the selected movie. Follow the navigation value into the detail and understand which fields are present even when artwork is only a placeholder.

### Step toward the implementation

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. The source files for this module are `Sources/ContentView.swift`, `Sources/Components.swift`, `Sources/Screens/MovieDetailView.swift`, `Sources/Screens/DiscoverView.swift`.

## Source evidence

Excerpt from [`Sources/ContentView.swift`](../../../../../../App%20Development/movieswiftui/Sources/ContentView.swift); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var store = MovieStore()

    var body: some View {
        TabView {
            DiscoverView()
                .tabItem { Label("Discover", systemImage: "sparkles") }
            SearchView()
                .tabItem { Label("Search", systemImage: "magnifyingglass") }
            WatchlistView()
                .tabItem { Label("Watchlist", systemImage: "bookmark") }
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

The lesson should produce a source-backed explanation of **Compose discovery, detail, and reusable poster views**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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
- [Source file](../../../../../../App%20Development/movieswiftui/Sources/ContentView.swift)
