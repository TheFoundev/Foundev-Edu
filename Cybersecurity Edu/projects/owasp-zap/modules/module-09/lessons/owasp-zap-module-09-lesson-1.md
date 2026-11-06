# A beginner's model of uris and webcrawler

**Lesson ID:** `owasp-zap-module-09-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/main/java/local/foundev/zap/core/Uris.java] and [src/main/java/local/foundev/zap/core/WebCrawler.java]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include class, stripFragment, sameOrigin, portOf, class, stop, crawl; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/main/java/local/foundev/zap/core/Uris.java`, `src/main/java/local/foundev/zap/core/WebCrawler.java`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/main/java/local/foundev/zap/core/Uris.java`, `package local.foundev.zap.core;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/Uris.java`, `import java.net.URI;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class Uris {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public static String stripFragment(String url) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public static boolean sameOrigin(URI a, URI b) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public static int portOf(URI uri) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/main/java/local/foundev/zap/core/WebCrawler.java`, `package local.foundev.zap.core;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/WebCrawler.java`, `import java.net.URI;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/WebCrawler.java`, `import java.util.ArrayDeque;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/WebCrawler.java`, `import java.util.ArrayList;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/WebCrawler.java`, `import java.util.Deque;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class WebCrawler {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public void stop() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public CrawlResult crawl(URI start, int maxPages, CrawlListener listener) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/main/java/local/foundev/zap/core/Uris.java

```text
package local.foundev.zap.core;

import java.net.URI;

/** Small URI helpers shared by the spider and the active checks. */
public final class Uris {

    private Uris() {
    }

    /** Removes the fragment part of a URL; fragments never change a request. */
    public static String stripFragment(String url) {
        if (url == null) {
            return "";
        }
        int hash = url.indexOf('#');
        return hash >= 0 ? url.substring(0, hash) : url;
    }

    /** True when both URIs share scheme, host and effective port over http(s). */
    public static boolean sameOrigin(URI a, URI b) {
        if (a == null || b == null) {
            return false;
        }
        String schemeA = a.getScheme();
        String schemeB = b.getScheme();
        if (schemeA == null || schemeB == null || !schemeA.equalsIgnoreCase(schemeB)) {
            return false;
        }
        if (!"http".equalsIgnoreCase(schemeA) && !"https".equalsIgnoreCase(schemeA)) {
            return false;
        }
        String hostA = a.getHost();
        String hostB = b.getHost();
        if (hostA == null || hostB == null || !hostA.equalsIgnoreCase(hostB)) {
            return false;
        }
        return portOf(a) == portOf(b);
    }

    /** The explicit port, or the scheme default (80/443). */
    public static int portOf(URI uri) {
        int port = uri.getPort();
        if (port != -1) {
            return port;
        }
        String scheme = uri.getScheme();
        if (scheme == null) {
            return -1;
        }
        if ("http".equalsIgnoreCase(scheme)) {
            return 80;
        }
        if ("https".equalsIgnoreCase(scheme)) {
            return 443;
        }
        return -1;
    }
}

```

### src/main/java/local/foundev/zap/core/WebCrawler.java

```text
package local.foundev.zap.core;

import java.net.URI;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Same-origin, breadth-first HTTP spider. It discovers href/src links and
 * enqueues GET form targets (named inputs appended as empty query values).
 * Every request it makes is a plain GET.
 */
public final class WebCrawler {

    // The fragment is part of the value: it is stripped when the link is
    // resolved, so a link with a fragment is followed like any other one.
    private static final Pattern LINK =
            Pattern.compile("(?i)(?:href|src)\\s*=\\s*[\"']([^\"']+)[\"']");
    private static final Pattern FORM_BLOCK =
            Pattern.compile("(?is)<form\\b([^>]*)>(.*?)</form>");
    private static final Pattern FORM_ACTION =
            Pattern.compile("(?i)action\\s*=\\s*[\"']([^\"']*)[\"']");
    private static final Pattern FORM_METHOD =
            Pattern.compile("(?i)method\\s*=\\s*[\"']([^\"']*)[\"']");
    private static final Pattern INPUT_NAME =
            Pattern.compile("(?i)<(?:input|select|textarea)\\b[^>]*\\bname\\s*=\\s*[\"']([^\"']+)");

    private final HttpFetcher fetcher;
    private volatile boolean stopRequested;

    public WebCrawler(HttpFetcher fetcher) {
        this.fetcher = fetcher;
    }

    /** Ask the crawl loop to finish once the request in flight returns. */
    public void stop() {
        stopRequested = true;
    }

    public CrawlResult crawl(URI start, int maxPages, CrawlListener listener) {
        CrawlListener l = listener == null ? CrawlListener.NONE : listener;
        List<FetchResult> pages = new ArrayList<>();
        Set<String> seen = new HashSet<>();
        Deque<String> queue = new ArrayDeque<>();

        String startUrl = Uris.stripFragment(start.toString());
        seen.add(startUrl);
        queue.add(startUrl);
        int fetched = 0;
        int limit = Math.max(1, maxPages);

        while (!queue.isEmpty() && fetched < limit && !stopRequested) {
            String url = queue.poll();

            FetchResult page;
            try {
                page = fetcher.fetch(URI.create(url));
            } catch (FetchException e) {
                l.error(url, e.getMessage());
                continue;
            } catch (IllegalArgumentException e) {
                l.error(url, "unusable URL: " + e.getMessage());
                continue;
            }

            fetched++;
            pages.add(page);
            l.pageCrawled(page, fetched, queue.size());

            if (!page.isHtml()) {
                continue;
            }
            for (String link : extractLinks(page, start)) {
                if (seen.add(link)) {
                    l.linkDiscovered(link, url);
                    queue.add(link);
                }
            }
        }
        return new CrawlResult(pages, stopRequested);
    }

    /** Absolute, fragment-free, same-origin URLs found in one HTML page. */
    private List<String> extractLinks(FetchResult page, URI origin) {
        List<String> out = new ArrayList<>();

        Matcher links = LINK.matcher(page.getBody());
        while (links.find()) {
            addIfUsable(out, page.getUri(), links.group(1).trim(), origin);
        }

        Matcher forms = FORM_BLOCK.matcher(page.getBody());
        while (forms.find()) {
            String attrs = forms.group(1);
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

This lesson ties its explanation to `src/main/java/local/foundev/zap/core/Uris.java`, `src/main/java/local/foundev/zap/core/WebCrawler.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
