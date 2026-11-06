# Read documented goals mapped to implementation in the source

**Lesson ID:** `memory-allocator-from-scratch-module-05-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors src/allocator.c, src/allocator.h, src/main.c. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `src/allocator.c`, `src/allocator.h`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/allocator.c`, `#include "allocator.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/allocator.c`, `#include <stddef.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/allocator.c`, `#include <stdint.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/allocator.c`, `#include <string.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/allocator.c`, `#include <sys/mman.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/allocator.h`, `#include <stddef.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.

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
# Memory Allocator from Scratch

A malloc replacement built on mmap with a coalescing free list.

> A thread-safe malloc/free replacement in C that demonstrates free-list design and fragmentation handling.

## Overview

An original, self-contained implementation of the **Memory Allocator from Scratch** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Single mmap arena with 16-byte alignment
- First-fit allocation and block splitting
- Coalescing free list to limit fragmentation
- realloc, calloc and allocation statistics

## Stack

`C; POSIX`
The CSV stack is C + POSIX. This build implements the allocator with mmap and a free list; there is no thread-local cache or arena per thread.

## Run

```bash
make
./build/app
make test
```

## Structure

```text
memory-allocator-from-scratch/
├── src/allocator.c        mmap allocator implementation
├── src/allocator.h        public API
├── src/main.c             demo program
├── tests/test_main.c      unit tests
└── Makefile
```

## Testing

```bash
make test
```

5 tests (`make test`), up from 2: the allocation, the zeroed memory, the reallocation, the end of the arena and the free of nothing.


## Notes and limitations

- The arena is fixed at four megabytes and never grows.
- There is no locking, so it is not safe across threads.
- Fragmentation handling is a simple first fit with coalescing.

## License

MIT. See `LICENSE`.

## About the scope

This is a third-year student project. The build and tests run locally with GCC; there is no portability work beyond the platforms named in the notes.

```

### src/allocator.c

```text
#include "allocator.h"

#include <stddef.h>
#include <stdint.h>
#include <string.h>
#include <sys/mman.h>

#define ARENA_BYTES (4u * 1024u * 1024u)

typedef struct block {
    size_t size;
    int free;
    struct block *next;
    struct block *prev;
} block_t;

#define HEADER_SIZE (((sizeof(block_t)) + 15u) & ~((size_t)15u))

static unsigned char *arena = NULL;
static block_t *first = NULL;
static size_t used_bytes = 0;
static size_t used_blocks = 0;

static void ensure_arena(void) {
    void *memory;
    if (arena != NULL) {
        return;
    }
    memory = mmap(NULL, ARENA_BYTES, PROT_READ | PROT_WRITE,
                  MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (memory == MAP_FAILED) {
        arena = NULL;
        return;
    }
    arena = (unsigned char *)memory;
    first = (block_t *)arena;
    first->size = ARENA_BYTES - HEADER_SIZE;
    first->free = 1;
    first->next = NULL;
    first->prev = NULL;
}

static void *payload(block_t *block) {
    return (void *)((unsigned char *)block + HEADER_SIZE);
}

static block_t *header(void *pointer) {
    return (block_t *)((unsigned char *)pointer - HEADER_SIZE);
}

static void split(block_t *block, size_t size) {
    block_t *rest;
    if (block->size < size + HEADER_SIZE + 16u) {
        return;
    }
    rest = (block_t *)((unsigned char *)payload(block) + size);
    rest->size = block->size - size - HEADER_SIZE;
    rest->free = 1;
    rest->next = block->next;
    rest->prev = block;
    if (rest->next != NULL) {
        rest->next->prev = rest;
    }
    block->next = rest;
    block->size = size;
}

void *my_malloc(size_t size) {
    block_t *block;
    if (size == 0) {
        return NULL;
    }
    ensure_arena();
    if (first == NULL) {
        return NULL;
    }
    size = (size + 15u) & ~((size_t)15u);
    for (block = first; block != NULL; block = block->next) {
        if (block->free && block->size >= size) {
            split(block, size);
            block->free = 0;
            used_bytes += block->size;
            used_blocks++;
            return payload(block);
        }
    }
    return NULL;
}

void *my_calloc(size_t count, size_t size) {
    size_t total = count * size;
    void *memory = my_malloc(total);
    if (memory != NULL) {
        memset(memory, 0, total);
    }
    return memory;
}

static void coalesce(block_t *block) {
    if (block->next != NULL && block->next->free) {
```

### src/allocator.h

```text
#ifndef ALLOCATOR_H
#define ALLOCATOR_H

#include <stddef.h>

void *my_malloc(size_t size);
void *my_calloc(size_t count, size_t size);
void *my_realloc(void *pointer, size_t size);
void my_free(void *pointer);
void alloc_stats(size_t *bytes_in_use, size_t *blocks);

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

This lesson ties its explanation to `README.md`, `src/allocator.c`, `src/allocator.h`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
