# Read risk and alerttablemodel in the source

**Lesson ID:** `owasp-zap-module-03-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/main/java/local/foundev/zap/model/Risk.java] and [src/main/java/local/foundev/zap/ui/AlertTableModel.java]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include Risk, label, toString, class, setAlerts, getRowCount, getColumnCount, getColumnName, getValueAt; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/main/java/local/foundev/zap/model/Risk.java`, `src/main/java/local/foundev/zap/ui/AlertTableModel.java`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/main/java/local/foundev/zap/model/Risk.java`, `package local.foundev.zap.model;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public enum Risk {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public String label() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public String toString() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/main/java/local/foundev/zap/ui/AlertTableModel.java`, `package local.foundev.zap.ui;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ui/AlertTableModel.java`, `import local.foundev.zap.model.Alert;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ui/AlertTableModel.java`, `import local.foundev.zap.model.Confidence;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ui/AlertTableModel.java`, `import local.foundev.zap.model.Risk;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ui/AlertTableModel.java`, `import javax.swing.table.AbstractTableModel;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class AlertTableModel extends AbstractTableModel {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public void setAlerts(List<Alert> alerts) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public int getRowCount() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public int getColumnCount() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public String getColumnName(int column) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public Object getValueAt(int row, int column) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/main/java/local/foundev/zap/model/Risk.java

```text
package local.foundev.zap.model;

/**
 * Risk level of a finding, declared from least to most severe so that
 * {@link #ordinal()} orders alerts naturally.
 */
public enum Risk {

    INFORMATIONAL("Informational"),
    LOW("Low"),
    MEDIUM("Medium"),
    HIGH("High");

    private final String label;

    Risk(String label) {
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

### src/main/java/local/foundev/zap/ui/AlertTableModel.java

```text
package local.foundev.zap.ui;

import local.foundev.zap.model.Alert;
import local.foundev.zap.model.Confidence;
import local.foundev.zap.model.Risk;

import javax.swing.table.AbstractTableModel;
import java.util.ArrayList;
import java.util.List;

/** Table model behind the alerts grid. */
public final class AlertTableModel extends AbstractTableModel {

    private static final String[] COLUMNS = {"Risk", "Confidence", "Alert", "URL", "Parameter", "Evidence"};

    private List<Alert> rows = new ArrayList<>();

    public void setAlerts(List<Alert> alerts) {
        this.rows = new ArrayList<>(alerts == null ? List.of() : alerts);
        fireTableDataChanged();
    }

    @Override
    public int getRowCount() {
        return rows.size();
    }

    @Override
    public int getColumnCount() {
        return COLUMNS.length;
    }

    @Override
    public String getColumnName(int column) {
        return COLUMNS[column];
    }

    @Override
    public Class<?> getColumnClass(int column) {
        if (column == 0) {
            return Risk.class;
        }
        if (column == 1) {
            return Confidence.class;
        }
        return String.class;
    }

    @Override
    public Object getValueAt(int row, int column) {
        Alert a = rows.get(row);
        switch (column) {
            case 0:
                return a.getRisk();
            case 1:
                return a.getConfidence();
            case 2:
                return a.getName();
            case 3:
                return a.getUrl();
            case 4:
                return a.getParameter();
            case 5:
                return a.getEvidence();
            default:
                return "";
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

This lesson ties its explanation to `src/main/java/local/foundev/zap/model/Risk.java`, `src/main/java/local/foundev/zap/ui/AlertTableModel.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
