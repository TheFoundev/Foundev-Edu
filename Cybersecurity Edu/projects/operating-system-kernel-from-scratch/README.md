# Operating System Kernel From Scratch

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

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
- The host

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Multiboot header and 32-bit entry stub
- Freestanding string and memory helpers
- VGA text buffer helpers for colour and cell layout
- Host tests for the pure logic plus an optional boot image
- There is no memory manager, scheduler, interrupts or file system.
- The boot image target is best effort; it needs gcc -m32 and ld with elf_i386.
- The host tests only cover the pure helper functions.

The implementation inventory includes 15 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `the repository dependency/configuration files`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `Makefile`
- `README.md`
- `src/kernel.c`
- `src/kernel.h`
- `tests/test_main.c`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: tests/test_main.c. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
