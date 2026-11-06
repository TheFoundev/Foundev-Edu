# Read test code and implementation evidence in the source

**Lesson ID:** `owasp-zap-module-13-lesson-2`

## Purpose and learning objectives

Read the test cases in src/test/java/local/foundev/zap/AlertStoreTest.java, src/test/java/local/foundev/zap/CookieAnalysisTest.java, src/test/java/local/foundev/zap/PassiveAnalyzerTest.java beside the implementation in src/main/java/local/foundev/zap/model/AlertStore.java. Explain the behavior asserted by the tests and trace each assertion to the implementation. A test file describes a check; it does not prove that check passed.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/test/java/local/foundev/zap/AlertStoreTest.java`, `src/test/java/local/foundev/zap/CookieAnalysisTest.java`, `src/test/java/local/foundev/zap/PassiveAnalyzerTest.java`, `src/main/java/local/foundev/zap/model/AlertStore.java`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/test/java/local/foundev/zap/AlertStoreTest.java`, `package local.foundev.zap;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/local/foundev/zap/AlertStoreTest.java`, `import local.foundev.zap.model.Alert;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/local/foundev/zap/AlertStoreTest.java`, `import local.foundev.zap.model.AlertStore;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/local/foundev/zap/AlertStoreTest.java`, `import local.foundev.zap.model.Confidence;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/local/foundev/zap/AlertStoreTest.java`, `import local.foundev.zap.model.Risk;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class AlertStoreTest {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/test/java/local/foundev/zap/CookieAnalysisTest.java`, `package local.foundev.zap;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/local/foundev/zap/CookieAnalysisTest.java`, `import local.foundev.zap.core.FetchResult;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/local/foundev/zap/CookieAnalysisTest.java`, `import local.foundev.zap.core.PassiveAnalyzer;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/local/foundev/zap/CookieAnalysisTest.java`, `import local.foundev.zap.model.Alert;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/local/foundev/zap/CookieAnalysisTest.java`, `import org.junit.jupiter.api.Test;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class CookieAnalysisTest {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/test/java/local/foundev/zap/PassiveAnalyzerTest.java`, `package local.foundev.zap;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/local/foundev/zap/PassiveAnalyzerTest.java`, `import local.foundev.zap.core.FetchResult;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/local/foundev/zap/PassiveAnalyzerTest.java`, `import local.foundev.zap.core.PassiveAnalyzer;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/local/foundev/zap/PassiveAnalyzerTest.java`, `import local.foundev.zap.model.Alert;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/local/foundev/zap/PassiveAnalyzerTest.java`, `import local.foundev.zap.model.Risk;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class PassiveAnalyzerTest {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/main/java/local/foundev/zap/model/AlertStore.java`, `package local.foundev.zap.model;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/model/AlertStore.java`, `import java.util.ArrayList;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/model/AlertStore.java`, `import java.util.HashSet;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/model/AlertStore.java`, `import java.util.List;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/model/AlertStore.java`, `import java.util.Set;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class AlertStore {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public synchronized boolean add(Alert alert) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public synchronized int addAll(List<Alert> items) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public synchronized void clear() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public synchronized List<Alert> snapshot() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public synchronized List<Alert> byRisk(Risk risk) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/test/java/local/foundev/zap/AlertStoreTest.java

```text
package local.foundev.zap;

import local.foundev.zap.model.Alert;
import local.foundev.zap.model.AlertStore;
import local.foundev.zap.model.Confidence;
import local.foundev.zap.model.Risk;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

/** The store keeps every finding once and can be filtered by risk. */
class AlertStoreTest {

    private static Alert alert(String name, String url, String parameter, Risk risk) {
        return new Alert(name, risk, Confidence.HIGH, url, parameter, "evidence", "why", "fix");
    }

