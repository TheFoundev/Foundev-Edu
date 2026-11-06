# Read alertstore and confidence in the source

**Lesson ID:** `owasp-zap-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/main/java/local/foundev/zap/model/AlertStore.java] and [src/main/java/local/foundev/zap/model/Confidence.java]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include class, boolean, int, void, List, List, int, int, Confidence, label, toString; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/main/java/local/foundev/zap/model/AlertStore.java`, `src/main/java/local/foundev/zap/model/Confidence.java`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

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
- In `src/main/java/local/foundev/zap/model/Confidence.java`, `package local.foundev.zap.model;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public enum Confidence {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public String label() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public String toString() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### src/main/java/local/foundev/zap/model/Confidence.java

```text
package local.foundev.zap.model;

/** How sure the scanner is that a finding is real. */
public enum Confidence {

    LOW("Low"),
    MEDIUM("Medium"),
    HIGH("High");

    private final String label;

    Confidence(String label) {
        this.label = label;
    }

    public String label() {
        return label;
    }

    @Override
    public String toString() {
        return label;
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

This lesson ties its explanation to `src/main/java/local/foundev/zap/model/AlertStore.java`, `src/main/java/local/foundev/zap/model/Confidence.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
