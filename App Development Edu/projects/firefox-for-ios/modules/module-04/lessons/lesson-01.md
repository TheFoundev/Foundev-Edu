# Map a settings choice to tracker rules

**Lesson ID:** `firefox-for-ios-04-protection-levels-and-rules-lesson-01`  
**Project:** Firefox for iOS  
**Source focus:** `Sources/Core.swift` — `standardTrackers`

## Purpose and learning objectives

In plain terms, this lesson teaches **A protection switch chooses a collection of content rules. Follow the selected level into rule creation and display; distinguish a configured rule count from independently verified blocking**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `Sources/Core.swift` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: Rules are a small sample, not Firefox’s full tracking-protection lists or guarantees.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: A protection switch chooses a collection of content rules. Follow the selected level into rule creation and display; distinguish a configured rule count from independently verified blocking. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Protection modes, rule selection, rule compilation, and observed count**. This is a learning implementation, so keep the limit in view: Rules are a small sample, not Firefox’s full tracking-protection lists or guarantees.

## Learning objectives

1. Describe the everyday behavior: A protection switch chooses a collection of content rules. Follow the selected level into rule creation and display; distinguish a configured rule count from independently verified blocking.
2. Find the relevant implementation in `Sources/Core.swift` and explain the named symbol.
3. Trace the responsibility across the related files: `Sources/Core.swift`, `Sources/Models.swift`, `Sources/Screens/SettingsView.swift`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: A protection switch chooses a collection of content rules. Follow the selected level into rule creation and display; distinguish a configured rule count from independently verified blocking. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Protection modes, rule selection, rule compilation, and observed count**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: Rules are a small sample, not Firefox’s full tracking-protection lists or guarantees.

### 3. Read the real implementation

The excerpt below is copied directly from `Sources/Core.swift` around `standardTrackers`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```swift
    public static let strictTrackers: [String] = standardTrackers + [
        ".*mixpanel\\.com.*",
        ".*quantserve\\.com.*",
        ".*adnxs\\.com.*",
        ".*scorecardresearch\\.com.*",
        ".*appsflyer\\.com.*",
        ".*branch\\.io.*",
    ]

    /// The trackers the user can block by hand.
    public static let customTrackers: [String] = [
        ".*twitter\\.com.*",
        ".*linkedin\\.com.*",
        ".*tiktok\\.com.*",
    ]

    /// The rules of the content rule list of WebKit, as json.
    public static func contentRuleListJSON(level: ProtectionLevel, custom: [String] = customTrackers) -> String {
```



The selected symbol is `standardTrackers`. Relate its code to this source map:

- `Sources/Core.swift` — inspect how this part participates in protection modes, rule selection, rule compilation, and observed count.
- `Sources/Models.swift` — inspect how this part participates in protection modes, rule selection, rule compilation, and observed count.
- `Sources/Screens/SettingsView.swift` — inspect how this part participates in protection modes, rule selection, rule compilation, and observed count.

### 4. Step-by-step source reading

1. Open `Sources/Core.swift` and search for `standardTrackers`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: A protection switch chooses a collection of content rules. Follow the selected level into rule creation and display; distinguish a configured rule count from independently verified blocking. The known limitation is explicit: Rules are a small sample, not Firefox’s full tracking-protection lists or guarantees. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `firefox-for-ios-04-protection-levels-and-rules-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

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

You started from the user task, named its everyday model, followed `standardTrackers` in `Sources/Core.swift`, and traced the related files. The implemented behavior is **A protection switch chooses a collection of content rules. Follow the selected level into rule creation and display; distinguish a configured rule count from independently verified blocking**; the boundary is **Rules are a small sample, not Firefox’s full tracking-protection lists or guarantees**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`Sources/Core.swift`](../../../../../../projects/firefox-for-ios/Sources/Core.swift)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [Swiftui](https://developer.apple.com/documentation/swiftui/), [Webkit](https://developer.apple.com/documentation/webkit/wkwebview), [Xcodegen](https://github.com/yonaskolb/XcodeGen), [Xctest](https://developer.apple.com/documentation/xctest), [Owasp Mobile](https://mas.owasp.org/MASVS/)