    @Test
    void anAlertIsStoredOnce() {
        AlertStore store = new AlertStore();

        assertTrue(store.add(alert("XSS", "http://a/", "q", Risk.HIGH)));
        assertFalse(store.add(alert("XSS", "http://a/", "q", Risk.HIGH)));

        assertEquals(1, store.size());
    }

    @Test
    void theSameFindingOnAnotherUrlIsAnotherAlert() {
        AlertStore store = new AlertStore();

        store.add(alert("XSS", "http://a/", "q", Risk.HIGH));
        store.add(alert("XSS", "http://b/", "q", Risk.HIGH));

        assertEquals(2, store.size());
    }

    @Test
    void theSameFindingOnAnotherParameterIsAnotherAlert() {
        AlertStore store = new AlertStore();

        store.add(alert("XSS", "http://a/", "q", Risk.HIGH));
        store.add(alert("XSS", "http://a/", "id", Risk.HIGH));

        assertEquals(2, store.size());
    }

    @Test
    void aNullAlertIsRefused() {
        AlertStore store = new AlertStore();

        assertFalse(store.add(null));
        assertEquals(0, store.size());
    }

    @Test
    void addAllCountsOnlyTheNewAlerts() {
        AlertStore store = new AlertStore();
        store.add(alert("XSS", "http://a/", "q", Risk.HIGH));

        int added = store.addAll(List.of(
                alert("XSS", "http://a/", "q", Risk.HIGH),
                alert("SQLi", "http://a/", "q", Risk.HIGH),
                alert("HSTS", "http://a/", "", Risk.LOW)));

        assertEquals(2, added);
        assertEquals(3, store.size());
    }

    @Test
    void addAllOfNullIsZero() {
        AlertStore store = new AlertStore();

        assertEquals(0, store.addAll(null));
    }

    @Test
    void theAlertsCanBeFilteredByRisk() {
        AlertStore store = new AlertStore();
        store.add(alert("XSS", "http://a/", "q", Risk.HIGH));
        store.add(alert("HSTS", "http://a/", "", Risk.LOW));
        store.add(alert("CSP", "http://a/", "", Risk.MEDIUM));

        assertEquals(1, store.countByRisk(Risk.HIGH));
        assertEquals(3, store.byRisk(Risk.HIGH).size() + store.byRisk(Risk.LOW).size()
                + store.byRisk(Risk.MEDIUM).size());
        assertTrue(store.byRisk(Risk.HIGH).get(0).getName().equals("XSS"));
    }

