# A beginner's model of server and kernel

**Lesson ID:** `operating-system-kernel-from-scratch-module-01-lesson-1`

## Purpose and learning objectives

Study the implementation in [web/server.py] and [src/kernel.c]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include source_files, count_lines, count_tests, language_of, summary; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `web/server.py`, `src/kernel.c`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `web/server.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/server.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/server.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/server.py`, `import shutil` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/server.py`, `import subprocess` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def source_files():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def count_lines(path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def count_tests(files):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def language_of(path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def run_demo():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/kernel.c`, `#include "kernel.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### web/server.py

```text
#!/usr/bin/env python3
"""Serve the Operating System Kernel project console.

This server has no third-party dependencies. It serves the static site in this
folder and exposes two real endpoints:

  GET  /api/summary  counts the files, lines and tests of this repository and
                     groups the source lines by language
  POST /api/run      executes the project's own demo command and returns its
                     actual stdout, stderr and exit code

Nothing is mocked. If a toolchain or dependency is missing, the output says so.

Usage:  py -3 web/server.py [--port 8000] [--host 127.0.0.1]
"""
import argparse
import json
import os
import shutil
import subprocess
import time
from collections import Counter
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

WEB = Path(__file__).resolve().parent
ROOT = WEB.parent
DEMO = ["make","test"]
DEMO_TIMEOUT = 120
SKIP_DIRS = {".git", "node_modules", "__pycache__", "target", "build", "dist",
             ".venv", "venv", "vendor", ".idea", ".gradle", "artifacts"}
LANGUAGES = {
    ".py": "Python", ".js": "JavaScript", ".mjs": "JavaScript", ".cjs": "JavaScript",
    ".ts": "TypeScript", ".tsx": "TypeScript", ".jsx": "JavaScript",
    ".go": "Go", ".rs": "Rust", ".java": "Java", ".kt": "Kotlin",
    ".c": "C", ".h": "C", ".cc": "C++", ".cpp": "C++", ".hpp": "C++",
    ".cs": "C#", ".rb": "Ruby", ".php": "PHP", ".swift": "Swift",
    ".ex": "Elixir", ".exs": "Elixir", ".erl": "Erlang", ".hrl": "Erlang",
    ".sol": "Solidity", ".sh": "Shell", ".bash": "Shell", ".ps1": "PowerShell",
    ".yml": "YAML", ".yaml": "YAML", ".sql": "SQL", ".css": "CSS",
    ".html": "HTML", ".md": "Markdown", ".tf": "Terraform", ".toml": "TOML",
}
TEST_HINTS = ("test", "spec")


def source_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in {"package-lock.json", "Cargo.lock", "rebar.lock"}:
            continue
        yield path


def count_lines(path):
    try:
        with path.open("rb") as handle:
            return sum(1 for _ in handle)
    except OSError:
        return 0


def count_tests(files):
    total = 0
    for path in files:
        if not any(hint in path.name.lower() for hint in TEST_HINTS):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        total += text.count("def test_")
        total += text.count("@Test")
        total += text.count("test(") if path.suffix in {".js", ".mjs", ".cjs", ".ts", ".tsx"} else 0
        if path.suffix == ".go":
            total += text.count("func Test")
        if path.suffix == ".rs":
            total += text.count("#[test]")
        if path.suffix in {".c", ".h"}:
            total += text.count("TEST(") + text.count("RUN_TEST(")
    return total


def language_of(path):
    return LANGUAGES.get(path.suffix.lower(), None)


def summary():
    files = [path for path in source_files() if language_of(path)]
    by_language = Counter()
    per_file = []
    for path in files:
        lines = count_lines(path)
        by_language[language_of(path)] += lines
        per_file.append({
            "file": str(path.relative_to(ROOT)).replace(os.sep, "/"),
            "language": language_of(path),
            "lines": lines,
```

### src/kernel.c

```text
#include "kernel.h"

#define VGA_WIDTH 80
#define VGA_HEIGHT 25
#define VGA_MEMORY ((volatile uint16_t *)0xB8000)

size_t kstrlen(const char *text) {
    size_t length = 0;
    while (text[length] != '\0') {
        length++;
    }
    return length;
}

int kstrcmp(const char *left, const char *right) {
    size_t index = 0;
    while (left[index] != '\0' && left[index] == right[index]) {
        index++;
    }
    return (unsigned char)left[index] - (unsigned char)right[index];
}

void *kmemset(void *destination, int value, size_t count) {
    unsigned char *bytes = (unsigned char *)destination;
    size_t index;
    for (index = 0; index < count; index++) {
        bytes[index] = (unsigned char)value;
    }
    return destination;
}

void *kmemcpy(void *destination, const void *source, size_t count) {
    unsigned char *target = (unsigned char *)destination;
    const unsigned char *origin = (const unsigned char *)source;
    size_t index;
    for (index = 0; index < count; index++) {
        target[index] = origin[index];
    }
    return destination;
}

uint8_t vga_color(uint8_t foreground, uint8_t background) {
    return (uint8_t)(foreground | (background << 4));
}

uint16_t vga_entry(char character, uint8_t color) {
    return (uint16_t)((uint8_t)character | ((uint16_t)color << 8));
}

size_t vga_index(size_t row, size_t column) {
    return row * (size_t)VGA_WIDTH + column;
}

void kernel_main(uint32_t magic, uint32_t address) {
    const char *message = "foundev kernel";
    size_t index = 0;
    uint8_t color = vga_color(7, 0);
    size_t cell = vga_index(0, 0);
    (void)magic;
    (void)address;

    for (index = 0; index < (size_t)VGA_WIDTH * (size_t)VGA_HEIGHT; index++) {
        VGA_MEMORY[index] = vga_entry(' ', vga_color(7, 0));
    }
    for (index = 0; message[index] != '\0' && index < (size_t)VGA_WIDTH; index++) {
        VGA_MEMORY[cell + index] = vga_entry(message[index], color);
    }
    for (;;) {
        __asm__ volatile("hlt");
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

This lesson ties its explanation to `web/server.py`, `src/kernel.c`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
