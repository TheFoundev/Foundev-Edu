# Read api impl and vpn in the source

**Lesson ID:** `vpn-and-virtual-switch-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [web/api_impl.py] and [vpn.go]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include main, DeriveKey, NewSalt, DeriveKeyWithSalt, pbkdf2Key, Encrypt, Decrypt, NewReplayGuard, Accept; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `web/api_impl.py`, `vpn.go`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `web/api_impl.py`, `from __future__ import annotations` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import hashlib` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import hmac` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func main() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _sources() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _build_helper() -> Path | None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _run_helper(messages: list) -> dict | None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class _TagError(Exception):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class _Aead:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `vpn.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `vpn.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func DeriveKey(secret string) []byte {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func NewSalt() []byte {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func DeriveKeyWithSalt(secret string, salt []byte) []byte {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func pbkdf2Key(password, salt []byte, iterations, length int) []byte {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func Encrypt(key, plaintext []byte, sequence uint64) ([]byte, error) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `func Decrypt(key, data []byte) ([]byte, uint64, error) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
"""The API of the tunnel: the peers of the switch, the packets and the key.

The numbers come from the Go code of the project. A helper program is built
from the sources of the project (vpn.go, main.go and go.mod) with a `main`
that derives the key with DeriveKeyWithSalt, opens two UDP sockets, registers
the two peers in a Switch, sends the messages of the plan through it, reads
them back with ReadFrom and shows what the ReplayGuard and the tag of the
AEAD refuse.

When the Go toolchain is not installed, the same code is mirrored in Python:
the key comes from the same PBKDF2 with the same salt, the packets are sealed
with AES-GCM and the replay guard and the tag check work the same way.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import shutil
import struct
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(tempfile.gettempdir()) / "foundev-go-helpers"
GO = shutil.which("go")

#: The passphrase of the demo of main.go.
PASSPHRASE = "correct horse battery staple"

#: The salt of the console. It is fixed so the console shows the same key
#: between two runs; the project uses a random salt on every machine.
SALT = hashlib.sha256(b"foundev-vpn-console").digest()[:16]

#: The messages that go through the tunnel, the first one is the demo of main.go.
DEFAULT_MESSAGES = [
    "hello from the tunnel",
    "the second frame",
    "the third frame",
]

#: The helper program: it derives the key, sends the packets and shows the
#: refusals of the replay guard and of the tag.
HELPER = r'''
package main

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"net"
	"os"
)

func main() {
	var input struct {
		Passphrase string   `json:"passphrase"`
		Salt       string   `json:"salt"`
		Messages   []string `json:"messages"`
	}
	if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {
		os.Exit(1)
	}
	salt, err := hex.DecodeString(input.Salt)
	if err != nil {
		os.Exit(1)
	}

	key := DeriveKeyWithSalt(input.Passphrase, salt)
	digest := sha256.Sum256(key)

	left, err := net.ListenPacket("udp", "127.0.0.1:0")
	if err != nil {
		os.Exit(1)
	}
	defer left.Close()
	right, err := net.ListenPacket("udp", "127.0.0.1:0")
	if err != nil {
		os.Exit(1)
	}
	defer right.Close()

	switching := NewSwitch()
	// The packets to the peer 20 leave the left socket and arrive at the
	// right one; the packets to the peer 10 take the other way.
	switching.RegisterAt(20, left, right.LocalAddr(), key)
	switching.RegisterAt(10, right, left.LocalAddr(), key)

	guard := NewReplayGuard()
	peers := []map[string]any{
		{"vip": 10, "role": "sender", "sent": 0, "received": 0},
		{"vip": 20, "role": "receiver", "sent": 0, "received": 0},
	}
	packets := []map[string]any{}
	guards := []map[string]any{}
	lastSealed := []byte{}
	lastSequence := uint64(0)
```

### vpn.go

```text
package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/hmac"
	"crypto/rand"
	"crypto/sha256"
	"encoding/binary"
	"errors"
	"net"
	"sync"
)

// The parameters of the key derivation.
const (
	// SaltSize is the length of the salt.
	SaltSize = 16
	// DerivationIterations is how often the passphrase is hashed.
	DerivationIterations = 120000
)

// Packet is one tunnelled frame.
type Packet struct {
	Src     uint32
	Dst     uint32
	Payload []byte
}

// DeriveKey turns a passphrase into a 32-byte AES key.
//
// The key is derived with PBKDF2 and a random salt, so the same passphrase
// gives a different key on every machine and a dictionary of passphrases does
// not help against the stored key.
func DeriveKey(secret string) []byte {
	return DeriveKeyWithSalt(secret, NewSalt())
}

// NewSalt returns a new random salt.
func NewSalt() []byte {
	salt := make([]byte, SaltSize)
	if _, err := rand.Read(salt); err != nil {
		return make([]byte, SaltSize)
	}
	return salt
}

// DeriveKeyWithSalt turns a passphrase and a salt into a 32-byte AES key.
func DeriveKeyWithSalt(secret string, salt []byte) []byte {
	return pbkdf2Key([]byte(secret), salt, DerivationIterations, 32)
}

// pbkdf2Key is PBKDF2 with HMAC-SHA256.
func pbkdf2Key(password, salt []byte, iterations, length int) []byte {
	blocks := (length + 31) / 32
	result := make([]byte, 0, blocks*32)
	for block := 1; block <= blocks; block++ {
		mac := hmac.New(sha256.New, password)
		mac.Write(salt)
		mac.Write([]byte{byte(block >> 24), byte(block >> 16), byte(block >> 8), byte(block)})
		current := mac.Sum(nil)
		result = append(result, current...)
		for round := 1; round < iterations; round++ {
			mac.Reset()
			mac.Write(current)
			current = mac.Sum(nil)
			for index := range current {
				result[(block-1)*32+index] ^= current[index]
			}
		}
	}
	return result[:length]
}

// Encrypt seals a plaintext with AES-GCM and a random nonce.
//
// The nonce is written in front of the sealed text, and the sequence number
// is added to the data that is authenticated, so a packet cannot be replayed.
func Encrypt(key, plaintext []byte, sequence uint64) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	aead, err := cipher.NewGCM(block)
	if err != nil {
		return nil, err
	}
	nonce := make([]byte, aead.NonceSize())
	if _, err := rand.Read(nonce); err != nil {
		return nil, err
	}

	header := make([]byte, 8)
	binary.BigEndian.PutUint64(header, sequence)

	sealed := aead.Seal(nil, nonce, plaintext, header)
	return append(append(nonce, header...), sealed...), nil
}

// Decrypt opens a sealed buffer and says which sequence number it had.
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

This lesson ties its explanation to `web/api_impl.py`, `vpn.go`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
