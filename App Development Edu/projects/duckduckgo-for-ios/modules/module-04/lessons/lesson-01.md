# Content rules and private-mode clearing

**Lesson ID:** `duckduckgo-for-ios-04-tracker-rules-and-privacy-mode-lesson-01`  
**Project:** DuckDuckGo for iOS  
**Source focus:** `Sources/Core.swift` — `trackerPatterns`

## Purpose and learning objectives

In plain terms, this lesson teaches **A rule list is a set of instructions sent to WebKit’s content blocker. Follow its JSON shape and how settings select it, then examine tests for private-mode cleanup and tracker counts**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `Sources/Core.swift` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: The sample rules are limited; a counter is not proof that every tracker was blocked.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: A rule list is a set of instructions sent to WebKit’s content blocker. Follow its JSON shape and how settings select it, then examine tests for private-mode cleanup and tracker counts. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Rule-list JSON, rule compilation, blocked-count reporting, and private data behavior**. This is a learning implementation, so keep the limit in view: The sample rules are limited; a counter is not proof that every tracker was blocked.

## Learning objectives

1. Describe the everyday behavior: A rule list is a set of instructions sent to WebKit’s content blocker. Follow its JSON shape and how settings select it, then examine tests for private-mode cleanup and tracker counts.
2. Find the relevant implementation in `Sources/Core.swift` and explain the named symbol.
3. Trace the responsibility across the related files: `Sources/Core.swift`, `Sources/Models.swift`, `Sources/Screens/SettingsView.swift`, `Tests/BrowserCoreTests.swift`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: A rule list is a set of instructions sent to WebKit’s content blocker. Follow its JSON shape and how settings select it, then examine tests for private-mode cleanup and tracker counts. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Rule-list JSON, rule compilation, blocked-count reporting, and private data behavior**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: The sample rules are limited; a counter is not proof that every tracker was blocked.

### 3. Read the real implementation

The excerpt below is copied directly from `Sources/Core.swift` around `trackerPatterns`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```swift
    public static var blockingRuleCount: Int { trackerPatterns.count }

    // MARK: - Private mode

    /// The name of the data store of the private mode.
    ///
    /// A private window keeps its data in a store of its own, which is
    /// thrown away when the window closes.
    public static let privateStoreName = "duckduckgo-private"

    /// True when the data store of a window has to be thrown away.
    public static func shouldDiscardData(privateMode: Bool) -> Bool { privateMode }

    // MARK: - The tabs

    /// The tabs that are left after a tab is closed.
    public static func tabsAfterClosing(_ tabs: [BrowserTabInfo], at offset: Int) -> [BrowserTabInfo] {
        var result = tabs
```



The selected symbol is `trackerPatterns`. Relate its code to this source map:

- `Sources/Core.swift` — inspect how this part participates in rule-list json, rule compilation, blocked-count reporting, and private data behavior.
- `Sources/Models.swift` — inspect how this part participates in rule-list json, rule compilation, blocked-count reporting, and private data behavior.
- `Sources/Screens/SettingsView.swift` — inspect how this part participates in rule-list json, rule compilation, blocked-count reporting, and private data behavior.
- `Tests/BrowserCoreTests.swift` — inspect how this part participates in rule-list json, rule compilation, blocked-count reporting, and private data behavior.

### 4. Step-by-step source reading

1. Open `Sources/Core.swift` and search for `trackerPatterns`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: A rule list is a set of instructions sent to WebKit’s content blocker. Follow its JSON shape and how settings select it, then examine tests for private-mode cleanup and tracker counts. The known limitation is explicit: The sample rules are limited; a counter is not proof that every tracker was blocked. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `duckduckgo-for-ios-04-tracker-rules-and-privacy-mode-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `Sources/Core.swift`; UI labels alone do not define behavior.
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

You started from the user task, named its everyday model, followed `trackerPatterns` in `Sources/Core.swift`, and traced the related files. The implemented behavior is **A rule list is a set of instructions sent to WebKit’s content blocker. Follow its JSON shape and how settings select it, then examine tests for private-mode cleanup and tracker counts**; the boundary is **The sample rules are limited; a counter is not proof that every tracker was blocked**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`Sources/Core.swift`](../../../../../../projects/duckduckgo-for-ios/Sources/Core.swift)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [Swiftui](https://developer.apple.com/documentation/swiftui/), [Webkit](https://developer.apple.com/documentation/webkit/wkwebview), [Xcodegen](https://github.com/yonaskolb/XcodeGen), [Xctest](https://developer.apple.com/documentation/xctest), [Owasp Mobile](https://mas.owasp.org/MASVS/)
