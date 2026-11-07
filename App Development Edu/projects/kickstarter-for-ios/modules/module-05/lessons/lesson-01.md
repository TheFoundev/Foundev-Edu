# Build a screen flow around one observable store

**Lesson ID:** `kickstarter-for-ios-05-swiftui-navigation-and-shared-store-lesson-01`  
**Project:** Kickstarter for iOS  
**Source focus:** `Sources/ContentView.swift` — `struct ContentView`

## Purpose and learning objectives

In plain terms, this lesson teaches **SwiftUI views describe the screens from current model state. Follow the shared store from the app root into lists, reusable cards, profile, and detail actions, then see state changes refresh the UI**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `Sources/ContentView.swift` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: The source is a compact educational client, not production Kickstarter UI.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: SwiftUI views describe the screens from current model state. Follow the shared store from the app root into lists, reusable cards, profile, and detail actions, then see state changes refresh the UI. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Environment object injection, NavigationStack, and view actions**. This is a learning implementation, so keep the limit in view: The source is a compact educational client, not production Kickstarter UI.

## Learning objectives

1. Describe the everyday behavior: SwiftUI views describe the screens from current model state. Follow the shared store from the app root into lists, reusable cards, profile, and detail actions, then see state changes refresh the UI.
2. Find the relevant implementation in `Sources/ContentView.swift` and explain the named symbol.
3. Trace the responsibility across the related files: `Sources/ContentView.swift`, `Sources/Components.swift`, `Sources/Screens/DiscoverView.swift`, `Sources/Screens/SavedView.swift`, `Sources/Screens/ProjectDetailView.swift`, `Sources/Screens/ProfileView.swift`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: SwiftUI views describe the screens from current model state. Follow the shared store from the app root into lists, reusable cards, profile, and detail actions, then see state changes refresh the UI. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Environment object injection, NavigationStack, and view actions**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: The source is a compact educational client, not production Kickstarter UI.

### 3. Read the real implementation

The excerpt below is copied directly from `Sources/ContentView.swift` around `struct ContentView`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```swift
struct ContentView: View {
    @StateObject private var store = ProjectStore()

    var body: some View {
        TabView {
            DiscoverView()
                .tabItem { Label("Discover", systemImage: "safari") }
            SavedView()
                .tabItem { Label("Saved", systemImage: "bookmark") }
            ProfileView()
                .tabItem { Label("Profile", systemImage: "person.crop.circle") }
        }
        .tint(.accentColor)
        .environmentObject(store)
    }
}

#Preview {
```



The selected symbol is `struct ContentView`. Relate its code to this source map:

- `Sources/ContentView.swift` — inspect how this part participates in environment object injection, navigationstack, and view actions.
- `Sources/Components.swift` — inspect how this part participates in environment object injection, navigationstack, and view actions.
- `Sources/Screens/DiscoverView.swift` — inspect how this part participates in environment object injection, navigationstack, and view actions.
- `Sources/Screens/SavedView.swift` — inspect how this part participates in environment object injection, navigationstack, and view actions.
- `Sources/Screens/ProjectDetailView.swift` — inspect how this part participates in environment object injection, navigationstack, and view actions.
- `Sources/Screens/ProfileView.swift` — inspect how this part participates in environment object injection, navigationstack, and view actions.

### 4. Step-by-step source reading

1. Open `Sources/ContentView.swift` and search for `struct ContentView`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: SwiftUI views describe the screens from current model state. Follow the shared store from the app root into lists, reusable cards, profile, and detail actions, then see state changes refresh the UI. The known limitation is explicit: The source is a compact educational client, not production Kickstarter UI. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `kickstarter-for-ios-05-swiftui-navigation-and-shared-store-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `Sources/ContentView.swift`; UI labels alone do not define behavior.
- **Assuming a product-name feature exists:** compare the implementation and the limitation above with the project README.
- **Changing state in several places:** identify the owning model/store/context before editing.
- **Calling a test a full-system check:** determine whether it uses fake data, fake storage, a fake socket, or a real runtime.
- **Debug sequence:** reproduce the behavior, inspect the relevant input, log or assert the model result, verify the caller and rendered state, then check persistence or network boundaries separately.

## Best practices and security

- Keep this behavior small and testable; make validation and failure outcomes explicit.
- Preserve the typed boundary and avoid trusting unvalidated input.
- Do not place credentials, private keys, health details, financial records, or trusted-network controls in an insecure client setting.
- If a service integration is proposed, add authentication, transport protection, privacy review, and provider-specific tests before describing it as implemented.
- See the project-specific review items and [Owasp Mobile](https://mas.owasp.org/MASVS/).

## Summary

You started from the user task, named its everyday model, followed `struct ContentView` in `Sources/ContentView.swift`, and traced the related files. The implemented behavior is **SwiftUI views describe the screens from current model state. Follow the shared store from the app root into lists, reusable cards, profile, and detail actions, then see state changes refresh the UI**; the boundary is **The source is a compact educational client, not production Kickstarter UI**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`Sources/ContentView.swift`](../../../../../../projects/kickstarter-for-ios/Sources/ContentView.swift)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [Swiftui](https://developer.apple.com/documentation/swiftui/), [Xcodegen](https://github.com/yonaskolb/XcodeGen), [Xctest](https://developer.apple.com/documentation/xctest), [Owasp Mobile](https://mas.owasp.org/MASVS/)
