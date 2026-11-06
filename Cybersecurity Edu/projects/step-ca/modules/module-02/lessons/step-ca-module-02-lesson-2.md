# Read api impl and pki in the source

**Lesson ID:** `step-ca-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [web/api_impl.py] and [pki.go]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include main, serial, NewAuthority, IssueCSR, maySign; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `web/api_impl.py`, `pki.go`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `web/api_impl.py`, `from __future__ import annotations` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import hashlib` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import shutil` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import subprocess` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func main() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func describeAuthority(authority *Authority) map[string]any {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func describe(certificate *x509.Certificate, hosts []string, authority *Authority) map[string]any {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func keyUsage(usage x509.KeyUsage) string {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func extKeyUsage(usages []x509.ExtKeyUsage) string {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func makeRequest(commonName string, hosts []string) ([]byte, *ecdsa.PrivateKey, error) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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

### web/api_impl.py

```text
"""The API of the certificate authority: the root, the leaves and the requests.

The numbers come from the Go code of the project. A helper program is built
from the sources of the project (pki.go, main.go and go.mod) with a `main`
that makes the root with NewAuthority, issues the leaves with Issue, signs the
requests with IssueCSR and checks every chain with Verify. The PEM files are
written with Save, the way the demo of main.go writes them. When the Go
toolchain is not installed, the same code is mirrored in Python with the
cryptography library. The answer of the last run is kept in the cache, so the
console shows the same certificates either way.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(tempfile.gettempdir()) / "foundev-go-helpers"
GO = shutil.which("go")

#: Where the certificates of the console are written, next to the ones of the demo.
ARTIFACTS = ROOT / "artifacts" / "console"

#: The root of the console and the names it may sign for.
AUTHORITY = "Foundev Student CA"
NAMES = ["internal", "localhost"]

#: The leaves and the requests of the demo: the certificate of main.go, the
#: leaf of the api and the request that the root refuses.
SEED_CERTIFICATES = [
    {"common_name": "service.internal", "hosts": ["service.internal", "localhost"]},
    {"common_name": "api.internal", "hosts": ["api.internal"]},
]
SEED_REQUESTS = [
    {"common_name": "api.internal", "hosts": ["api.internal"]},
    {"common_name": "evil.com", "hosts": ["evil.com"]},
]

#: The helper program: it makes the root, issues the leaves and signs the requests.
HELPER = r'''
package main

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/x509"
	"crypto/x509/pkix"
	"encoding/json"
	"encoding/pem"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

type request struct {
	CommonName string   `json:"common_name"`
	Hosts      []string `json:"hosts"`
}

func main() {
	var input struct {
		Authority    string    `json:"authority"`
		Names        []string  `json:"names"`
		Artifacts    string    `json:"artifacts"`
		Certificates []request `json:"certificates"`
		Requests     []request `json:"requests"`
	}
	if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {
		fail(err)
	}

	authority, err := NewAuthority(input.Authority, input.Names...)
	if err != nil {
		fail(err)
	}

	directory := input.Artifacts
	if directory != "" {
		if err := os.MkdirAll(directory, 0o755); err != nil {
			fail(err)
		}
		writeKey(filepath.Join(directory, "ca.key"), authority.PrivateKey)
	}

	certificates := []map[string]any{}
	for index, item := range input.Certificates {
		leaf, err := authority.Issue(item.CommonName, item.Hosts)
		if err != nil {
			fail(err)
		}
		if directory != "" {
			if index == 0 {
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

This lesson ties its explanation to `web/api_impl.py`, `pki.go`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
