# Read code review and safe change 6 in the source

**Lesson ID:** `memory-allocator-from-scratch-module-06-lesson-2`

## Purpose and learning objectives

Use src/allocator.c to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/allocator.c`, `src/allocator.h`, `src/main.c`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/allocator.c`, `#include "allocator.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/allocator.c`, `#include <stddef.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/allocator.c`, `#include <stdint.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/allocator.c`, `#include <string.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/allocator.c`, `#include <sys/mman.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/allocator.h`, `#include <stddef.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main.c`, `#include "allocator.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main.c`, `#include <stdio.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### src/main.c

```text
#include "allocator.h"

#include <stdio.h>

int main(void) {
    int *numbers = (int *)my_malloc(32 * sizeof(int));
    char *text = (char *)my_calloc(16, 1);
    size_t bytes = 0;
    size_t blocks = 0;
    int index;

    if (numbers == NULL || text == NULL) {
        fprintf(stderr, "allocation failed\n");
        return 1;
    }
    for (index = 0; index < 32; index++) {
        numbers[index] = index * index;
    }
    numbers = (int *)my_realloc(numbers, 64 * sizeof(int));
    for (index = 32; index < 64; index++) {
        numbers[index] = index;
    }
    for (index = 0; index < 16; index++) {
        if (text[index] != 0) {
            fprintf(stderr, "calloc did not zero memory\n");
            return 1;
        }
    }

    alloc_stats(&bytes, &blocks);
    printf("allocated %zu bytes in %zu blocks\n", bytes, blocks);
    printf("last value: %d\n", numbers[63]);

    my_free(numbers);
    my_free(text);
    alloc_stats(&bytes, &blocks);
    printf("after free: %zu bytes in %zu blocks\n", bytes, blocks);
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

This lesson ties its explanation to `src/allocator.c`, `src/allocator.h`, `src/main.c`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
