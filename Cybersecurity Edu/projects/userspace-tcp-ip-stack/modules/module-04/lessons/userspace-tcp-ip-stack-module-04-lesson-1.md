# A beginner's model of runtime configuration connected to code

**Lesson ID:** `userspace-tcp-ip-stack-module-04-lesson-1`

## Purpose and learning objectives

Inspect the declared manifests .github/workflows/ci.yml, Makefile and trace the relevant package or setting into implementation file src/main.c. Separate a declaration from an imported, configured, or executed behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `.github/workflows/ci.yml`, `Makefile`, `src/main.c`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- The excerpt from `.github/workflows/ci.yml` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `Makefile` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/main.c`, `#include "packet.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main.c`, `#include <stdio.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.

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
      - name: Build
        run: make
      - name: Run the tests
        run: make test

```

### Makefile

```text
CC ?= gcc
CXX ?= g++
CFLAGS ?= -std=c11 -Wall -Wextra -O2 -Isrc
CXXFLAGS ?= -std=c++17 -Wall -Wextra -O2 -Isrc

TEST_BIN := build/tests
SRC := $(wildcard src/*.c)
OBJ := $(patsubst src/%.c,build/%.o,$(SRC))

all: build/app

build:
	mkdir -p build

build/%.o: src/%.c | build
	$(CC) $(CFLAGS) -c $< -o $@

build/app: $(OBJ) | build
	$(CC) $(CFLAGS) $(OBJ) -o $@

test: $(TEST_BIN)
	$(TEST_BIN)

$(TEST_BIN): tests/test_main.c $(filter-out build/main.o,$(OBJ)) | build
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm -rf build

.PHONY: all test clean

```

### src/main.c

```text
#include "packet.h"

#include <stdio.h>

int main(void) {
    uint8_t buffer[256];
    ipv4_header_t ip;
    tcp_header_t tcp;
    size_t total;
    const char *payload = "hello";

    total = packet_build_ipv4_tcp(buffer, sizeof(buffer), 0x0a000001u, 0x0a000002u,
                                  12345, 80, (const uint8_t *)payload, 5);
    printf("built %zu bytes\n", total);
    if (packet_parse_ipv4(buffer, total, &ip) == 0) {
        fprintf(stderr, "bad ip header\n");
        return 1;
    }
    if (packet_parse_tcp(buffer + IPV4_HEADER, total - IPV4_HEADER, &tcp) == 0) {
        fprintf(stderr, "bad tcp header\n");
        return 1;
    }
    printf("ip ttl=%u protocol=%u checksum=0x%04x\n", ip.ttl, ip.protocol, ip.checksum);
    printf("tcp %u -> %u flags=0x%02x\n", tcp.source_port, tcp.destination_port, tcp.flags);
    printf("ipv4 checksum valid: %s\n", packet_checksum(buffer, IPV4_HEADER) == 0 ? "yes" : "no");
    return 0;
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

This lesson ties its explanation to `.github/workflows/ci.yml`, `Makefile`, `src/main.c`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
