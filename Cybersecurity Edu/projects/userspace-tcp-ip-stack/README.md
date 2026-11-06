# Userspace Tcp Ip Stack

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Userspace TCP/IP Stack

Parse and build Ethernet, IPv4 and TCP headers in userspace.

> A small userspace TCP/IP stack written for learning how protocols are implemented end to end.

## Overview

An original, self-contained implementation of the **Userspace TCP/IP Stack** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Header parsing with length checks
- Internet checksum computation and verification
- Packet builder for IPv4 and TCP
- Loopback stack that maps ports to handlers

## Stack

`C; POSIX`
The CSV stack is C + POSIX. This build works on raw byte buffers and an in-process loopback; the TUN/TAP device is documented but not opened in tests.

## Run

```bash
make
./build/app
make test
```

## Structure

```text
userspace-tcp-ip-stack/
├── src/packet.c            header parsing and building
├── src/packet.h            structs and API
├── src/main.c              demo program
├── tests/test_main.c       unit tests
└── Makefile
```

## Testing

```bash
make test
```

6 tests (`make test`), up from 2: the checksum, the byte order helpers, the headers and a packet that is built.


## Notes and limitations

- There is no congestion control, retransmission or TCP state machine.
- The TUN device code is optional and needs root to run.
- Only IPv4 is supported.

## License

MIT. See `LICENSE`.

## About the scope

This is a third-year student project. The build and tests run locally with GCC; there is no portability work beyond the platforms nam

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Header parsing with length checks
- Internet checksum computation and verification
- Packet builder for IPv4 and TCP
- Loopback stack that maps ports to handlers
- There is no congestion control, retransmission or TCP state machine.
- The TUN device code is optional and needs root to run.
- Only IPv4 is supported.

The implementation inventory includes 14 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `the repository dependency/configuration files`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `Makefile`
- `README.md`
- `src/main.c`
- `src/packet.c`
- `src/packet.h`
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
