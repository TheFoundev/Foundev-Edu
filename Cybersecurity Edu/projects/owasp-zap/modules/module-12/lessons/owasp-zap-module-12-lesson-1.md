# A beginner's model of scannercli and scannerframe

**Lesson ID:** `owasp-zap-module-12-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/main/java/local/foundev/zap/ScannerCli.java] and [src/main/java/local/foundev/zap/ui/ScannerFrame.java]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include class, main, class, onStatus, onLink, onFinished; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/main/java/local/foundev/zap/ScannerCli.java`, `src/main/java/local/foundev/zap/ui/ScannerFrame.java`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

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
- In `src/main/java/local/foundev/zap/ui/ScannerFrame.java`, `package local.foundev.zap.ui;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ui/ScannerFrame.java`, `import local.foundev.zap.core.ScanEngine;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ui/ScannerFrame.java`, `import local.foundev.zap.core.ScanProgress;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ui/ScannerFrame.java`, `import local.foundev.zap.core.ScanSummary;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/local/foundev/zap/ui/ScannerFrame.java`, `import local.foundev.zap.core.Uris;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public final class ScannerFrame extends JFrame {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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

### src/main/java/local/foundev/zap/ui/ScannerFrame.java

```text
package local.foundev.zap.ui;

import local.foundev.zap.core.ScanEngine;
import local.foundev.zap.core.ScanProgress;
import local.foundev.zap.core.ScanSummary;
import local.foundev.zap.core.Uris;
import local.foundev.zap.model.Alert;
import local.foundev.zap.model.AlertStore;
import local.foundev.zap.model.Risk;
import local.foundev.zap.report.HtmlReportWriter;
import local.foundev.zap.report.JsonReportWriter;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.JScrollPane;
import javax.swing.JSplitPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.JTree;
import javax.swing.SwingUtilities;
import javax.swing.SwingWorker;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutionException;

/**
 * Main window: target URL bar, the "I am authorized" gate, crawl progress,
 * the discovered-site tree, a color-coded alerts grid and report export.
 * Active checks stay disabled until the checkbox is ticked.
 */
public final class ScannerFrame extends JFrame {

    private static final Color HIGH_BG = new Color(0xFF, 0xD6, 0xD6);
    private static final Color HIGH_FG = new Color(0x8B, 0x00, 0x00);
    private static final Color MEDIUM_BG = new Color(0xFF, 0xE9, 0xC8);
    private static final Color MEDIUM_FG = new Color(0x7A, 0x4B, 0x00);
    private static final Color LOW_BG = new Color(0xFF, 0xF6, 0xC9);
    private static final Color LOW_FG = new Color(0x6B, 0x5B, 0x00);
    private static final Color INFO_BG = new Color(0xDB, 0xE9, 0xFF);
    private static final Color INFO_FG = new Color(0x0B, 0x3D, 0x91);

    private final AlertStore store;
    private final ScanEngine engine;
    private final AlertTableModel tableModel;
    private final Map<String, DefaultMutableTreeNode> nodeMap = new HashMap<>();

    private JTextField urlField;
    private JCheckBox authorizedCheck;
    private JButton startButton;
    private JButton stopButton;
    private JButton exportHtmlButton;
    private JButton exportJsonButton;
    private JComboBox<Object> riskFilter;
    private JProgressBar progressBar;
    private JLabel statusLabel;
    private JTree siteTree;
    private JTable alertsTable;
    private URI lastTarget;

    private final ScanProgress uiProgress = new ScanProgress() {
        @Override
        public void onStatus(String message) {
            SwingUtilities.invokeLater(() -> {
                statusLabel.setText(message);
                refreshAlerts();
            });
        }

        @Override
        public void onLink(String url, String parentUrl) {
            SwingUtilities.invokeLater(() -> addTreeNode(url, parentUrl));
        }

        @Override
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

This lesson ties its explanation to `src/main/java/local/foundev/zap/ScannerCli.java`, `src/main/java/local/foundev/zap/ui/ScannerFrame.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
