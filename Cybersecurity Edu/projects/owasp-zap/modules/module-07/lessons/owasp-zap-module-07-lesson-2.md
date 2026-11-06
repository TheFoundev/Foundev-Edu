# Read passiveanalyzer and scanengine in the source

**Lesson ID:** `owasp-zap-module-07-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/main/java/local/foundev/zap/core/PassiveAnalyzer.java] and [src/main/java/local/foundev/zap/core/ScanEngine.java]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include class, analyze, class, int, getStore, cancel, run, pageCrawled, linkDiscovered, error; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/main/java/local/foundev/zap/core/PassiveAnalyzer.java`, `src/main/java/local/foundev/zap/core/ScanEngine.java`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/main/java/local/foundev/zap/core/PassiveAnalyzer.java`, `package local.foundev.zap.core;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/PassiveAnalyzer.java`, `import local.foundev.zap.model.Alert;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/PassiveAnalyzer.java`, `import local.foundev.zap.model.Confidence;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/PassiveAnalyzer.java`, `import local.foundev.zap.model.Risk;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/PassiveAnalyzer.java`, `import java.util.ArrayList;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class PassiveAnalyzer {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public List<Alert> analyze(FetchResult page) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/main/java/local/foundev/zap/core/ScanEngine.java`, `package local.foundev.zap.core;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/ScanEngine.java`, `import local.foundev.zap.model.Alert;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/ScanEngine.java`, `import local.foundev.zap.model.AlertStore;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/ScanEngine.java`, `import java.net.URI;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/ScanEngine.java`, `import java.util.List;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class ScanEngine {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public static final int DEFAULT_MAX_PAGES = 50;` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public AlertStore getStore() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public void cancel() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public ScanSummary run(URI target, boolean authorizedActive, int maxPages, ScanProgress progress) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public void pageCrawled(FetchResult page, int fetched, int queued) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/main/java/local/foundev/zap/core/PassiveAnalyzer.java

```text
package local.foundev.zap.core;

import local.foundev.zap.model.Alert;
import local.foundev.zap.model.Confidence;
import local.foundev.zap.model.Risk;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Passive checks: nothing is sent beyond the request that was already made to
 * fetch the page. Everything is inferred from the response as received.
 */
public final class PassiveAnalyzer {

    private static final Pattern INSECURE_RESOURCE =
            Pattern.compile("(?i)(?:src|href)\\s*=\\s*[\"']http://[^\"']+[\"']");

    public List<Alert> analyze(FetchResult page) {
        List<Alert> out = new ArrayList<>();
        String url = page.getUri().toString();
        String body = page.getBody();
        boolean https = "https".equalsIgnoreCase(page.getUri().getScheme());

        if (page.isHtml()) {
            if (isBlank(page.header("Content-Security-Policy"))) {
                out.add(new Alert(
                        "Content-Security-Policy header not set",
                        Risk.LOW,
                        Confidence.MEDIUM,
                        url,
                        "",
                        "",
                        "The response does not carry a Content-Security-Policy header, so the browser places no restriction on script origins, inline script or frame sources.",
                        "Define a Content-Security-Policy that whitelists the required script, style and frame origins; prefer nonces or hashes over 'unsafe-inline'."));
            }
            if (isBlank(page.header("X-Frame-Options")) && !hasFrameAncestors(page.header("Content-Security-Policy"))) {
                out.add(new Alert(
                        "X-Frame-Options header not set",
                        Risk.LOW,
                        Confidence.MEDIUM,
                        url,
                        "",
                        "",
                        "The page can be embedded in a frame on another origin, which enables clickjacking.",
                        "Set X-Frame-Options: DENY (or SAMEORIGIN), or declare frame-ancestors in the Content-Security-Policy header."));
            }
            if (isBlank(page.header("X-Content-Type-Options"))) {
                out.add(new Alert(
                        "X-Content-Type-Options header not set",
                        Risk.INFORMATIONAL,
                        Confidence.MEDIUM,
                        url,
                        "",
                        "",
                        "Without nosniff the browser may reinterpret a response as a different content type (MIME sniffing).",
                        "Set X-Content-Type-Options: nosniff on all responses."));
            }
        }

        if (https && isBlank(page.header("Strict-Transport-Security"))) {
            out.add(new Alert(
                    "Strict-Transport-Security header not set",
                    Risk.MEDIUM,
                    Confidence.MEDIUM,
                    url,
                    "",
                    "",
                    "The HTTPS response does not enable HSTS, so the first visit (or a downgrade) can be intercepted before the browser knows to force HTTPS.",
                    "Set Strict-Transport-Security: max-age=31536000; includeSubDomains on the HTTPS site."));
        }

        String server = page.header("Server");
        if (!isBlank(server)) {
            out.add(new Alert(
                    "Server banner disclosed",
                    Risk.INFORMATIONAL,
                    Confidence.HIGH,
                    url,
                    "",
                    server,
                    "The Server header discloses the web server product and version, which helps an attacker match it against known vulnerabilities.",
                    "Suppress or genericise the Server header; do not advertise exact software versions."));
        }

     
```

### src/main/java/local/foundev/zap/core/ScanEngine.java

```text
package local.foundev.zap.core;

import local.foundev.zap.model.Alert;
import local.foundev.zap.model.AlertStore;

import java.net.URI;
import java.util.List;

/**
 * Orchestrates one run: crawl the target, run the passive analyzer on every
 * page as it arrives, then - only when authorization was explicitly confirmed
 * - run the active probes. All alerts land in the shared {@link AlertStore}.
 */
public final class ScanEngine {

    public static final int DEFAULT_MAX_PAGES = 50;

    private final AlertStore store;
    private final HttpFetcher fetcher;

    private volatile WebCrawler crawler;
    private volatile boolean cancelled;

    public ScanEngine(AlertStore store) {
        this.store = store;
        this.fetcher = new HttpFetcher();
    }

    public AlertStore getStore() {
        return store;
    }

    /** Cancels a run in progress: the crawl loop exits, active probes stop. */
    public void cancel() {
        cancelled = true;
        WebCrawler c = crawler;
        if (c != null) {
            c.stop();
        }
    }

    public ScanSummary run(URI target, boolean authorizedActive, int maxPages, ScanProgress progress) {
        ScanProgress p = [REDACTED] == null ? ScanProgress.NONE : progress;
        cancelled = false;
        store.clear();
        long started = System.currentTimeMillis();

        PassiveAnalyzer passive = new PassiveAnalyzer();
        WebCrawler crawl = new WebCrawler(fetcher);
        crawler = crawl;

        int crawled = 0;
        boolean stoppedEarly = false;
        boolean activeRan = false;
        try {
            CrawlResult result = crawl.crawl(target, maxPages, new CrawlListener() {
                @Override
                public void pageCrawled(FetchResult page, int fetched, int queued) {
                    store.addAll(passive.analyze(page));
                    p.onStatus("Crawled " + page.getUri() + " (" + fetched + " pages, " + queued + " queued)");
                }

                @Override
                public void linkDiscovered(String url, String parentUrl) {
                    p.onLink(url, parentUrl);
                }

                @Override
                public void error(String url, String message) {
                    p.onStatus("Skipped " + url + ": " + message);
                }
            });
            crawled = result.getPages().size();
            stoppedEarly = result.isStopped() || cancelled;

            // Active checks are refused unless the caller passed the gate.
            if (authorizedActive && !cancelled && !result.getPages().isEmpty()) {
                ActiveAnalyzer active = new ActiveAnalyzer(fetcher);
                List<Alert> found = active.analyze(target, result.getPages(), true, () -> cancelled, p);
                store.addAll(found);
                activeRan = true;
            }
        } finally {
            crawler = null;
        }

        ScanSummary summary = new ScanSummary(
                target,
                crawled,
                store.size(),
                activeRan,
                stoppedEarly,
                System.currentTimeMillis() - started);
        p.onFinished(summary);
        return summary;
    }
}

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

This lesson ties its explanation to `src/main/java/local/foundev/zap/core/PassiveAnalyzer.java`, `src/main/java/local/foundev/zap/core/ScanEngine.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
