# A beginner's model of documented goals mapped to implementation

**Lesson ID:** `owasp-zap-module-15-lesson-1`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors src/main/java/local/foundev/zap/ScannerApp.java, src/main/java/local/foundev/zap/ScannerCli.java, src/main/java/local/foundev/zap/core/ActiveAnalyzer.java. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `README.md`, `src/main/java/local/foundev/zap/ScannerApp.java`, `src/main/java/local/foundev/zap/ScannerCli.java`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/main/java/local/foundev/zap/ScannerApp.java`, `package local.foundev.zap;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ScannerApp.java`, `import local.foundev.zap.ui.ScannerFrame;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ScannerApp.java`, `import javax.swing.SwingUtilities;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ScannerApp.java`, `import javax.swing.UIManager;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class ScannerApp {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public static void main(String[] args) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/main/java/local/foundev/zap/ScannerCli.java`, `package local.foundev.zap;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ScannerCli.java`, `import local.foundev.zap.core.ScanEngine;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ScannerCli.java`, `import local.foundev.zap.core.ScanProgress;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ScannerCli.java`, `import local.foundev.zap.core.ScanSummary;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ScannerCli.java`, `import local.foundev.zap.model.Alert;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class ScannerCli {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public static void main(String[] args) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public void onStatus(String message) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public void onLink(String url, String parentUrl) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public void onFinished(ScanSummary summary) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### README.md

```text
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
- Headless CLI for scripted assessments

## Stack

`JUnit; Java`
The CSV stack is JUnit + Java. The project is built with Maven and a JDK 17: `mvn test` compiles the scanner core, the Swing UI, the CLI and the tests, and runs the 26 tests of the suite.

## Authorized use only

Active checks send deliberately malformed requests (script tags, SQL quotes, traversal paths). Run them only against systems you own or have explicit, written permission to test — the UI checkbox and the CLI `--authorized` flag are that confirmation, and they are required. Pointing a scanner at third-party systems without permission may be a crime; treat every alert as a hint to verify manually, never as permission to exploit.

## Run

```bash
mvn package                # needs a JDK; see the environment note below

java -jar target/owasp-zap-0.1.0.jar                                  # Swing UI
java -jar target/owasp-zap-0.1.0.jar cli http://localhost:8080/       # headless run

# headless with active probes (the explicit authorization flag is mandatory):
java -jar target/owasp-zap-0.1.0.jar cli http://localhost:3000/ \
     --active --authorized --html report.html --json report.json
```

CLI options: `--active`, `--authorized`, `--max-pages <n>`, `--html <file>`, `--json <file>`, `--help`.

## Structure

```text
owasp-zap/
├── pom.xml                        Maven project (jar, JUnit 5 only)
├── src/main/java/local/foundev/zap/
│   ├── ScannerApp.java            Swing entry point (dispatches to the CLI with "cli")
│   ├── ScannerCli.java            headless entry point
│   ├── core/                      HttpFetcher, spider, passive/active analyzers, scan engine
│   ├── model/                     Alert, Risk/Confidence enums, AlertStore
│   ├── report/                    HTML and JSON report writers
│   └── ui/                        Swing frame and alerts table model
├── src/test/java/                 PassiveAnalyzerTest, ReportExportTest,
│                                  CookieAnalysisTest, AlertStoreTest, WebCrawlerTest
├── LICENSE
└── README.md
```

## Testing

```bash
mvn test                          # 26 tests; needs a JDK 17 and Maven
```

The suite covers the passive checks, the report writers, the cookie analysis
(the attributes are what follow the first `;`, so a value that looks like a
flag is not mistaken for one), the alert store (the de-duplication, the
filtering by risk, the c
```

### src/main/java/local/foundev/zap/ScannerApp.java

```text
package local.foundev.zap;

import local.foundev.zap.ui.ScannerFrame;

import javax.swing.SwingUtilities;
import javax.swing.UIManager;

/**
 * Application entry point: launches the Swing UI with no arguments, and the
 * headless CLI when given "cli", any option, or a target URL
 * (so {@code java -jar owasp-zap.jar cli http://localhost:8080/} works).
 */
public final class ScannerApp {

    private ScannerApp() {
    }

    public static void main(String[] args) {
        if (args.length > 0 && isCliInvocation(args[0])) {
            String[] rest = args;
            if ("cli".equals(args[0]) || "--cli".equals(args[0])) {
                rest = new String[args.length - 1];
                System.arraycopy(args, 1, rest, 0, rest.length);
            }
            ScannerCli.main(rest);
            return;
        }
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception ignored) {
            // Keep the platform default look and feel.
        }
        SwingUtilities.invokeLater(() -> {
            ScannerFrame frame = new ScannerFrame();
            frame.setVisible(true);
        });
    }

    private static boolean isCliInvocation(String first) {
        return "cli".equals(first) || "--cli".equals(first)
                || first.startsWith("-")
                || first.startsWith("http://")
                || first.startsWith("https://");
    }
}

```

### src/main/java/local/foundev/zap/ScannerCli.java

```text
package local.foundev.zap;

import local.foundev.zap.core.ScanEngine;
import local.foundev.zap.core.ScanProgress;
import local.foundev.zap.core.ScanSummary;
import local.foundev.zap.model.Alert;
import local.foundev.zap.model.AlertStore;
import local.foundev.zap.report.HtmlReportWriter;
import local.foundev.zap.report.JsonReportWriter;

import java.io.IOException;
import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * Headless entry point: crawl, passive checks, optional authorized active
 * checks, then print the alerts and optionally export the reports.
 */
public final class ScannerCli {

    private ScannerCli() {
    }

    public static void main(String[] args) {
        System.exit(run(args));
    }

    private static int run(String[] args) {
        String url = null;
        boolean active = false;
        boolean authorized = false;
        int maxPages = ScanEngine.DEFAULT_MAX_PAGES;
        Path htmlOut = null;
        Path jsonOut = null;

        for (int i = 0; i < args.length; i++) {
            String arg = args[i];
            switch (arg) {
                case "--help":
                case "-h":
                    printUsage();
                    return 0;
                case "--active":
                    active = true;
                    break;
                case "--authorized":
                    authorized = true;
                    break;
                case "--max-pages":
                    if (i + 1 >= args.length) {
                        System.err.println("--max-pages needs a value.");
                        return 2;
                    }
                    try {
                        maxPages = Integer.parseInt(args[++i]);
                    } catch (NumberFormatException e) {
                        System.err.println("Invalid --max-pages value: " + args[i]);
                        return 2;
                    }
                    break;
                case "--html":
                    if (i + 1 >= args.length) {
                        System.err.println("--html needs a file path.");
                        return 2;
                    }
                    htmlOut = Path.of(args[++i]);
                    break;
                case "--json":
                    if (i + 1 >= args.length) {
                        System.err.println("--json needs a file path.");
                        return 2;
                    }
                    jsonOut = Path.of(args[++i]);
                    break;
                default:
                    if (arg.startsWith("--")) {
                        System.err.println("Unknown option: " + arg);
                        printUsage();
                        return 2;
                    }
                    if (url != null) {
                        System.err.println("Only one target URL may be given.");
                        return 2;
                    }
                    url = arg;
            }
        }

        if (url == null) {
            printUsage();
            return 2;
        }
        if (active && !authorized) {
            System.err.println("Active checks refused: pass --authorized to confirm you are "
                    + "permitted to actively test this target.");
```

The excerpt comes from this project’s source tree and may omit context. It is not evidence that the source was executed. Never treat a listed function name alone as proof that a user-facing path reaches it.

## Expected behavior and known limits

Only behavior visible in the cited implementation or assertions can be explained as implemented. External calls, deployment settings, successful installation, performance, and test outcomes remain unverified here.

## Practical exercise

Use the module exercise to create a call/data/configuration trace for these exact files. Include a source location for every claim.

## Common mistakes and debugging

- Reading only function names: follow bodies, callers, and return paths.
- Assuming imports prove an integration ran: inspect the call site and configuration.
- Assuming tests pass because they exist: record execution separately.
- If the path is unclear, search all references to the symbol and trace from the actual entry point.

## Best practices and security

Use synthetic fixtures and isolated environments. Redact credentials and personal data. Review validation at input boundaries, dependency declarations, and error handling before suggesting a change. These security projects are dual-use: scan, intercept, phish, or operate honeypots only on systems you own or have explicit authorization to test. Keep intentionally vulnerable apps and security labs isolated, and use synthetic targets and credentials.

## Summary

This lesson ties its explanation to `README.md`, `src/main/java/local/foundev/zap/ScannerApp.java`, `src/main/java/local/foundev/zap/ScannerCli.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
