# Read code review and safe change 6 in the source

**Lesson ID:** `naabu-module-06-lesson-2`

## Purpose and learning objectives

Use main.go to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `main.go`, `scanner.go`, `scanner_test.go`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `main.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func main() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `scanner.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `scanner.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func ParsePorts(spec string) ([]int, error) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func ParseHosts(spec string) ([]string, error) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func expandNetwork(spec string) ([]string, error) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func nextAddress(address net.IP) net.IP {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func Scan(host string, ports []int, timeout time.Duration) []PortResult {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func OpenPorts(results []PortResult) []int {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `scanner_test.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `scanner_test.go`, `import "testing"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func TestTheHostsOfAList(t *testing.T) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func TestANetworkIsExpanded(t *testing.T) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func TestABrokenNetworkIsRefused(t *testing.T) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func TestThePortsAreParsed(t *testing.T) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### scanner.go

```text
package main

import (
	"fmt"
	"net"
	"sort"
	"strconv"
	"strings"
	"sync"
	"time"
)

// DefaultTimeout is used when the caller does not set one.
const DefaultTimeout = 400 * time.Millisecond

// PortResult describes the outcome for one port.
type PortResult struct {
	Port  int    `json:"port"`
	State string `json:"state"`
}

// ParsePorts understands "22,80,1000-1005" syntax.
func ParsePorts(spec string) ([]int, error) {
	seen := map[int]bool{}
	for _, part := range strings.Split(spec, ",") {
		part = strings.TrimSpace(part)
		if part == "" {
			continue
		}
		if strings.Contains(part, "-") {
			bounds := strings.SplitN(part, "-", 2)
			start, err := strconv.Atoi(strings.TrimSpace(bounds[0]))
			if err != nil {
				return nil, fmt.Errorf("invalid port range %q", part)
			}
			end, err := strconv.Atoi(strings.TrimSpace(bounds[1]))
			if err != nil || end < start {
				return nil, fmt.Errorf("invalid port range %q", part)
			}
			for port := start; port <= end; port++ {
				if port >= 1 && port <= 65535 {
					seen[port] = true
				}
			}
			continue
		}
		port, err := strconv.Atoi(part)
		if err != nil || port < 1 || port > 65535 {
			return nil, fmt.Errorf("invalid port %q", part)
		}
		seen[port] = true
	}
	ports := make([]int, 0, len(seen))
	for port := range seen {
		ports = append(ports, port)
	}
	sort.Ints(ports)
	return ports, nil
}

// Scan dials each port concurrently.
// ParseHosts turns a list of hosts and network ranges into the hosts.
//
// A network is written as 10.0.0.0/24 and is expanded into its addresses.
func ParseHosts(spec string) ([]string, error) {
	hosts := []string{}
	for _, part := range strings.Split(spec, ",") {
		part = strings.TrimSpace(part)
		if part == "" {
			continue
		}
		if !strings.Contains(part, "/") {
			hosts = append(hosts, part)
			continue
		}
		expanded, err := expandNetwork(part)
		if err != nil {
			return nil, err
		}
		hosts = append(hosts, expanded...)
	}
	if len(hosts) == 0 {
		return nil, fmt.Errorf("no hosts to scan")
	}
	return hosts, nil
}

// expandNetwork turns a network into its addresses.
func expandNetwork(spec string) ([]string, error) {
	parts := strings.Split(spec, "/")
	if len(parts) != 2 {
		return nil, fmt.Errorf("%q is not a network", spec)
	}
	address := net.ParseIP(parts[0])
	if address == nil {
		return nil, fmt.Errorf("%q is not an address", parts[0])
	}
	bits, err := strconv.Atoi(parts[1])
	if err != nil || bits < 0 || bits > 32 {
		return nil, fmt.Errorf("%q is not a prefix", parts[1])
```

### scanner_test.go

```text
package main

import "testing"

func TestTheHostsOfAList(t *testing.T) {
	hosts, err := ParseHosts("127.0.0.1, 10.0.0.1")
	if err != nil {
		t.Fatal(err)
	}
	if len(hosts) != 2 {
		t.Fatalf("unexpected hosts %#v", hosts)
	}
}

func TestANetworkIsExpanded(t *testing.T) {
	hosts, err := ParseHosts("10.0.0.0/30")
	if err != nil {
		t.Fatal(err)
	}
	// A /30 network has four addresses.
	if len(hosts) != 4 {
		t.Fatalf("unexpected hosts %#v", hosts)
	}
	if hosts[0] != "10.0.0.0" {
		t.Fatalf("unexpected first host %q", hosts[0])
	}
}

func TestABrokenNetworkIsRefused(t *testing.T) {
	if _, err := ParseHosts("10.0.0.0/not a prefix"); err == nil {
		t.Fatal("expected an error for a broken prefix")
	}
	if _, err := ParseHosts("999.0.0.1/24"); err == nil {
		t.Fatal("expected an error for an address that does not exist")
	}
	if _, err := ParseHosts(""); err == nil {
		t.Fatal("expected an error for an empty list")
	}
}

func TestThePortsAreParsed(t *testing.T) {
	ports, err := ParsePorts("80,443,8000-8002")
	if err != nil {
		t.Fatal(err)
	}
	if len(ports) != 5 {
		t.Fatalf("unexpected ports %#v", ports)
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

This lesson ties its explanation to `main.go`, `scanner.go`, `scanner_test.go`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
