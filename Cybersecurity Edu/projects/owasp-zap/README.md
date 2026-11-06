# Owasp Zap

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# OWASP ZAP

A web application security scanner offering passive and active testing for authorised assessments.

> A ZAP-style scanner that spiders a target you supply, checks every response for security weaknesses, sends active probes only after an explicit authorization confirmation, and exports the alerts as HTML or JSON.

## Overview

An original, self-contained implementation of the **OWASP ZAP** concept for the Foundev portfolio. It focuses on the core workflow from the project brief — spider, passive analysis, authorized active checks, alert report — and keeps the architecture small enough to read end to end.

## Features

- Same-origin, breadth-first HTTP spider that discovers `href`/`src` links and GET form targets
- Passive analyzer: missing Content-Security-Policy / X-Frame-Options / X-Content-Type-Options / HSTS, cookie flags (Secure, HttpOnly, SameSite), `Server` and `X-Powered-By` banner disclosure, directory listing, mixed content
- Active analyzer behind a hard gate: reflected XSS, error-based SQL injection and path-traversal probes on query parameters — disabled unless the "I am authorized" checkbox (UI) or the `--authorized` flag (CLI) is given; the analyzer itself refuses to run without that confirmation
- Alert model with risk level, confidence, URL, parameter, evidence, description and remediation, plus an in-memory store that de-duplicates findings and filters by risk
- Swing UI: target URL bar, authorization checkbox, crawl progress bar, discovered-site tree, color-coded alerts table, risk filter
- Export of the alert report as HTML and JSON
- Headles

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Same-origin, breadth-first HTTP spider that discovers `href`/`src` links and GET form targets
- Passive analyzer: missing Content-Security-Policy / X-Frame-Options / X-Content-Type-Options / HSTS, cookie flags (Secure, HttpOnly, SameSite), `Server` and `X-Powered-By` banner disclosure, directory listing, mixed content
- Active analyzer behind a hard gate: reflected XSS, error-based SQL injection and path-traversal probes on query parameters — disabled unless the "I am authorized" checkbox (UI) or the `--authorized` flag (CLI) is given; the analyzer itself refuses to run without that confirmation
- Alert model with risk level, confidence, URL, parameter, evidence, description and remediation, plus an in-memory store that de-duplicates findings and filters by risk
- Swing UI: target URL bar, authorization checkbox, crawl progress bar, discovered-site tree, color-coded alerts table, risk filter
- Export of the alert report as HTML and JSON
- Headless CLI for scripted assessments
- **Build:** the project is written for plain Java 17 and is built with Maven. `mvn test` compiles everything (the scanner core, the Swing UI, the CLI) and runs the 26 tests of the suite; the CI workflow does the same on every push.
- The spider is GET-only and same-origin, capped at 50 pages by default; response bodies are truncated to 512 KB for analysis, and JavaScript is never executed (no headless browser), so single-page applications are only partially covered.
- Active checks are three conservative probes (one XSS marker, one SQL quote checked against common error strings, one traversal payload); their alerts are evidence hints with medium confidence, not proof.
- The cookie analysis follows RFC 6265: the name/value pair ends at the first `;` and only what follows it is read as attributes, so a value that looks like a flag is not mistaken for one.

The implementation inventory includes 38 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `the repository dependency/configuration files`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `pom.xml`
- `src/main/java/local/foundev/zap/ScannerApp.java`
- `src/main/java/local/foundev/zap/ScannerCli.java`
- `src/main/java/local/foundev/zap/core/ActiveAnalyzer.java`
- `src/main/java/local/foundev/zap/core/CrawlListener.java`
- `src/main/java/local/foundev/zap/core/CrawlResult.java`
- `src/main/java/local/foundev/zap/core/FetchException.java`
- `src/main/java/local/foundev/zap/core/FetchResult.java`
- `src/main/java/local/foundev/zap/core/HttpFetcher.java`
- `src/main/java/local/foundev/zap/core/PassiveAnalyzer.java`
- `src/main/java/local/foundev/zap/core/ScanEngine.java`
- `src/main/java/local/foundev/zap/core/ScanProgress.java`
- `src/main/java/local/foundev/zap/core/ScanSummary.java`
- `src/main/java/local/foundev/zap/core/Uris.java`
- `src/main/java/local/foundev/zap/core/WebCrawler.java`
- `src/main/java/local/foundev/zap/model/Alert.java`
- `src/main/java/local/foundev/zap/model/AlertStore.java`
- `src/main/java/local/foundev/zap/model/Confidence.java`
- `src/main/java/local/foundev/zap/model/Risk.java`
- `src/main/java/local/foundev/zap/report/HtmlReportWriter.java`
- `src/main/java/local/foundev/zap/report/JsonReportWriter.java`
- `src/main/java/local/foundev/zap/report/ReportSupport.java`
- `src/main/java/local/foundev/zap/ui/AlertTableModel.java`
- `src/main/java/local/foundev/zap/ui/ScannerFrame.java`
- `src/test/java/local/foundev/zap/AlertStoreTest.java`
- `src/test/java/local/foundev/zap/CookieAnalysisTest.java`
- `src/test/java/local/foundev/zap/PassiveAnalyzerTest.java`
- `src/test/java/local/foundev/zap/ReportExportTest.java`
- `src/test/java/local/foundev/zap/WebCrawlerTest.java`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: src/test/java/local/foundev/zap/AlertStoreTest.java, src/test/java/local/foundev/zap/CookieAnalysisTest.java, src/test/java/local/foundev/zap/PassiveAnalyzerTest.java, src/test/java/local/foundev/zap/ReportExportTest.java, src/test/java/local/foundev/zap/WebCrawlerTest.java. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
