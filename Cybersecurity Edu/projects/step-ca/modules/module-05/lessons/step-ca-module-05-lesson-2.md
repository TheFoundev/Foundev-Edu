# Read documented goals mapped to implementation in the source

**Lesson ID:** `step-ca-module-05-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors main.go, pki.go, web/api_impl.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `main.go`, `pki.go`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `main.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func main() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `pki.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `pki.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func serial() (*big.Int, error) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func NewAuthority(name string, names ...string) (*Authority, error) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func (authority *Authority) IssueCSR(csrPEM []byte) (*Leaf, error) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func (authority *Authority) maySign(commonName string) bool {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func (authority *Authority) Issue(commonName string, hosts []string) (*Leaf, error) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func (authority *Authority) Verify(certificate *x509.Certificate) error {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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

```

### main.go

```text
package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
	commonName := flag.String("cn", "service.internal", "leaf common name")
	output := flag.String("out", "artifacts", "output directory")
	flag.Parse()

	authority, err := NewAuthority("Foundev Student CA")
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	leaf, err := authority.Issue(*commonName, []string{*commonName, "localhost"})
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	if err := authority.Verify(leaf.Certificate); err != nil {
		fmt.Fprintln(os.Stderr, "verification failed:", err)
		os.Exit(1)
	}
	if err := authority.Save(*output, leaf); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	fmt.Printf("issued %s valid until %s\n", leaf.Certificate.Subject.CommonName, leaf.Certificate.NotAfter.Format("2006-01-02"))
}

```

### pki.go

```text
package main

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/x509"
	"crypto/x509/pkix"
	"encoding/pem"
	"fmt"
	"math/big"
	"os"
	"path/filepath"
	"strings"
	"time"
)

// Leaf bundles an issued certificate and its private key.
type Leaf struct {
	Certificate *x509.Certificate
	PrivateKey  *ecdsa.PrivateKey
}

// Authority is a simple root CA.
type Authority struct {
	Name        string
	Certificate *x509.Certificate
	PrivateKey  *ecdsa.PrivateKey
	// Names are the names the authority may sign for. A signing request
	// for anything else is refused.
	Names []string
}

func serial() (*big.Int, error) {
	limit := new(big.Int).Lsh(big.NewInt(1), 128)
	return rand.Int(rand.Reader, limit)
}

// NewAuthority creates a self-signed root with an ECDSA key.
func NewAuthority(name string, names ...string) (*Authority, error) {
	key, err := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	if err != nil {
		return nil, err
	}
	number, err := serial()
	if err != nil {
		return nil, err
	}
	template := &x509.Certificate{
		SerialNumber:          number,
		Subject:               pkix.Name{CommonName: name, Organization: []string{"Foundev Student Projects"}},
		NotBefore:             time.Now().Add(-time.Hour),
		NotAfter:              time.Now().AddDate(5, 0, 0),
		KeyUsage:              x509.KeyUsageCertSign | x509.KeyUsageDigitalSignature,
		BasicConstraintsValid: true,
		IsCA:                  true,
	}
	der, err := x509.CreateCertificate(rand.Reader, template, template, &key.PublicKey, key)
	if err != nil {
		return nil, err
	}
	certificate, err := x509.ParseCertificate(der)
	if err != nil {
		return nil, err
	}
	if len(names) == 0 {
		names = []string{name}
	}
	return &Authority{Name: name, Certificate: certificate, PrivateKey: [REDACTED], Names: names}, nil
}

// Issue creates a leaf certificate for a common name and SAN list.
// IssueCSR signs a certificate signing request.
//
// The request has to be checked: the name of the request has to be one the
// authority is allowed to sign, and the request has to be signed with a key
// the authority knows.
func (authority *Authority) IssueCSR(csrPEM []byte) (*Leaf, error) {
	block, _ := pem.Decode(csrPEM)
	if block == nil || block.Type != "CERTIFICATE REQUEST" {
		return nil, fmt.Errorf("the certificate signing request could not be read")
	}
	request, err := x509.ParseCertificateRequest(block.Bytes)
	if err != nil {
		return nil, fmt.Errorf("the certificate signing request is broken: %w", err)
	}
	if err := request.CheckSignature(); err != nil {
		return nil, fmt.Errorf("the certificate signing request is not signed: %w", err)
	}

	name := request.Subject.CommonName
	if !authority.maySign(name) {
		return nil, fmt.Errorf("the authority may not sign for %q", name)
	}

	hosts := request.DNSNames
	number, err := serial()
	if err != nil {
		return nil, err
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

This lesson ties its explanation to `README.md`, `main.go`, `pki.go`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
