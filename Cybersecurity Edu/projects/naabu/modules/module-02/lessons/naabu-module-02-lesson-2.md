# Read api impl and scanner in the source

**Lesson ID:** `naabu-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [web/api_impl.py] and [scanner.go]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include main, report, _sources, _build_helper, ParsePorts, ParseHosts, expandNetwork, nextAddress, Scan, OpenPorts; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `web/api_impl.py`, `scanner.go`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `web/api_impl.py`, `from __future__ import annotations` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import hashlib` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import ipaddress` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import shutil` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func main() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func report(answer map[string]any) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _sources() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _build_helper() -> Path | None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _run_helper(host: str, ports: str, timeout_ms: int) -> dict | None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _parse_ports(spec: str) -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `scanner.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `scanner.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func ParsePorts(spec string) ([]int, error) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func ParseHosts(spec string) ([]string, error) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func expandNetwork(spec string) ([]string, error) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func nextAddress(address net.IP) net.IP {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func Scan(host string, ports []int, timeout time.Duration) []PortResult {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func OpenPorts(results []PortResult) []int {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
"""The API of the port scanner: the ports of a spec and the state of every port.

The numbers come from the Go code of the project. A helper program is built
from the sources of the project (scanner.go, main.go and go.mod) with a
`main` that reads the ports with ParsePorts, the hosts with ParseHosts and
scans every host with Scan, which dials each port with net.DialTimeout. The
helper prints the answer as JSON.

When the Go toolchain is not installed, the same code is mirrored here:
ParsePorts and ParseHosts are read as they are written in scanner.go and the
ports are dialled with socket.create_connection and the same timeout, so a
port that accepts the connection is open and every other port is closed.
"""

from __future__ import annotations

import hashlib
import ipaddress
import json
import shutil
import socket
import subprocess
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(tempfile.gettempdir()) / "foundev-go-helpers"
GO = shutil.which("go")

#: How long an answer of the helper is reused.
TTL = 30.0

#: The host and the ports the command line uses, as main.go sets them.
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORTS = "22,80,443,8000-8010"

#: The timeout of a port, in milliseconds: DefaultTimeout of scanner.go.
DEFAULT_TIMEOUT_MS = 400

#: The helper program: it parses the spec and scans the hosts.
HELPER = r'''
package main

import (
	"encoding/json"
	"os"
	"time"
)

func main() {
	var input struct {
		Host      string `json:"host"`
		Ports     string `json:"ports"`
		TimeoutMS int    `json:"timeout_ms"`
	}
	if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {
		os.Exit(1)
	}

	ports, err := ParsePorts(input.Ports)
	if err != nil {
		report(map[string]any{"error": err.Error()})
		return
	}
	hosts, err := ParseHosts(input.Host)
	if err != nil {
		report(map[string]any{"error": err.Error()})
		return
	}

	timeout := time.Duration(input.TimeoutMS) * time.Millisecond
	if timeout <= 0 {
		timeout = DefaultTimeout
	}

	scans := []map[string]any{}
	open := []map[string]any{}
	closed := 0
	for _, host := range hosts {
		results := Scan(host, ports, timeout)
		scans = append(scans, map[string]any{"host": host, "results": results})
		for _, result := range results {
			if result.State == "open" {
				open = append(open, map[string]any{"host": host, "port": result.Port})
			} else {
				closed++
			}
		}
	}

	report(map[string]any{
		"ports":      ports,
		"hosts":      hosts,
		"scans":      scans,
		"open":       open,
		"closed":     closed,
		"timeout_ms": int(timeout / time.Millisecond),
	})
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

This lesson ties its explanation to `web/api_impl.py`, `scanner.go`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
