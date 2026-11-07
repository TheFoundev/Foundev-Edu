# Remember a watchlist without a service account

**Lesson ID:** `movieswiftui-04-watchlist-persistence-lesson-01`  
**Project:** MovieSwiftUI  
**Source focus:** `Sources/Models.swift` — `final class MovieStore`

## Purpose and learning objectives

In plain terms, this lesson teaches **A watchlist is a saved set of identifiers. Follow a toggle from button through the store to UserDefaults and verify persistence using the tests**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `Sources/Models.swift` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: Local watchlist persistence does not create an account or sync across devices.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: A watchlist is a saved set of identifiers. Follow a toggle from button through the store to UserDefaults and verify persistence using the tests. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Store defaults, add/remove operations, and UserDefaults reload**. This is a learning implementation, so keep the limit in view: Local watchlist persistence does not create an account or sync across devices.

## Learning objectives

1. Describe the everyday behavior: A watchlist is a saved set of identifiers. Follow a toggle from button through the store to UserDefaults and verify persistence using the tests.
2. Find the relevant implementation in `Sources/Models.swift` and explain the named symbol.
3. Trace the responsibility across the related files: `Sources/Models.swift`, `Sources/Screens/WatchlistView.swift`, `Tests/MovieCoreTests.swift`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: A watchlist is a saved set of identifiers. Follow a toggle from button through the store to UserDefaults and verify persistence using the tests. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Store defaults, add/remove operations, and UserDefaults reload**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: Local watchlist persistence does not create an account or sync across devices.

### 3. Read the real implementation

The excerpt below is copied directly from `Sources/Models.swift` around `final class MovieStore`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```swift
final class MovieStore: ObservableObject {
    private static let watchlistKey = "movies.watchlist"

    @Published var watchlist: Set<Int>
    @Published var query = ""
    @Published var movies: [Movie]

    private let defaults: UserDefaults

    init(defaults: UserDefaults = .standard) {
        self.defaults = defaults
        self.movies = sampleMovies
        self.watchlist = Set(defaults.array(forKey: Self.watchlistKey) as? [Int] ?? [])
    }

    /// The films that match the search and the genre.
    var filtered: [Movie] {
        let ids = MovieCore.search(movies.map(\.info), query: query).map(\.id)
```



The selected symbol is `final class MovieStore`. Relate its code to this source map:

- `Sources/Models.swift` — inspect how this part participates in store defaults, add/remove operations, and userdefaults reload.
- `Sources/Screens/WatchlistView.swift` — inspect how this part participates in store defaults, add/remove operations, and userdefaults reload.
- `Tests/MovieCoreTests.swift` — inspect how this part participates in store defaults, add/remove operations, and userdefaults reload.

### 4. Step-by-step source reading

1. Open `Sources/Models.swift` and search for `final class MovieStore`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: A watchlist is a saved set of identifiers. Follow a toggle from button through the store to UserDefaults and verify persistence using the tests. The known limitation is explicit: Local watchlist persistence does not create an account or sync across devices. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `movieswiftui-04-watchlist-persistence-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `Sources/Models.swift`; UI labels alone do not define behavior.
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

You started from the user task, named its everyday model, followed `final class MovieStore` in `Sources/Models.swift`, and traced the related files. The implemented behavior is **A watchlist is a saved set of identifiers. Follow a toggle from button through the store to UserDefaults and verify persistence using the tests**; the boundary is **Local watchlist persistence does not create an account or sync across devices**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`Sources/Models.swift`](../../../../../../projects/movieswiftui/Sources/Models.swift)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [Swiftui](https://developer.apple.com/documentation/swiftui/), [Xcodegen](https://github.com/yonaskolb/XcodeGen), [Xctest](https://developer.apple.com/documentation/xctest), [Owasp Mobile](https://mas.owasp.org/MASVS/)
