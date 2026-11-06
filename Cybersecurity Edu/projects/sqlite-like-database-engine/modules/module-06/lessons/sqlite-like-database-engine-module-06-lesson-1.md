# A beginner's model of code review and safe change 6

**Lesson ID:** `sqlite-like-database-engine-module-06-lesson-1`

## Purpose and learning objectives

Use src/db.c to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/db.c`, `src/db.h`, `src/main.c`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/db.c`, `#include "db.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/db.c`, `#include <stdio.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/db.c`, `#include <stdlib.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/db.c`, `#include <string.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/db.h`, `#include <stddef.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
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

### src/db.c

```text
#define _POSIX_C_SOURCE 200809L

#include "db.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct entry {
    char *key;
    char *value;
};

struct db {
    char *path;
    struct entry *entries;
    size_t count;
    size_t capacity;
};

static long find_index(db_t *database, const char *key) {
    size_t low = 0;
    size_t high = database->count;
    while (low < high) {
        size_t middle = (low + high) / 2;
        int comparison = strcmp(database->entries[middle].key, key);
        if (comparison == 0) {
            return (long)middle;
        }
        if (comparison < 0) {
            low = middle + 1;
        } else {
            high = middle;
        }
    }
    return (long)low;
}

static int ensure_capacity(db_t *database) {
    if (database->count < database->capacity) {
        return 1;
    }
    size_t next = database->capacity == 0 ? 8 : database->capacity * 2;
    struct entry *grown = (struct entry *)realloc(database->entries, next * sizeof(struct entry));
    if (grown == NULL) {
        return 0;
    }
    database->entries = grown;
    database->capacity = next;
    return 1;
}

db_t *db_open(const char *path) {
    db_t *database = (db_t *)calloc(1, sizeof(db_t));
    FILE *file;
    unsigned int count = 0;
    unsigned int index;
    if (database == NULL) {
        return NULL;
    }
    database->path = strdup(path);
    file = fopen(path, "rb");
    if (file == NULL) {
        return database;
    }
    if (fread(&count, sizeof(count), 1, file) != 1) {
        fclose(file);
        return database;
    }
    for (index = 0; index < count; index++) {
        unsigned int key_length = 0;
        unsigned int value_length = 0;
        char *key;
        char *value;
        if (fread(&key_length, sizeof(key_length), 1, file) != 1 ||
            fread(&value_length, sizeof(value_length), 1, file) != 1) {
            break;
        }
        key = (char *)malloc(key_length + 1u);
        value = (char *)malloc(value_length + 1u);
        if (key == NULL || value == NULL) {
            free(key);
            free(value);
            break;
        }
        if (fread(key, 1, key_length, file) != key_length ||
            fread(value, 1, value_length, file) != value_length) {
            free(key);
            free(value);
            break;
        }
        key[key_length] = '\0';
        value[value_length] = '\0';
        if (!ensure_capacity(database)) {
            free(key);
            free(value);
            break;
        }
        database->entries[database->count].key = key;
        database->entries[database->count].value = value;
```

### src/db.h

```text
#ifndef DB_H
#define DB_H

#include <stddef.h>

typedef struct db db_t;

db_t *db_open(const char *path);
void db_close(db_t *database);
int db_put(db_t *database, const char *key, const char *value);
const char *db_get(db_t *database, const char *key);
int db_delete(db_t *database, const char *key);
size_t db_count(db_t *database);
int db_save(db_t *database);
int db_dump(db_t *database);

#endif

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

This lesson ties its explanation to `src/db.c`, `src/db.h`, `src/main.c`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
