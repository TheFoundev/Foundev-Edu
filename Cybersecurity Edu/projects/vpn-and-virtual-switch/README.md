# Vpn And Virtual Switch

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# VPN and Virtual Switch

A UDP tunnel with AES-GCM packets and a virtual switch.

> A tutorial that builds a Layer 2 virtual switch and VPN overlay similar to ZeroTier.

## Overview

An original, self-contained implementation of the **VPN and Virtual Switch** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- The key is derived with PBKDF2 and a random salt, so the same passphrase
  gives a different key on every machine
- Every packet carries a sequence number that is authenticated with the
  ciphertext, and a replay guard refuses a packet that was seen before or
  that is older than the last one
- A packet that was changed on the way is refused by the AEAD tag
- The switch routes the packets between the peers

## Stack

`Go`
The CSV stack is Go. This build implements the tunnel and switch in Go over real UDP sockets; there is no TUN device, routing table or C data path.

## Run

```bash
go run . -message hello
go test ./...
```

## Structure

```text
vpn-and-virtual-switch/
├── main.go                tunnel demo
├── vpn.go                 encryption and switch
├── vpn_test.go            unit tests
└── go.mod
```

## Testing

```bash
go test ./...
```

6 tests: the key derivation with a salt, the sequence number of a packet, a
packet that was tampered with, a replay that is refused and the switch that
forwards a packet.

## Notes and limitations

- Keys are derived from a shared passphrase instead of a handshake.
- There is no rekeying, replay

## Actual features and limits

README feature statements (verify each against code before relying on it):
- The key is derived with PBKDF2 and a random salt, so the same passphrase
- Every packet carries a sequence number that is authenticated with the
- A packet that was changed on the way is refused by the AEAD tag
- The switch routes the packets between the peers
- Keys are derived from a shared passphrase instead of a handshake.
- There is no rekeying, replay window or compression.
- The virtual switch is a userspace map, not a kernel bridge.

The implementation inventory includes 15 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `go.mod`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `go.mod`
- `main.go`
- `vpn.go`
- `vpn_test.go`
- `web/api_impl.py`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: vpn_test.go. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