    @Test
    void clearingRemovesEverything() {
        AlertStore store = new AlertStore();
        store.add(alert("XSS", "http://a/", "q", Risk.HIGH));

        store.clear();

```

### src/test/java/local/foundev/zap/CookieAnalysisTest.java

```text
package local.foundev.zap;

import local.foundev.zap.core.FetchResult;
import local.foundev.zap.core.PassiveAnalyzer;
import local.foundev.zap.model.Alert;
import org.junit.jupiter.api.Test;

import java.net.URI;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * The cookie analysis follows RFC 6265: the name/value pair ends at the
 * first ';', the attributes follow it.
 */
class CookieAnalysisTest {

    private static List<Alert> analyze(String setCookie) {
        Map<String, List<String>> headers = new HashMap<>();
        headers.put("Content-Type", List.of("text/html"));
        headers.put("Set-Cookie", List.of(setCookie));
        FetchResult page = new FetchResult(URI.create("https://shop.example.test/"), 200, headers,
                "<html><body>hello</body></html>");
        return new PassiveAnalyzer().analyze(page);
    }

    private static boolean hasAlert(List<Alert> alerts, String fragment) {
        return alerts.stream().anyMatch(alert -> alert.getName().contains(fragment));
    }

    @Test
    void aCookieWithoutAttributesMissesEveryFlag() {
        List<Alert> alerts = analyze("SESSIONid=abc123");

        assertTrue(hasAlert(alerts, "Secure flag"), "missing Secure");
        assertTrue(hasAlert(alerts, "HttpOnly flag"), "missing HttpOnly");
        assertTrue(hasAlert(alerts, "SameSite"), "missing SameSite");
    }

    @Test
    void aWellConfiguredCookieRaisesNothing() {
        List<Alert> alerts = analyze("SESSIONid=abc123; Path=/; Secure; HttpOnly; SameSite=Lax");

        assertFalse(hasAlert(alerts, "Secure flag"), "Secure must be seen");
        assertFalse(hasAlert(alerts, "HttpOnly flag"), "HttpOnly must be seen");
        assertFalse(hasAlert(alerts, "SameSite"), "SameSite must be seen");
    }

    @Test
    void theAttributesAreWhatFollowsTheFirstSemicolon() {
        // RFC 6265: the pair is "SESSIONid=abc", the attributes are the
        // parts that follow the first ';'.
        List<Alert> alerts = analyze("SESSIONid=abc; HttpOnly; Path=/");

        assertFalse(hasAlert(alerts, "HttpOnly flag"), "HttpOnly is a real attribute");
        assertTrue(hasAlert(alerts, "Secure flag"), "Secure is really absent");
    }

    @Test
    void aValueThatLooksLikeASecureFlagIsNotAnAttribute() {
        List<Alert> alerts = analyze("SESSIONid=Secure");

        assertTrue(hasAlert(alerts, "Secure flag"), "the value is not the attribute");
    }

    @Test
    void theNameIsThePartBeforeTheFirstEquals() {
        List<Alert> alerts = analyze("SESSIONid=a=b; Path=/");

        assertTrue(alerts.stream().allMatch(alert -> !alert.getName().contains("SESSIONid=a")),
                "the name of the cookie is SESSIONid, got: " + alerts);
    }

    @Test
    void anExpiresAttributeIsNotMistakenForAFlag() {
        List<Alert> alerts = analyze("SESSIONid=abc; Expires=Wed, 21 Oct 2026 07:28:00 GMT; Secure; HttpOnly");

        assertFalse(hasAlert(alerts, "Secure flag"), "Secure must be seen");
        assertFalse(hasAlert(alerts, "HttpOnly flag"), "HttpOnly must be seen");
        assertTrue(hasAlert(alerts, "SameSite"), "SameSite is really absent");
    }
}

```

### src/test/java/local/foundev/zap/PassiveAnalyzerTest.java

```text
package local.foundev.zap;

import local.foundev.zap.core.FetchResult;
import local.foundev.zap.core.PassiveAnalyzer;
import local.foundev.zap.model.Alert;
import local.foundev.zap.model.Risk;
import org.junit.jupiter.api.Test;

import java.net.URI;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class PassiveAnalyzerTest {

    private static FetchResult page(String url, Map<String, List<String>> headers, String body) {
        return new FetchResult(URI.create(url), 200, headers, body);
    }

    private static List<String> names(List<Alert> alerts) {
        List<String> out = new ArrayList<>();
        for (Alert alert : alerts) {
            out.add(alert.getName());
        }
        return out;
    }

    @Test
    void flagsMissingSecurityHeadersOnBareHttpsResponse() {
        Map<String, List<String>> headers = new HashMap<>();
        headers.put("Content-Type", List.of("text/html; charset=utf-8"));
        headers.put("Server", List.of("Apache/2.4.57 (Unix)"));
        headers.put("Set-Cookie", List.of("SESSIONid=abc123; Path=/"));
        FetchResult page = page("https://shop.example.test/", headers,
                "<html><body>hello</body></html>");

        List<Alert> alerts = new PassiveAnalyzer().analyze(page);
        List<String> names = names(alerts);

        assertTrue(names.contains("Content-Security-Policy header not set"), String.valueOf(names));
        assertTrue(names.contains("X-Frame-Options header not set"), String.valueOf(names));
        assertTrue(names.contains("Strict-Transport-Security header not set"), String.valueOf(names));
        assertTrue(names.contains("Server banner disclosed"), String.valueOf(names));
        assertTrue(names.stream().anyMatch(n -> n.contains("Secure flag")), String.valueOf(names));
        assertTrue(names.stream().anyMatch(n -> n.contains("HttpOnly flag")), String.valueOf(names));
        assertFalse(alerts.stream().anyMatch(a -> a.getRisk() == Risk.HIGH),
                "passive checks must not report high risk for this fixture");
    }

    @Test
    void acceptsWellConfiguredResponseWithoutAlerts() {
        Map<String, List<String>> headers = new HashMap<>();
        headers.put("Content-Type", List.of("text/html"));
        headers.put("Content-Security-Policy", List.of("default-src 'self'; frame-ancestors 'none'"));
        headers.put("X-Frame-Options", List.of("DENY"));
        headers.put("X-Content-Type-Options", List.of("nosniff"));
        headers.put("Strict-Transport-Security", List.of("max-age=31536000; includeSubDomains"));
        headers.put("Set-Cookie", List.of("SESSIONid=abc123; Path=/; Secure; HttpOnly; SameSite=Lax"));
        FetchResult page = page("https://shop.example.test/", headers,
                "<html><body>ok</body></html>");

        List<Alert> alerts = new PassiveAnalyzer().analyze(page);

        assertTrue(alerts.isEmpty(), "expected no alerts but got: " + names(alerts));
    }

    @Test
    void detectsDirectoryListingIndexPage() {
        Map<String, List<String>> headers = new HashMap<>();
        headers.put("Content-Type", List.of("text/html"));
        FetchResult page = page("http://files.example.test:8080/uploads/", headers,
                "<html><head><title>Index of /uploads</title></head><body></body></html>");

        List<Alert> alerts = new PassiveAnalyzer().analyze(page);

        assertTrue(names(alerts).contains("Directory listing enabled"), String.valueOf(names(alerts)));
    }
}

```

### src/main/java/local/foundev/zap/model/AlertStore.java

```text
package local.foundev.zap.model;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Thread-safe in-memory store for the alerts of the current scan.
 * Identical findings (same name, URL and parameter) are stored only once.
 */
public final class AlertStore {

    private final List<Alert> alerts = new ArrayList<>();
    private final Set<String> seenKeys = new HashSet<>();

    /** Returns true when the alert was new and has been stored. */
    public synchronized boolean add(Alert alert) {
        if (alert == null) {
            return false;
        }
        if (!seenKeys.add(alert.dedupKey())) {
            return false;
        }
        alerts.add(alert);
        return true;
    }

    /** Stores every new alert from the list, returns how many were added. */
    public synchronized int addAll(List<Alert> items) {
        if (items == null) {
            return 0;
        }
        int added = 0;
        for (Alert alert : items) {
            if (add(alert)) {
                added++;
            }
        }
        return added;
    }

    public synchronized void clear() {
        alerts.clear();
        seenKeys.clear();
    }

    /** A mutable copy of every stored alert. */
    public synchronized List<Alert> snapshot() {
        return new ArrayList<>(alerts);
    }

    /** Only the alerts at exactly the given risk level. */
    public synchronized List<Alert> byRisk(Risk risk) {
        List<Alert> out = new ArrayList<>();
        for (Alert alert : alerts) {
            if (alert.getRisk() == risk) {
                out.add(alert);
            }
        }
        return out;
    }

    public synchronized int countByRisk(Risk risk) {
        int count = 0;
        for (Alert alert : alerts) {
            if (alert.getRisk() == risk) {
                count++;
            }
        }
        return count;
    }

    public synchronized int size() {
        return alerts.size();
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

This lesson ties its explanation to `src/test/java/local/foundev/zap/AlertStoreTest.java`, `src/test/java/local/foundev/zap/CookieAnalysisTest.java`, `src/test/java/local/foundev/zap/PassiveAnalyzerTest.java`, `src/main/java/local/foundev/zap/model/AlertStore.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
