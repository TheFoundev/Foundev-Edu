# A beginner's model of fetchresult and httpfetcher

**Lesson ID:** `owasp-zap-module-06-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/main/java/local/foundev/zap/core/FetchResult.java] and [src/main/java/local/foundev/zap/core/HttpFetcher.java]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include class, getUri, getStatusCode, header, headers, getBody, isHtml, class, String, fetch; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/main/java/local/foundev/zap/core/FetchResult.java`, `src/main/java/local/foundev/zap/core/HttpFetcher.java`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/main/java/local/foundev/zap/core/FetchResult.java`, `package local.foundev.zap.core;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/FetchResult.java`, `import java.net.URI;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/FetchResult.java`, `import java.util.ArrayList;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/FetchResult.java`, `import java.util.LinkedHashMap;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/FetchResult.java`, `import java.util.List;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class FetchResult {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public URI getUri() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public int getStatusCode() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public String header(String name) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public List<String> headers(String name) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public String getBody() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/main/java/local/foundev/zap/core/HttpFetcher.java`, `package local.foundev.zap.core;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/HttpFetcher.java`, `import java.io.IOException;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/HttpFetcher.java`, `import java.net.URI;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/HttpFetcher.java`, `import java.net.http.HttpClient;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/core/HttpFetcher.java`, `import java.net.http.HttpRequest;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class HttpFetcher {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public static final String USER_AGENT = "Foundev-Zap/0.1 (authorised security testing)";` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public FetchResult fetch(URI uri) throws FetchException {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/main/java/local/foundev/zap/core/FetchResult.java

```text
package local.foundev.zap.core;

import java.net.URI;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

/**
 * Immutable view of one HTTP response: final URI (after redirects), status
 * code, case-insensitive headers and the (possibly truncated) body.
 */
public final class FetchResult {

    private final URI uri;
    private final int statusCode;
    private final Map<String, List<String>> headersByLowerName;
    private final String body;

    public FetchResult(URI uri, int statusCode, Map<String, List<String>> headers, String body) {
        this.uri = uri;
        this.statusCode = statusCode;
        this.headersByLowerName = new LinkedHashMap<>();
        if (headers != null) {
            for (Map.Entry<String, List<String>> entry : headers.entrySet()) {
                if (entry.getKey() == null) {
                    continue;
                }
                String key = entry.getKey().toLowerCase(Locale.ROOT);
                List<String> bucket = headersByLowerName.computeIfAbsent(key, k -> new ArrayList<>());
                if (entry.getValue() != null) {
                    bucket.addAll(entry.getValue());
                }
            }
        }
        this.body = body == null ? "" : body;
    }

    /** The URI the response was actually served from (after redirects). */
    public URI getUri() {
        return uri;
    }

    public int getStatusCode() {
        return statusCode;
    }

    /** First value of the header, looked up case-insensitively, or null. */
    public String header(String name) {
        List<String> values = headers(name);
        return values.isEmpty() ? null : values.get(0);
    }

    /** All values of the header, looked up case-insensitively, never null. */
    public List<String> headers(String name) {
        if (name == null) {
            return List.of();
        }
        List<String> values = headersByLowerName.get(name.toLowerCase(Locale.ROOT));
        return values == null ? List.of() : values;
    }

    public String getBody() {
        return body;
    }

    public boolean isHtml() {
        String contentType = header("Content-Type");
        return contentType != null && contentType.toLowerCase(Locale.ROOT).contains("text/html");
    }
}

```

### src/main/java/local/foundev/zap/core/HttpFetcher.java

```text
package local.foundev.zap.core;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;

/**
 * Thin wrapper around {@link java.net.http.HttpClient}: fixed timeouts, a
 * honest user agent, redirects followed, bodies truncated for analysis.
 */
public final class HttpFetcher {

    public static final String USER_AGENT = "Foundev-Zap/0.1 (authorised security testing)";

    /** Bodies are cut here to keep very large downloads from exhausting memory. */
    private static final int MAX_BODY_CHARS = 512 * 1024;

    private final HttpClient client;

    public HttpFetcher() {
        client = HttpClient.newBuilder()
                .followRedirects(HttpClient.Redirect.NORMAL)
                .connectTimeout(Duration.ofSeconds(10))
                .build();
    }

    public FetchResult fetch(URI uri) throws FetchException {
        HttpRequest request = HttpRequest.newBuilder(uri)
                .timeout(Duration.ofSeconds(15))
                .header("User-Agent", USER_AGENT)
                .header("Accept", "text/html,application/xhtml+xml,*/*;q=0.8")
                .GET()
                .build();
        try {
            HttpResponse<String> response =
                    client.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body() == null ? "" : response.body();
            if (body.length() > MAX_BODY_CHARS) {
                body = body.substring(0, MAX_BODY_CHARS);
            }
            URI effective = response.uri() != null ? response.uri() : uri;
            return new FetchResult(effective, response.statusCode(), response.headers().map(), body);
        } catch (IOException e) {
            throw new FetchException("request failed: " + e, e);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new FetchException("interrupted while fetching", e);
        }
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

This lesson ties its explanation to `src/main/java/local/foundev/zap/core/FetchResult.java`, `src/main/java/local/foundev/zap/core/HttpFetcher.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
