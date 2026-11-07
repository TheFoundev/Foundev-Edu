# App Development learning packages

Source-grounded, portable learning packages for the 11 copied mobile app projects in the sibling `../projects/` tree. Every lesson maps to current source files and includes a code excerpt, a practical exercise, ten student-facing MCQs, a separate explained answer key, and an assessed final project.

These packages describe learning implementations, not full upstream products. Read source-specific limitations before running apps. A passing structural validator checks references and package shape only; it does not prove educational correctness, application execution, API behavior, or deployment.

## Packages

- [`bluesky-social-app`](projects/bluesky-social-app/README.md)
- [`bluewallet`](projects/bluewallet/README.md)
- [`covid-alert`](projects/covid-alert/README.md)
- [`duckduckgo-for-ios`](projects/duckduckgo-for-ios/README.md)
- [`firefox-for-ios`](projects/firefox-for-ios/README.md)
- [`gitpoint`](projects/gitpoint/README.md)
- [`kickstarter-for-ios`](projects/kickstarter-for-ios/README.md)
- [`movieswiftui`](projects/movieswiftui/README.md)
- [`new-expensify`](projects/new-expensify/README.md)
- [`peyara-remote-mouse`](projects/peyara-remote-mouse/README.md)
- [`rocket-chat-mobile`](projects/rocket-chat-mobile/README.md)

## Validation and archives

Run `python tools/validate_content.py` from this directory. It writes human-readable reports under `reports/` and checks structural constraints. ZIPs are under `dist/`, each with its project slug as the archive root.
