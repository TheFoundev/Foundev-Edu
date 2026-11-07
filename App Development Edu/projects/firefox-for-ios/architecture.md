# Architecture — Firefox for iOS

Build a SwiftUI/WebKit browser-shell mini app with URL/search handling, tab state, protection settings, and rule-based tracking controls.

## Data and behavior map

1. **Browser records and protection state** — `Sources/Models.swift` (`struct BrowserTab`): Tab, protection-level, and tracker data types. Related files: Sources/Models.swift; Sources/Core.swift.
2. **Turn an address-bar string into a destination** — `Sources/Core.swift` (`func destination`): URL recognition, scheme normalization, and search fallback. Related files: Sources/Core.swift; Tests/BrowserCoreTests.swift.
3. **Render navigation through WebKit** — `Sources/WebView.swift` (`struct WebView`): Representable wrapper, load calls, and browser controls. Related files: Sources/WebView.swift; Sources/Screens/BrowserScreen.swift.
4. **Map a settings choice to tracker rules** — `Sources/Core.swift` (`standardTrackers`): Protection modes, rule selection, rule compilation, and observed count. Related files: Sources/Core.swift; Sources/Models.swift; Sources/Screens/SettingsView.swift.
5. **Share browser state across screens** — `Sources/ContentView.swift` (`struct ContentView`): Observable store lifecycle, tab navigation, and settings binding. Related files: Sources/ContentView.swift; Sources/Screens/TabsView.swift; Sources/Screens/HomeView.swift; Sources/Screens/SettingsView.swift.
6. **Read the test suite and XcodeGen spec** — `Tests/BrowserCoreTests.swift` (`final class BrowserCoreTests`): XCTest assertions, target configuration, and what a test does not establish. Related files: Tests/BrowserCoreTests.swift; project.yml; README.md.

## Runtime boundaries

- Stack: Swift, SwiftUI, WebKit, XCTest, XcodeGen.
- Explicit limits across modules: ['The sample model is not the complete Firefox account/profile model', 'Search and navigation behavior is a teaching implementation and may omit edge cases of the full Firefox browser', 'The project does not embed Firefox’s Gecko engine', 'Rules are a small sample, not Firefox’s full tracking-protection lists or guarantees', 'Account sync, history sync, and production data management are not implemented', 'The source was not built or deployed here; no runtime result is implied'].
- Source code is the implementation of record; compare each claim with project README and tests.
- Read each lesson’s directly quoted source excerpt and linked source path before changing behavior.
- No application is claimed to have been deployed or connected to production infrastructure.
