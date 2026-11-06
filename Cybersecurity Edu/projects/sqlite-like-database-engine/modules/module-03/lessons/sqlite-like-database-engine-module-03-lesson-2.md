# Read test code and implementation evidence in the source

**Lesson ID:** `sqlite-like-database-engine-module-03-lesson-2`

## Purpose and learning objectives

Read the test cases in tests/test_main.c beside the implementation in src/main.c. Explain the behavior asserted by the tests and trace each assertion to the implementation. A test file describes a check; it does not prove that check passed.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `tests/test_main.c`, `src/main.c`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `tests/test_main.c`, `#include <assert.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_main.c`, `#include <stdio.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_main.c`, `#include <string.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_main.c`, `#include "../src/db.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main.c`, `#include "db.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main.c`, `#include <stdio.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main.c`, `#include <string.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.

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
#include <stdio.h>
#include <string.h>

#include "../src/db.h"

static void test_put_and_get(void) {
    db_t *db = db_open(":memory:");
    assert(db != NULL);

    assert(db_put(db, "greeting", "hello world") == 1);

    const char *found = db_get(db, "greeting");
    assert(found != NULL);
    assert(strcmp(found, "hello world") == 0);
    assert(db_count(db) == 1);

    db_close(db);
}

static void test_delete(void) {
    db_t *db = db_open(":memory:");
    assert(db != NULL);

    assert(db_put(db, "key", "value") == 1);
    assert(db_delete(db, "key") == 1);
    assert(db_get(db, "key") == NULL);
    assert(db_count(db) == 0);

    db_close(db);
}

static void test_a_key_that_is_not_there(void) {
    db_t *db = db_open(":memory:");
    assert(db != NULL);
    assert(db_get(db, "nope") == NULL);
    db_close(db);
}

static void test_the_database_is_written_and_read_back(void) {
    const char *path = "build/test-database.bin";
    remove(path);

    db_t *db = db_open(path);
    assert(db != NULL);
    assert(db_put(db, "answer", "42") == 1);
    assert(db_save(db) == 1);
    db_close(db);

    db_t *again = db_open(path);
    assert(again != NULL);
    const char *found = db_get(again, "answer");
    assert(found != NULL);
    assert(strcmp(found, "42") == 0);
    db_close(again);

    remove(path);
}

int main(void) {
    test_put_and_get();
    test_delete();
    test_a_key_that_is_not_there();
    test_the_database_is_written_and_read_back();
    printf("all database tests passed\n");
    return 0;
}

```

### src/main.c

```text
#include "db.h"

#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    const char *path = argc > 1 ? argv[1] : "demo.db";
    db_t *database = db_open(path);
    if (database == NULL) {
        fprintf(stderr, "could not open %s\n", path);
        return 1;
    }
    if (argc > 3 && strcmp(argv[2], "put") == 0) {
        db_put(database, argv[3], argc > 4 ? argv[4] : "");
        db_save(database);
        printf("stored %s\n", argv[3]);
    } else if (argc > 3 && strcmp(argv[2], "get") == 0) {
        const char *value = db_get(database, argv[3]);
        printf("%s\n", value != NULL ? value : "(not found)");
    } else if (argc > 3 && strcmp(argv[2], "delete") == 0) {
        printf("%s\n", db_delete(database, argv[3]) ? "deleted" : "missing");
        db_save(database);
    } else {
        db_put(database, "name", "foundev");
        db_put(database, "kind", "student database");
        db_put(database, "pages", "array index");
        db_save(database);
        printf("record count: %zu\n", db_count(database));
        db_dump(database);
    }
    db_close(database);
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
