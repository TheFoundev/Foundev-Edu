# Step Ca

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# step-ca

A tiny certificate authority that issues and verifies leaf certificates.

> A private certificate authority and ACME server for issuing short-lived certificates inside a zero-trust network.

## Overview

An original, self-contained implementation of the **step-ca** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- ECDSA root and intermediate certificates
- CSR based leaf issuance with SAN and validity
- Certificate chain verification
- PEM files for the CA and issued certificate

## Stack

`Go`
The CSV stack is Go. This build implements the PKI flow with crypto/x509; there is no ACME server, provisioner database or certificate revocation.

## Run

```bash
go run . -cn service.internal
go test ./...
```

## Structure

```text
step-ca/
├── main.go                issue a certificate from the CLI
├── pki.go                 CA and issuance logic
├── pki_test.go            unit tests
└── go.mod
```

## Testing

```bash
# see the Run section
```

## Notes and limitations

- Private keys are written to local PEM files in the demo.
- There is no revocation list, OCSP responder or HSM backing.
- Only ECDSA P-256 keys are supported.

## License

Apache-2.0. See `LICENSE`.

## About the scope

This is a third-year student project written in Go with the standard library only. It is not a hardened production service; the notes above list the missing pieces.

## Actual features and limits

README feature statements (verify each against code before relying on it):
- ECDSA root and intermediate certificates
- CSR based leaf issuance with SAN and validity
- Certificate chain verification
- PEM files for the CA and issued certificate
- Private keys are written to local PEM files in the demo.
- There is no revocation list, OCSP responder or HSM backing.
- Only ECDSA P-256 keys are supported.

The implementation inventory includes 31 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `go.mod`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `go.mod`
- `main.go`
- `pki.go`
- `pki_test.go`
- `web/api_impl.py`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: pki_test.go. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
