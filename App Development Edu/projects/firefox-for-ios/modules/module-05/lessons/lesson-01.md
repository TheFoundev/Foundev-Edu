# Share browser state across screens

**Lesson ID:** `firefox-for-ios-05-state-and-screen-composition-lesson-01`  
**Project:** Firefox for iOS  
**Source focus:** `Sources/ContentView.swift` — `struct ContentView`

## Purpose and learning objectives

In plain terms, this lesson teaches **A shared store lets multiple screens show the same browser state. Trace initialization and environment injection before following a tap into a state-changing method**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `Sources/ContentView.swift` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: Account sync, history sync, and production data management are not implemented.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: A shared store lets multiple screens show the same browser state. Trace initialization and environment injection before following a tap into a state-changing method. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Observable store lifecycle, tab navigation, and settings binding**. This is a learning implementation, so keep the limit in view: Account sync, history sync, and production data management are not implemented.

## Learning objectives

1. Describe the everyday behavior: A shared store lets multiple screens show the same browser state. Trace initialization and environment injection before following a tap into a state-changing method.
2. Find the relevant implementation in `Sources/ContentView.swift` and explain the named symbol.
3. Trace the responsibility across the related files: `Sources/ContentView.swift`, `Sources/Screens/TabsView.swift`, `Sources/Screens/HomeView.swift`, `Sources/Screens/SettingsView.swift`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: A shared store lets multiple screens show the same browser state. Trace initialization and environment injection before following a tap into a state-changing method. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Observable store lifecycle, tab navigation, and settings binding**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: Account sync, history sync, and production data management are not implemented.

### 3. Read the real implementation

The excerpt below is copied directly from `Sources/ContentView.swift` around `struct ContentView`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```swift
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
```



The selected symbol is `struct ContentView`. Relate its code to this source map:

- `Sources/ContentView.swift` — inspect how this part participates in observable store lifecycle, tab navigation, and settings binding.
- `Sources/Screens/TabsView.swift` — inspect how this part participates in observable store lifecycle, tab navigation, and settings binding.
- `Sources/Screens/HomeView.swift` — inspect how this part participates in observable store lifecycle, tab navigation, and settings binding.
- `Sources/Screens/SettingsView.swift` — inspect how this part participates in observable store lifecycle, tab navigation, and settings binding.

### 4. Step-by-step source reading

1. Open `Sources/ContentView.swift` and search for `struct ContentView`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: A shared store lets multiple screens show the same browser state. Trace initialization and environment injection before following a tap into a state-changing method. The known limitation is explicit: Account sync, history sync, and production data management are not implemented. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `firefox-for-ios-05-state-and-screen-composition-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

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

You started from the user task, named its everyday model, followed `struct ContentView` in `Sources/ContentView.swift`, and traced the related files. The implemented behavior is **A shared store lets multiple screens show the same browser state. Trace initialization and environment injection before following a tap into a state-changing method**; the boundary is **Account sync, history sync, and production data management are not implemented**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`Sources/ContentView.swift`](../../../../../../projects/firefox-for-ios/Sources/ContentView.swift)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [Swiftui](https://developer.apple.com/documentation/swiftui/), [Webkit](https://developer.apple.com/documentation/webkit/wkwebview), [Xcodegen](https://github.com/yonaskolb/XcodeGen), [Xctest](https://developer.apple.com/documentation/xctest), [Owasp Mobile](https://mas.owasp.org/MASVS/)
