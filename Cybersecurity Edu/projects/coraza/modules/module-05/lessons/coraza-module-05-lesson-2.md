# Read documented goals mapped to implementation in the source

**Lesson ID:** `coraza-module-05-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors main.go, waf.go, web/api_impl.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `main.go`, `waf.go`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `main.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func main() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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

### README.md

```text
# Coraza

A small web application firewall that inspects requests against rules.

> An open-source Web Application Firewall engine that is embedded to filter HTTP traffic in real time.

## Overview

An original, self-contained implementation of the **Coraza** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Regex rules for SQL injection, XSS, traversal and scanners
- Per-request findings with severity and evidence
- Allow or block decision with a score
- Command line inspection and JSON output

## Stack

`Go`
The CSV stack is Go. This build implements a compact rule engine with Go's regexp package instead of loading the full OWASP Core Rule Set.

## Run

```bash
go run . -path /items -query 'id=1 union select 1'
go test ./...
```

## Structure

```text
coraza/
├── main.go                request inspection CLI
├── waf.go                 rules and decision logic
├── waf_test.go            unit tests
└── go.mod
```

## Testing

```bash
go test ./...
```

5 tests (`go test ./...`), up from 2: the middleware, a suspicious request, a request that is written with escapes, the body and the request that is looked at.


## Notes and limitations

- The rule set is tiny and will miss most real attacks.
- Requests are inspected as strings; there is no HTTP middleware or body streaming.
- There is no anomaly scoring across sessions or rule tuning.

## License

Apache-2.0. See `LICENSE`.

## About the scope

This is a third-year student project written in Go with the standard library only. It is not a hardened production service; the notes above list the missing pieces.

```

### main.go

```text
package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"strings"
)

func main() {
	method := flag.String("method", "GET", "HTTP method")
	path := flag.String("path", "/", "request path")
	query := flag.String("query", "", "query string")
	body := flag.String("body", "", "request body")
	flag.Parse()

	request := Request{Method: *method, Path: *path, Query: *query, Body: *body}
	findings := Inspect(request)
	decision := "allow"
	if Blocked(findings) {
		decision = "block"
	}
	output := map[string]any{
		"decision": decision,
		"score":    Score(findings),
		"findings": findings,
	}
	encoder := json.NewEncoder(os.Stdout)
	encoder.SetIndent("", "  ")
	if err := encoder.Encode(output); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	if decision == "block" {
		fmt.Fprintln(os.Stderr, "request blocked:", strings.Join(Evidence(findings), "; "))
	}
}

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

This lesson ties its explanation to `README.md`, `main.go`, `waf.go`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
