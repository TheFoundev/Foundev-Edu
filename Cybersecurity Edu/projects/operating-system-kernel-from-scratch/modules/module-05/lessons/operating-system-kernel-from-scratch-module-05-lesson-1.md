# A beginner's model of documented goals mapped to implementation

**Lesson ID:** `operating-system-kernel-from-scratch-module-05-lesson-1`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors src/kernel.c, src/kernel.h, web/server.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `README.md`, `src/kernel.c`, `src/kernel.h`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/kernel.c`, `#include "kernel.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/kernel.h`, `#include <stddef.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/kernel.h`, `#include <stdint.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.

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
# Operating System Kernel from Scratch

A tiny x86 kernel with a multiboot entry point and text utilities.

> A from-scratch operating system tutorial that boots a kernel and implements basic drivers.

## Overview

An original, self-contained implementation of the **Operating System Kernel from Scratch** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Multiboot header and 32-bit entry stub
- Freestanding string and memory helpers
- VGA text buffer helpers for colour and cell layout
- Host tests for the pure logic plus an optional boot image

## Stack

`C; POSIX`
The CSV stack is C + POSIX. The freestanding image needs a 32-bit toolchain and GRUB to actually boot; the test target compiles the same kernel logic for the host so the checks run anywhere.

## Run

```bash
make
make test
make image  # optional, needs a 32-bit toolchain
```

## Structure

```text
operating-system-kernel-from-scratch/
├── src/kernel.c           freestanding helpers and kernel_main
├── src/kernel.h           kernel API
├── src/boot.S             multiboot entry stub
├── src/linker.ld          link script
├── tests/test_main.c      host tests
└── Makefile
```

## Testing

```bash
make test
```

4 tests (`make test`), up from 2: the string helpers, the memory helpers and the VGA helpers.


## Notes and limitations

- There is no memory manager, scheduler, interrupts or file system.
- The boot image target is best effort; it needs gcc -m32 and ld with elf_i386.
- The host tests only cover the pure helper functions.

## License

BSD-3-Clause. See `LICENSE`.

## About the scope

This is a third-year student project. The build and tests run locally with GCC; there is no portability work beyond the platforms named in the notes.

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

### src/kernel.h

```text
#ifndef KERNEL_H
#define KERNEL_H

#include <stddef.h>
#include <stdint.h>

size_t kstrlen(const char *text);
int kstrcmp(const char *left, const char *right);
void *kmemset(void *destination, int value, size_t count);
void *kmemcpy(void *destination, const void *source, size_t count);
uint8_t vga_color(uint8_t foreground, uint8_t background);
uint16_t vga_entry(char character, uint8_t color);
size_t vga_index(size_t row, size_t column);
void kernel_main(uint32_t magic, uint32_t address);

#endif

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

This lesson ties its explanation to `README.md`, `src/kernel.c`, `src/kernel.h`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
