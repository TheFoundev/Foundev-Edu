# Architecture — MovieSwiftUI

Build a SwiftUI movie-discovery mini app with catalogue mapping, search, genre selection, sorting, detail pages, and a persistent watchlist.

## Data and behavior map

1. **A movie record and a useful catalogue** — `Sources/Models.swift` (`struct Movie`): Movie fields, identity, MovieInfo projection, and seed records. Related files: Sources/Models.swift; Sources/Core.swift.
2. **Convert untrusted response data into movie records** — `Sources/Core.swift` (`func movie`): Response decoding/mapping and missing-field rejection. Related files: Sources/Core.swift; Tests/MovieCoreTests.swift.
3. **Narrow and order the catalogue** — `Sources/Core.swift` (`func search`): Text search fields, genre filtering, rating/year ordering, and UI controls. Related files: Sources/Core.swift; Sources/Screens/SearchView.swift; Sources/Screens/DiscoverView.swift.
4. **Remember a watchlist without a service account** — `Sources/Models.swift` (`final class MovieStore`): Store defaults, add/remove operations, and UserDefaults reload. Related files: Sources/Models.swift; Sources/Screens/WatchlistView.swift; Tests/MovieCoreTests.swift.
5. **Compose discovery, detail, and reusable poster views** — `Sources/Components.swift` (`struct MoviePoster`): Navigation, card poster rendering, shared store, and detail fields. Related files: Sources/ContentView.swift; Sources/Components.swift; Sources/Screens/MovieDetailView.swift; Sources/Screens/DiscoverView.swift.
6. **Read test evidence and plan runtime checks** — `Tests/MovieCoreTests.swift` (`final class MovieCoreTests`): Mapping/filter tests, watchlist persistence tests, XcodeGen targets, and simulator review. Related files: Tests/MovieCoreTests.swift; project.yml; README.md.

## Runtime boundaries

- Stack: Swift, SwiftUI, UserDefaults, XCTest, XcodeGen.
- Explicit limits across modules: ['The displayed catalogue is seeded sample data; live movie-service access is not configured', 'No API credentials or live server call are present in the sample app', 'Results only cover the in-memory catalogue available to the store', 'Local watchlist persistence does not create an account or sync across devices', 'Poster URLs/assets may be absent; do not imply a live streaming/catalogue integration', 'No Xcode or simulator execution was available in this build environment'].
- Source code is the implementation of record; compare each claim with project README and tests.
- Read each lesson’s directly quoted source excerpt and linked source path before changing behavior.
- No application is claimed to have been deployed or connected to production infrastructure.
