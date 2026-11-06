# Read reportsupport and scannerapp in the source

**Lesson ID:** `owasp-zap-module-11-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/main/java/local/foundev/zap/report/ReportSupport.java] and [src/main/java/local/foundev/zap/ScannerApp.java]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include class, main; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/main/java/local/foundev/zap/report/ReportSupport.java`, `src/main/java/local/foundev/zap/ScannerApp.java`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/main/java/local/foundev/zap/report/ReportSupport.java`, `package local.foundev.zap.report;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/report/ReportSupport.java`, `import local.foundev.zap.model.Alert;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/report/ReportSupport.java`, `import local.foundev.zap.model.Risk;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/report/ReportSupport.java`, `import java.util.ArrayList;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/report/ReportSupport.java`, `import java.util.Comparator;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ScannerApp.java`, `package local.foundev.zap;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ScannerApp.java`, `import local.foundev.zap.ui.ScannerFrame;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ScannerApp.java`, `import javax.swing.SwingUtilities;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ScannerApp.java`, `import javax.swing.UIManager;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class ScannerApp {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public static void main(String[] args) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/main/java/local/foundev/zap/report/ReportSupport.java

```text
package local.foundev.zap.report;

import local.foundev.zap.model.Alert;
import local.foundev.zap.model.Risk;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/** Shared helpers for the report writers. */
final class ReportSupport {

    private ReportSupport() {
    }

    /** Most severe first, then by name. */
    static List<Alert> sorted(List<Alert> alerts) {
        List<Alert> copy = new ArrayList<>(alerts == null ? List.of() : alerts);
        copy.sort(Comparator.comparingInt((Alert a) -> a.getRisk().ordinal()).reversed()
                .thenComparing(Alert::getName, String.CASE_INSENSITIVE_ORDER));
        return copy;
    }

    static int count(List<Alert> alerts, Risk risk) {
        int count = 0;
        for (Alert alert : alerts) {
            if (alert.getRisk() == risk) {
                count++;
            }
        }
        return count;
    }

    static String htmlEscape(String s) {
        if (s == null || s.isEmpty()) {
            return "";
        }
        StringBuilder sb = new StringBuilder(s.length() + 16);
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            switch (ch) {
                case '&':
                    sb.append("&amp;");
                    break;
                case '<':
                    sb.append("&lt;");
                    break;
                case '>':
                    sb.append("&gt;");
                    break;
                case '"':
                    sb.append("&quot;");
                    break;
                case '\'':
                    sb.append("&#39;");
                    break;
                default:
                    sb.append(ch);
            }
        }
        return sb.toString();
    }
}

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

This lesson ties its explanation to `src/main/java/local/foundev/zap/report/ReportSupport.java`, `src/main/java/local/foundev/zap/ScannerApp.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
