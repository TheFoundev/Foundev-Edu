# A beginner's model of test code and implementation evidence

**Lesson ID:** `memory-allocator-from-scratch-module-03-lesson-1`

## Purpose and learning objectives

Read the test cases in tests/test_main.c beside the implementation in src/main.c. Explain the behavior asserted by the tests and trace each assertion to the implementation. A test file describes a check; it does not prove that check passed.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `tests/test_main.c`, `src/main.c`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `tests/test_main.c`, `#include <assert.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_main.c`, `#include <stdint.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_main.c`, `#include <stdio.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_main.c`, `#include <string.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_main.c`, `#include "../src/allocator.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
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

### tests/test_main.c

```text
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "../src/allocator.h"

static void test_malloc_and_free(void) {
    void *pointer = my_malloc(64);
    assert(pointer != NULL);
    memset(pointer, 'x', 64);

    size_t bytes = 0;
    size_t blocks = 0;
    alloc_stats(&bytes, &blocks);
    assert(bytes >= 64);
    assert(blocks >= 1);

    my_free(pointer);
    alloc_stats(&bytes, &blocks);
    assert(blocks == 0);
}

static void test_calloc_is_zeroed(void) {
    unsigned char *pointer = (unsigned char *)my_calloc(16, 4);
    assert(pointer != NULL);
    for (int i = 0; i < 64; i++) {
        assert(pointer[i] == 0);
    }
    my_free(pointer);
}

static void test_realloc_keeps_the_data(void) {
    char *pointer = (char *)my_malloc(16);
    assert(pointer != NULL);
    memcpy(pointer, "hello", 6);

    char *bigger = (char *)my_realloc(pointer, 64);
    assert(bigger != NULL);
    assert(strncmp(bigger, "hello", 6) == 0);
    my_free(bigger);
}

static void test_the_arena_is_used_up(void) {
    // The arena is finite, so asking for a lot has to fail at some point.
    void *pointers[4096];
    int taken = 0;
    for (int i = 0; i < 4096; i++) {
        pointers[i] = my_malloc(64 * 1024);
        if (pointers[i] == NULL) {
            break;
        }
        taken++;
    }
    assert(taken < 4096);
    for (int i = 0; i < taken; i++) {
        my_free(pointers[i]);
    }
}

static void test_free_of_null_is_safe(void) {
    my_free(NULL);
}

int main(void) {
    test_malloc_and_free();
    test_calloc_is_zeroed();
    test_realloc_keeps_the_data();
    test_the_arena_is_used_up();
    test_free_of_null_is_safe();
    printf("all allocator tests passed\n");
    return 0;
}

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

This lesson ties its explanation to `tests/test_main.c`, `src/main.c`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
