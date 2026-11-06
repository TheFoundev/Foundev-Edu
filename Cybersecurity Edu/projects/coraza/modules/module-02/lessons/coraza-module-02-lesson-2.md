# Read api impl and waf in the source

**Lesson ID:** `coraza-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [web/api_impl.py] and [waf.go]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include main, _sources, _build_helper, Middleware, Inspectable, decodeOnce, Inspect, Score, Blocked, Evidence; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `web/api_impl.py`, `waf.go`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `web/api_impl.py`, `from __future__ import annotations` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import hashlib` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import re` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import shutil` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func main() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _sources() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _build_helper() -> Path | None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _run_helper(request: dict) -> dict | None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _rules_from_source() -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _inspect_in_python(request: dict) -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `waf.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `waf.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func Middleware(next http.Handler) http.Handler {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func Inspectable(request *http.Request) Request {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func decodeOnce(text string) string {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func Inspect(request Request) []Finding {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func Score(findings []Finding) int {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func Blocked(findings []Finding) bool {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### web/api_impl.py

```text
"""The API of the firewall: the rule set and the findings of a request.

The numbers come from the Go code of the project. A helper program is built
from the sources of the project (waf.go, main.go and go.mod) with a `main`
that reads the rules, inspects a request with Inspect and puts the same
decision in front of a handler with Middleware, and prints the result as
JSON. When the Go toolchain is not installed, the rules are read from waf.go
and the same patterns are applied here.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(tempfile.gettempdir()) / "foundev-go-helpers"
GO = shutil.which("go")

#: The request the console shows when nothing was inspected yet.
SAMPLE = {"method": "GET", "path": "/items", "query": "id=1 union select 1", "body": ""}

#: The helper program: it inspects a request and prints the result as JSON.
HELPER = r'''
package main

import (
	"encoding/json"
	"flag"
	"net/http"
	"net/http/httptest"
	"os"
)

func main() {
	method := flag.String("method", "GET", "the method of the request")
	path := flag.String("path", "/items", "the path of the request")
	query := flag.String("query", "id=1 union select 1", "the query of the request")
	body := flag.String("body", "", "the body of the request")
	flag.Parse()

	rulesOut := []map[string]any{}
	for _, rule := range rules {
		rulesOut = append(rulesOut, map[string]any{
			"id":       rule.ID,
			"category": rule.Category,
			"severity": rule.Severity,
			"pattern":  rule.Pattern.String(),
		})
	}

	request := Request{Method: *method, Path: *path, Query: *query, Body: *body}
	findings := Inspect(request)
	decision := "allow"
	if Blocked(findings) {
		decision = "block"
	}

	// the same decision in front of a handler
	target := "http://127.0.0.1" + *path
	if *query != "" {
		target = target + "?" + *query
	}
	httpRequest, err := http.NewRequest(*method, target, http.NoBody)
	if err != nil {
		json.NewEncoder(os.Stdout).Encode(map[string]any{"error": err.Error()})
		os.Exit(1)
	}
	recorder := httptest.NewRecorder()
	handler := Middleware(http.HandlerFunc(func(writer http.ResponseWriter, r *http.Request) {
		writer.WriteHeader(http.StatusOK)
	}))
	handler.ServeHTTP(recorder, httpRequest)

	json.NewEncoder(os.Stdout).Encode(map[string]any{
		"rules":    rulesOut,
		"findings": findings,
		"decision": decision,
		"score":    Score(findings),
		"status":   recorder.Code,
		"request":  request,
	})
}
'''

#: The last inspection.
_STATE: dict = {}


def _sources() -> dict:
    """The sources of the project that the helper is built from."""
    files = {}
    for path in sorted(ROOT.glob("*.go")):
        if path.name.endswith("_test.go"):
```

### waf.go

```text
package main

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
	"regexp"
)

// Request is the subset of an HTTP request the firewall inspects.
type Request struct {
	Method string
	Path   string
	Query  string
	Body   string
}

// Rule matches one class of attack.
type Rule struct {
	ID       string
	Category string
	Severity int
	Pattern  *regexp.Regexp
}

// Finding is a rule match for one request.
type Finding struct {
	Rule     string `json:"rule"`
	Category string `json:"category"`
	Severity int    `json:"severity"`
	Evidence string `json:"evidence"`
}

var rules = []Rule{
	{"CRS-001", "sqli", 3, regexp.MustCompile(`(?i)(union\s+select|or\s+1\s*=\s*1|'\s*--|sleep\s*\()`)},
	{"CRS-002", "xss", 3, regexp.MustCompile(`(?i)(<script|javascript:|onerror\s*=|onload\s*=)`)},
	{"CRS-003", "traversal", 2, regexp.MustCompile(`(\.\./|\.\.\\|%2e%2e%2f)`)},
	{"CRS-004", "scanner", 1, regexp.MustCompile(`(?i)(sqlmap|nikto|nmap|acunetix)`)},
}

// Inspect returns the rule matches for a request.
// Middleware puts the WAF in front of a handler.
//
// The request is decoded before it is looked at, so an address that is
// written as %2e%2e%2f is caught as well.
func Middleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(writer http.ResponseWriter, request *http.Request) {
		findings := Inspect(Inspectable(request))
		if Blocked(findings) {
			writer.Header().Set("Content-Type", "text/plain; charset=utf-8")
			writer.WriteHeader(http.StatusForbidden)
			fmt.Fprintf(writer, "blocked by the WAF: %d finding(s)\n", len(findings))
			return
		}
		next.ServeHTTP(writer, request)
	})
}

// Inspectable turns an HTTP request into the request the firewall looks at.
//
// The escapes are decoded first, so an address that is written as
// %2e%2e%2f is caught as well.
func Inspectable(request *http.Request) Request {
	inspect := Request{Method: request.Method, Path: request.URL.Path}

	if request.URL.RawQuery != "" {
		inspect.Query = decodeOnce(request.URL.RawQuery)
	}
	if request.URL.RawPath != "" {
		inspect.Path = decodeOnce(request.URL.RawPath)
	}

	body := ""
	if request.Body != nil {
		raw, err := io.ReadAll(io.LimitReader(request.Body, 1<<20))
		if err == nil {
			body = string(raw)
		}
	}
	inspect.Body = decodeOnce(body)

	return inspect
}

// decodeOnce decodes the escapes of a text one time.
func decodeOnce(text string) string {
	decoded, err := url.PathUnescape(text)
	if err != nil {
		return text
	}
	return decoded
}

func Inspect(request Request) []Finding {
	targets := []string{request.Path, request.Query, request.Body}
	findings := []Finding{}
	for _, rule := range rules {
		for _, target := range targets {
			if match := rule.Pattern.FindString(target); match != "" && target != "" {
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

This lesson ties its explanation to `web/api_impl.py`, `waf.go`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
