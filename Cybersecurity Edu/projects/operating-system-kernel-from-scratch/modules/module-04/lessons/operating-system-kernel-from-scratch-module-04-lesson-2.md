# Read runtime configuration connected to code in the source

**Lesson ID:** `operating-system-kernel-from-scratch-module-04-lesson-2`

## Purpose and learning objectives

Inspect the declared manifests .github/workflows/ci.yml, Makefile and trace the relevant package or setting into implementation file src/kernel.c. Separate a declaration from an imported, configured, or executed behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `.github/workflows/ci.yml`, `Makefile`, `src/kernel.c`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `.github/workflows/ci.yml` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `Makefile` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/kernel.c`, `#include "kernel.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.

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
CFLAGS ?= -std=gnu11 -Wall -Wextra -O2 -Isrc
LD ?= ld

TEST_BIN := build/tests

all: $(TEST_BIN)

build:
	mkdir -p build

test: $(TEST_BIN)
	$(TEST_BIN)

$(TEST_BIN): tests/test_main.c src/kernel.c | build
	$(CC) $(CFLAGS) $^ -o $@

# Best-effort freestanding image. Needs a 32-bit toolchain and GRUB to boot.
image: build/kernel.elf

build/boot.o: src/boot.S | build
	$(CC) -m32 -ffreestanding -c $< -o $@

build/kernel.o: src/kernel.c | build
	$(CC) -m32 -ffreestanding -fno-pic -fno-stack-protector -c $< -o $@

build/kernel.elf: build/boot.o build/kernel.o src/linker.ld
	$(LD) -m elf_i386 -T src/linker.ld -o $@ build/boot.o build/kernel.o

clean:
	rm -rf build

.PHONY: all test image clean

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

This lesson ties its explanation to `.github/workflows/ci.yml`, `Makefile`, `src/kernel.c`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
