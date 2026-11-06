# Architecture and source map

## Repository evidence

- `.github/workflows/ci.yml`
- `Makefile`
- `README.md`
- `src/kernel.c`
- `src/kernel.h`
- `tests/test_main.c`
- `web/assets/app.js`
- `web/server.py`

## Reading path

Start with the README, then identify entry points and trace calls into reusable modules. Inspect inputs and outputs at each boundary, then compare tests and configuration. Filenames suggest roles but do not prove execution order.

## Documentation versus implementation

README excerpt for comparison (truncated to 8,000 characters):

> # Operating System Kernel from Scratch
> 
> A tiny x86 kernel with a multiboot entry point and text utilities.
> 
> > A from-scratch operating system tutorial that boots a kernel and implements basic drivers.
> 
> ## Overview
> 
> An original, self-contained implementation of the **Operating System Kernel from Scratch** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.
> 
> ## Features
> 
> - Multiboot header and 32-bit entry stub
> - Freestanding string and memory helpers
> - VGA text buffer helpers for colour and cell layout
> - Host tests for the pure logic plus an optional boot image
> 
> ## Stack
> 
> `C; POSIX`
> The CSV stack is C + POSIX. The freestanding image needs a 32-bit toolchain and GRUB to actually boot; the test target compiles the same kernel logic for the host so the checks run anywhere.
> 
> ## Run
> 
> ```bash
> make
> make test
> make image  # optional, needs a 32-bit toolchain
> ```
> 
> ## Structure
> 
> ```text
> operating-system-kernel-from-scratch/
> ├── src/kernel.c           freestanding helpers and kernel_main
> ├── src/kernel.h           kernel API
> ├── src/boot.S             multiboot entry stub
> ├── src/linker.ld          link script
> ├── tests/test_main.c      host tests
> └── Makefile
> ```
> 
> ## Testing
> 
> ```bash
> make test
> ```
> 
> 4 tests (`make test`), up from 2: the string helpers, the memory helpers and the VGA helpers.
> 
> 
> ## Notes and limitations
> 
> - There is no memory manager, scheduler, interrupts or file system.
> - The boot image target is best effort; it needs gcc -m32 and ld with elf_i386.
> - The host tests only cover the pure helper functions.
> 
> ## License
> 
> BSD-3-Clause. See `LICENSE`.
> 
> ## About the scope
> 
> This is a third-year student project. The build and tests run locally with GCC; there is no portability work beyond the platforms named in the notes.
> 

Treat these statements as claims. Confirm each against implementation. This package does not assert that every README feature exists, any test passes, or external integrations are live.
