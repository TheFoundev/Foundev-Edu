# Architecture — Kickstarter for iOS

Build a SwiftUI crowdfunding discovery demo with local project search, detail views, save/back workflows, validation, and local state persistence.

## Data and behavior map

1. **A project card starts with a project record** — `Sources/Models.swift` (`struct Project`): Project fields, computed progress, identity, and sample catalogue. Related files: Sources/Models.swift; Sources/Components.swift.
2. **Find projects in a local catalogue** — `Sources/Core.swift` (`func search`): Category data, search matching, sort ordering, and discovery rendering. Related files: Sources/Core.swift; Sources/Screens/DiscoverView.swift; Tests/ProjectCoreTests.swift.
3. **Validate a pledge without moving money** — `Sources/Core.swift` (`checkPledge`): Pledge validation, status changes, detail state, and progress display. Related files: Sources/Core.swift; Sources/Screens/ProjectDetailView.swift; Tests/ProjectCoreTests.swift.
4. **Save choices and persist local identifiers** — `Sources/Models.swift` (`final class ProjectStore`): ProjectStore, UserDefaults keys, toggling, and backed/saved projections. Related files: Sources/Models.swift; Sources/Screens/SavedView.swift; Sources/Screens/ProfileView.swift.
5. **Build a screen flow around one observable store** — `Sources/ContentView.swift` (`struct ContentView`): Environment object injection, NavigationStack, and view actions. Related files: Sources/ContentView.swift; Sources/Components.swift; Sources/Screens/DiscoverView.swift; Sources/Screens/SavedView.swift; Sources/Screens/ProjectDetailView.swift; Sources/Screens/ProfileView.swift.
6. **Use XCTest and XcodeGen to check the sample** — `Tests/ProjectCoreTests.swift` (`final class ProjectCoreTests`): Core rule tests, temporary UserDefaults, target generation, and simulator checklist. Related files: Tests/ProjectCoreTests.swift; project.yml; README.md.

## Runtime boundaries

- Stack: Swift, SwiftUI, UserDefaults, XCTest, XcodeGen.
- Explicit limits across modules: ['The catalogue is sample content and does not come from Kickstarter', 'Search is local and only covers the included sample records', 'No charge, payment authorization, or server-side pledge is performed', 'Saved/backed IDs persist locally; changing pledge totals is sample in-memory state and does not sync', 'The source is a compact educational client, not production Kickstarter UI', 'This workspace lacked Xcode; build and UI behavior remain unverified'].
- Source code is the implementation of record; compare each claim with project README and tests.
- Read each lesson’s directly quoted source excerpt and linked source path before changing behavior.
- No application is claimed to have been deployed or connected to production infrastructure.
