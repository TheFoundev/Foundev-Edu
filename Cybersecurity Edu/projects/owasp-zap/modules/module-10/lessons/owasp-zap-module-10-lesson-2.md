# Read htmlreportwriter and jsonreportwriter in the source

**Lesson ID:** `owasp-zap-module-10-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/main/java/local/foundev/zap/report/HtmlReportWriter.java] and [src/main/java/local/foundev/zap/report/JsonReportWriter.java]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include class, render, class, String, render; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/main/java/local/foundev/zap/report/HtmlReportWriter.java`, `src/main/java/local/foundev/zap/report/JsonReportWriter.java`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/main/java/local/foundev/zap/report/HtmlReportWriter.java`, `package local.foundev.zap.report;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/report/HtmlReportWriter.java`, `import local.foundev.zap.model.Alert;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/report/HtmlReportWriter.java`, `import local.foundev.zap.model.Risk;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/report/HtmlReportWriter.java`, `import java.time.Instant;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/report/HtmlReportWriter.java`, `import java.util.List;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class HtmlReportWriter {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public static String render(String target, List<Alert> alerts) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/main/java/local/foundev/zap/report/JsonReportWriter.java`, `package local.foundev.zap.report;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/report/JsonReportWriter.java`, `import local.foundev.zap.model.Alert;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/report/JsonReportWriter.java`, `import local.foundev.zap.model.Risk;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/report/JsonReportWriter.java`, `import java.time.Instant;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/report/JsonReportWriter.java`, `import java.util.List;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class JsonReportWriter {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public static final String TOOL_NAME = "Foundev OWASP ZAP MVP";` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public static String render(String target, List<Alert> alerts) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/main/java/local/foundev/zap/report/HtmlReportWriter.java

```text
package local.foundev.zap.report;

import local.foundev.zap.model.Alert;
import local.foundev.zap.model.Risk;

import java.time.Instant;
import java.util.List;

/** Renders the alert store as a self-contained HTML report page. */
public final class HtmlReportWriter {

    private HtmlReportWriter() {
    }

    public static String render(String target, List<Alert> alerts) {
        List<Alert> sorted = ReportSupport.sorted(alerts);
        StringBuilder sb = new StringBuilder(8192);

        sb.append("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n");
        sb.append("<meta charset=\"utf-8\">\n");
        sb.append("<title>Security assessment report</title>\n");
        sb.append("<style>\n");
        sb.append("body{font-family:Segoe UI,Helvetica,Arial,sans-serif;margin:2rem;color:#1c2733;background:#f6f8fa;}\n");
        sb.append("h1{font-size:1.5rem;}\n");
        sb.append(".meta{color:#57606a;}\n");
        sb.append("table{border-collapse:collapse;width:100%;background:#fff;}\n");
        sb.append("th,td{border:1px solid #d8dee4;padding:.5rem .6rem;text-align:left;vertical-align:top;font-size:.9rem;}\n");
        sb.append("th{background:#eaeef2;}\n");
        sb.append(".risk{font-weight:600;text-align:center;white-space:nowrap;}\n");
        sb.append(".risk-HIGH{background:#ffd6d6;color:#8b0000;}\n");
        sb.append(".risk-MEDIUM{background:#ffe9c8;color:#7a4b00;}\n");
        sb.append(".risk-LOW{background:#fff6c9;color:#6b5b00;}\n");
        sb.append(".risk-INFORMATIONAL{background:#dbe9ff;color:#0b3d91;}\n");
        sb.append(".summary span{display:inline-block;margin-right:1rem;padding:.2rem .6rem;border-radius:.6rem;}\n");
        sb.append("</style>\n</head>\n<body>\n");

        sb.append("<h1>Security assessment report</h1>\n");
        sb.append("<p class=\"meta\">Target: ").append(ReportSupport.htmlEscape(target));
        sb.append("<br>Generated: ").append(ReportSupport.htmlEscape(Instant.now().toString()));
        sb.append("<br>Tool: ").append(ReportSupport.htmlEscape(JsonReportWriter.TOOL_NAME));
        sb.append(" &mdash; authorised testing only</p>\n");

        sb.append("<p class=\"summary\">");
        sb.append("<span class=\"risk risk-HIGH\">High: ").append(ReportSupport.count(sorted, Risk.HIGH)).append("</span>");
        sb.append("<span class=\"risk risk-MEDIUM\">Medium: ").append(ReportSupport.count(sorted, Risk.MEDIUM)).append("</span>");
        sb.append("<span class=\"risk risk-LOW\">Low: ").append(ReportSupport.count(sorted, Risk.LOW)).append("</span>");
        sb.append("<span class=\"risk risk-INFORMATIONAL\">Informational: ").append(ReportSupport.count(sorted, Risk.INFORMATIONAL)).append("</span>");
        sb.append("<span>Total: ").append(sorted.size()).append("</span>");
        sb.append("</p>\n");

        sb.append("<table>\n<thead><tr><th>Risk</th><th>Confidence</th><th>Alert</th><th>URL</th>")
                .append("<th>Parameter</th><th>Evidence</th><th>Description</th><th>Remediation</th></tr></thead>\n<tbody>\n");
        if (sorted.isEmpty()) {
            sb.append("<tr><td colspan=\"8\">No alerts.</td></tr>\n");
        }
        for (Alert a : sorted) {
            sb.append("<tr>");
            sb.append("<td class=\"risk risk-").append(a.getRisk().name()).append("\">")
                    .append(ReportSupport.htmlEscape(a.getRisk().label())).append("</td>");
            sb.append("<td>").append(ReportSupport.htmlEscape(a.getConfidence().label())).append("</td>");
            sb.append("<td>").append(ReportSupport.htmlEscape(a.getName())).append("</td>");
            sb.append("<td>").append(ReportSupport.htmlEscape(a.getUrl())).append("</td>");
            sb.append("<td>").append(ReportSupport.htmlEscape(a.getParameter())).append("</td>");
            sb.append("<td>").append(ReportSupport.htmlEscape(a.getEvidence())).append("</td>");
            sb.append("<td>").append(ReportSupport.htmlEscape(a.getDescription())).append("</td>");
            sb.app
```

### src/main/java/local/foundev/zap/report/JsonReportWriter.java

```text
package local.foundev.zap.report;

import local.foundev.zap.model.Alert;
import local.foundev.zap.model.Risk;

import java.time.Instant;
import java.util.List;

/** Renders the alert store as a small JSON document, without any libraries. */
public final class JsonReportWriter {

    public static final String TOOL_NAME = "Foundev OWASP ZAP MVP";

    private JsonReportWriter() {
    }

    public static String render(String target, List<Alert> alerts) {
        List<Alert> sorted = ReportSupport.sorted(alerts);
        StringBuilder sb = new StringBuilder(4096);
        sb.append("{\n");
        sb.append("  \"tool\": ").append(quote(TOOL_NAME)).append(",\n");
        sb.append("  \"target\": ").append(quote(target)).append(",\n");
        sb.append("  \"generatedAt\": ").append(quote(Instant.now().toString())).append(",\n");
        sb.append("  \"summary\": {");
        sb.append("\"high\": ").append(ReportSupport.count(sorted, Risk.HIGH));
        sb.append(", \"medium\": ").append(ReportSupport.count(sorted, Risk.MEDIUM));
        sb.append(", \"low\": ").append(ReportSupport.count(sorted, Risk.LOW));
        sb.append(", \"informational\": ").append(ReportSupport.count(sorted, Risk.INFORMATIONAL));
        sb.append(", \"total\": ").append(sorted.size());
        sb.append("},\n");
        sb.append("  \"alerts\": [");
        for (int i = 0; i < sorted.size(); i++) {
            Alert a = sorted.get(i);
            sb.append(i == 0 ? "\n" : ",\n");
            sb.append("    {");
            sb.append("\"name\": ").append(quote(a.getName()));
            sb.append(", \"risk\": ").append(quote(a.getRisk().name()));
            sb.append(", \"confidence\": ").append(quote(a.getConfidence().name()));
            sb.append(", \"url\": ").append(quote(a.getUrl()));
            sb.append(", \"parameter\": ").append(quote(a.getParameter()));
            sb.append(", \"evidence\": ").append(quote(a.getEvidence()));
            sb.append(", \"description\": ").append(quote(a.getDescription()));
            sb.append(", \"remediation\": ").append(quote(a.getRemediation()));
            sb.append("}");
        }
        if (!sorted.isEmpty()) {
            sb.append("\n  ");
        }
        sb.append("]\n}\n");
        return sb.toString();
    }

    private static String quote(String s) {
        if (s == null) {
            return "\"\"";
        }
        StringBuilder sb = new StringBuilder(s.length() + 2);
        sb.append('"');
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            switch (ch) {
                case '"':
                    sb.append("\\\"");
                    break;
                case '\\':
                    sb.append("\\\\");
                    break;
                case '\n':
                    sb.append("\\n");
                    break;
                case '\r':
                    sb.append("\\r");
                    break;
                case '\t':
                    sb.append("\\t");
                    break;
                case '\b':
                    sb.append("\\b");
                    break;
                case '\f':
                    sb.append("\\f");
                    break;
                default:
                    if (ch < 0x20) {
                        String hex = Integer.toHexString(ch);
                        sb.append("\\u");
                        for (int pad = hex.length(); pad < 4; pad++) {
                            sb.append('0');
                        }
                        sb.append(hex);
                    } else {
                        sb.append(ch);
                    }
            }
        }
        sb.append('"');
        return sb.toString();
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

This lesson ties its explanation to `src/main/java/local/foundev/zap/report/HtmlReportWriter.java`, `src/main/java/local/foundev/zap/report/JsonReportWriter.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
