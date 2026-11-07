# Test routing, tab lifecycle, and privacy claims

**Lesson ID:** `duckduckgo-for-ios-06-tests-and-mini-project-release-lesson-01`  
**Project:** DuckDuckGo for iOS  
**Source focus:** `Tests/BrowserCoreTests.swift` — `func testThePrivateModeThrowsTheDataAway`

## Purpose and learning objectives

In plain terms, this lesson teaches **Tests are executable examples of expected browser rules. Compare each claim to source and tests, then identify runtime checks for navigation, persistence, and content rules**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `Tests/BrowserCoreTests.swift` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: No Xcode build was run in this workspace; simulator behavior remains unverified.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: Tests are executable examples of expected browser rules. Compare each claim to source and tests, then identify runtime checks for navigation, persistence, and content rules. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **XCTest coverage, XcodeGen project configuration, and documentation boundary**. This is a learning implementation, so keep the limit in view: No Xcode build was run in this workspace; simulator behavior remains unverified.

## Learning objectives

1. Describe the everyday behavior: Tests are executable examples of expected browser rules. Compare each claim to source and tests, then identify runtime checks for navigation, persistence, and content rules.
2. Find the relevant implementation in `Tests/BrowserCoreTests.swift` and explain the named symbol.
3. Trace the responsibility across the related files: `Tests/BrowserCoreTests.swift`, `project.yml`, `README.md`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: Tests are executable examples of expected browser rules. Compare each claim to source and tests, then identify runtime checks for navigation, persistence, and content rules. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **XCTest coverage, XcodeGen project configuration, and documentation boundary**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: No Xcode build was run in this workspace; simulator behavior remains unverified.

### 3. Read the real implementation

The excerpt below is copied directly from `Tests/BrowserCoreTests.swift` around `func testThePrivateModeThrowsTheDataAway`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```swift
    func testThePrivateModeThrowsTheDataAway() {
        XCTAssertTrue(BrowserCore.shouldDiscardData(privateMode: true))
        XCTAssertFalse(BrowserCore.shouldDiscardData(privateMode: false))
        XCTAssertFalse(BrowserCore.privateStoreName.isEmpty)
    }

    // MARK: - The tabs

    func testClosingATabLeavesTheOthers() {
        let tabs = [
            BrowserTabInfo(title: "One", urlString: "https://one.test"),
            BrowserTabInfo(title: "Two", urlString: "https://two.test"),
        ]
        let result = BrowserCore.tabsAfterClosing(tabs, at: 0)
        XCTAssertEqual(result.count, 1)
        XCTAssertEqual(result[0].title, "Two")
    }

```



The selected symbol is `func testThePrivateModeThrowsTheDataAway`. Relate its code to this source map:

- `Tests/BrowserCoreTests.swift` — inspect how this part participates in xctest coverage, xcodegen project configuration, and documentation boundary.
- `project.yml` — inspect how this part participates in xctest coverage, xcodegen project configuration, and documentation boundary.
- `README.md` — inspect how this part participates in xctest coverage, xcodegen project configuration, and documentation boundary.

### 4. Step-by-step source reading

1. Open `Tests/BrowserCoreTests.swift` and search for `func testThePrivateModeThrowsTheDataAway`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: Tests are executable examples of expected browser rules. Compare each claim to source and tests, then identify runtime checks for navigation, persistence, and content rules. The known limitation is explicit: No Xcode build was run in this workspace; simulator behavior remains unverified. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `duckduckgo-for-ios-06-tests-and-mini-project-release-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `Tests/BrowserCoreTests.swift`; UI labels alone do not define behavior.
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

You started from the user task, named its everyday model, followed `func testThePrivateModeThrowsTheDataAway` in `Tests/BrowserCoreTests.swift`, and traced the related files. The implemented behavior is **Tests are executable examples of expected browser rules. Compare each claim to source and tests, then identify runtime checks for navigation, persistence, and content rules**; the boundary is **No Xcode build was run in this workspace; simulator behavior remains unverified**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`Tests/BrowserCoreTests.swift`](../../../../../../projects/duckduckgo-for-ios/Tests/BrowserCoreTests.swift)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [Swiftui](https://developer.apple.com/documentation/swiftui/), [Webkit](https://developer.apple.com/documentation/webkit/wkwebview), [Xcodegen](https://github.com/yonaskolb/XcodeGen), [Xctest](https://developer.apple.com/documentation/xctest), [Owasp Mobile](https://mas.owasp.org/MASVS/)
