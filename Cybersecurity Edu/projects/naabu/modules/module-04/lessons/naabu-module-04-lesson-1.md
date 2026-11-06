# A beginner's model of runtime configuration connected to code

**Lesson ID:** `naabu-module-04-lesson-1`

## Purpose and learning objectives

Inspect the declared manifests .github/workflows/ci.yml, go.mod and trace the relevant package or setting into implementation file main.go. Separate a declaration from an imported, configured, or executed behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `.github/workflows/ci.yml`, `go.mod`, `main.go`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- The excerpt from `.github/workflows/ci.yml` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `go.mod` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `main.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func main() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### .github/workflows/ci.yml

```text
name: CI

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: '1.22'
      - name: Vet the code
        run: go vet ./...
      - name: Check the formatting
        run: test -z "$(gofmt -l .)"
      - name: Run the tests
        run: go test -race ./...

```

### go.mod

```text
module foundev/naabu

go 1.22

```

### main.go

```text
package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"
)

func main() {
	host := flag.String("host", "127.0.0.1", "target host")
	ports := flag.String("ports", "22,80,443,8000-8010", "ports to scan")
	timeout := flag.Duration("timeout", DefaultTimeout, "per-port timeout")
	flag.Parse()

	list, err := ParsePorts(*ports)
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	results := Scan(*host, list, *timeout)
	encoder := json.NewEncoder(os.Stdout)
	encoder.SetIndent("", "  ")
	if err := encoder.Encode(map[string]any{"host": *host, "results": results, "open": OpenPorts(results)}); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
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

This lesson ties its explanation to `.github/workflows/ci.yml`, `go.mod`, `main.go`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
