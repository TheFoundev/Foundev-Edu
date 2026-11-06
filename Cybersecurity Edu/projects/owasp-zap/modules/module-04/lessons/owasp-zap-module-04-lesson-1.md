# A beginner's model of activeanalyzer and crawllistener

**Lesson ID:** `owasp-zap-module-04-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/main/java/local/foundev/zap/core/ActiveAnalyzer.java] and [src/main/java/local/foundev/zap/core/CrawlListener.java]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include class, analyze, CrawlListener, pageCrawled, linkDiscovered, error; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/main/java/local/foundev/zap/core/ActiveAnalyzer.java`, `src/main/java/local/foundev/zap/core/CrawlListener.java`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/main/java/local/foundev/zap/core/ActiveAnalyzer.java`, `package local.foundev.zap.core;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/ActiveAnalyzer.java`, `import local.foundev.zap.model.Alert;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/ActiveAnalyzer.java`, `import local.foundev.zap.model.Confidence;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/ActiveAnalyzer.java`, `import local.foundev.zap.model.Risk;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/ActiveAnalyzer.java`, `import java.net.URI;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class ActiveAnalyzer {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public List<Alert> analyze(URI target, List<FetchResult> pages, boolean authorized,` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/main/java/local/foundev/zap/core/CrawlListener.java`, `package local.foundev.zap.core;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public interface CrawlListener {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public void pageCrawled(FetchResult page, int fetched, int queued) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public void linkDiscovered(String url, String parentUrl) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public void error(String url, String message) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/main/java/local/foundev/zap/core/ActiveAnalyzer.java

```text
package local.foundev.zap.core;

import local.foundev.zap.model.Alert;
import local.foundev.zap.model.Confidence;
import local.foundev.zap.model.Risk;

import java.net.URI;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Locale;
import java.util.Set;
import java.util.function.BooleanSupplier;

/**
 * Active checks, deliberately few and safe. Every probe is a single GET that
 * appends one marker payload to one query parameter of a URL the spider
 * already visited; no request is ever sent unless the caller explicitly
 * confirms authorization for the target.
 */
public final class ActiveAnalyzer {

    /** Cap on parameter/probe combinations so a scan stays polite. */
    private static final int MAX_PARAMS = 20;

    static final String XSS_PAYLOAD = "<script>window.__foundev_zap_marker__=1</script>";
    static final String SQLI_PAYLOAD = "'";
    static final String TRAVERSAL_PAYLOAD = "../../../../etc/passwd";

    private static final String[] SQL_ERROR_MARKERS = {
            "you have an error in your sql syntax",
            "warning: mysql",
            "mysqli",
            "sqlstate[",
            "unclosed quotation mark",
            "unterminated quoted string",
            "ora-00933",
            "ora-01756",
            "postgresql",
            "pg_query",
            "sqlite.exception",
            "odbc sql server driver",
            "microsoft odbc"
    };

    private final HttpFetcher fetcher;

    public ActiveAnalyzer(HttpFetcher fetcher) {
        this.fetcher = fetcher;
    }

    /**
     * Runs the probes against query parameters of already-crawled pages.
     *
     * @throws IllegalStateException when authorization was not confirmed
     */
    public List<Alert> analyze(URI target, List<FetchResult> pages, boolean authorized,
                               BooleanSupplier cancelled, ScanProgress progress) {
        if (!authorized) {
            throw new IllegalStateException("Active scanning requires explicit authorization for the target");
        }
        List<Alert> out = new ArrayList<>();
        if (pages == null || pages.isEmpty()) {
            return out;
        }
        ScanProgress p = [REDACTED] == null ? ScanProgress.NONE : progress;

        for (String[] pair : collectParams(pages)) {
            if (cancelled != null && cancelled.getAsBoolean()) {
                break;
            }
            URI base;
            try {
                base = URI.create(pair[0]);
            } catch (IllegalArgumentException e) {
                continue;
            }
            if (!Uris.sameOrigin(target, base)) {
                continue;
            }
            String param = pair[1];
            p.onStatus("Active probe: " + pair[0] + " [" + param + "]");
            probeReflectedXss(base, param, out);
            probeSqlInjection(base, param, out);
            probePathTraversal(base, param, out);
        }
        return out;
    }

    private void probeReflectedXss(URI base, String param, List<Alert> out) {
        FetchResult response = get(base, param, XSS_PAYLOAD);
        if (response == null) {
            return;
        }
        String body = response.getBody();
        int idx = body.indexOf(XSS_PAYLOAD);
        if (idx < 0) {
            return;
```

### src/main/java/local/foundev/zap/core/CrawlListener.java

```text
package local.foundev.zap.core;

/** Callbacks fired while the spider walks a site. */
public interface CrawlListener {

    /** One page was fetched successfully. */
    void pageCrawled(FetchResult page, int fetched, int queued);

    /** A link was found inside a page and queued for the crawl. */
    void linkDiscovered(String url, String parentUrl);

    /** A URL could not be fetched and was skipped. */
    void error(String url, String message);

    CrawlListener NONE = new CrawlListener() {
        @Override
        public void pageCrawled(FetchResult page, int fetched, int queued) {
        }

        @Override
        public void linkDiscovered(String url, String parentUrl) {
        }

        @Override
        public void error(String url, String message) {
        }
    };
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

This lesson ties its explanation to `src/main/java/local/foundev/zap/core/ActiveAnalyzer.java`, `src/main/java/local/foundev/zap/core/CrawlListener.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
