# Architecture — DuckDuckGo for iOS

Build a SwiftUI/WebKit browser sample with search routing, tabs, settings, tracker-rule demonstrations, and a private-mode data policy.

## Data and behavior map

1. **Decide whether text is a web address or a search** — `Sources/Core.swift` (`func destination`): Input classification, scheme handling, empty input, and search-engine selection. Related files: Sources/Core.swift; Tests/BrowserCoreTests.swift.
2. **Tabs as identifiable records** — `Sources/Models.swift` (`final class BrowserStore`): BrowserTab identity, selected-tab behavior, close rules, and UserDefaults persistence. Related files: Sources/Models.swift; Sources/Screens/TabsView.swift; Tests/BrowserCoreTests.swift.
3. **Embed a web page inside a SwiftUI screen** — `Sources/WebView.swift` (`struct WebView`): UIViewRepresentable/WebKit bridge, navigation state, and page loading. Related files: Sources/WebView.swift; Sources/Screens/BrowseView.swift.
4. **Content rules and private-mode clearing** — `Sources/Core.swift` (`trackerPatterns`): Rule-list JSON, rule compilation, blocked-count reporting, and private data behavior. Related files: Sources/Core.swift; Sources/Models.swift; Sources/Screens/SettingsView.swift; Tests/BrowserCoreTests.swift.
5. **Compose browse, tabs, and settings views** — `Sources/ContentView.swift` (`struct ContentView`): Observable store injection, navigation, toolbar actions, and settings binding. Related files: Sources/ContentView.swift; Sources/Screens/BrowseView.swift; Sources/Screens/SettingsView.swift.
6. **Test routing, tab lifecycle, and privacy claims** — `Tests/BrowserCoreTests.swift` (`func testThePrivateModeThrowsTheDataAway`): XCTest coverage, XcodeGen project configuration, and documentation boundary. Related files: Tests/BrowserCoreTests.swift; project.yml; README.md.

## Runtime boundaries

- Stack: Swift, SwiftUI, WebKit, XCTest, XcodeGen.
- Explicit limits across modules: ['The engine routing is a sample rule; it does not implement DuckDuckGo product services', 'Persisted URLs are ordinary browsing data and this sample has limited privacy guarantees', 'This is an educational WebKit wrapper, not a custom browser engine or hardened production browser', 'The sample rules are limited; a counter is not proof that every tracker was blocked', 'The views demonstrate a subset of a browser workflow and are not a production browser UX', 'No Xcode build was run in this workspace; simulator behavior remains unverified'].
- Source code is the implementation of record; compare each claim with project README and tests.
- Read each lesson’s directly quoted source excerpt and linked source path before changing behavior.
- No application is claimed to have been deployed or connected to production infrastructure.
