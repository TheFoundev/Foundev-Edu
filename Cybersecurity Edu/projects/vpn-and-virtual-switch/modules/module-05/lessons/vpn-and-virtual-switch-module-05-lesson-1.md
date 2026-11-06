# A beginner's model of documented goals mapped to implementation

**Lesson ID:** `vpn-and-virtual-switch-module-05-lesson-1`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors main.go, vpn.go, web/api_impl.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `README.md`, `main.go`, `vpn.go`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `main.go`, `package main` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.go`, `import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `func main() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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

### README.md

```text
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
- There is no rekeying, replay window or compression.
- The virtual switch is a userspace map, not a kernel bridge.

## License

MIT. See `LICENSE`.

## About the scope

This is a third-year student project written in Go with the standard library only. It is not a hardened production service; the notes above list the missing pieces.

```

### main.go

```text
package main

import (
	"flag"
	"fmt"
	"net"
	"os"
)

func main() {
	secret :[REDACTED] flag.String("secret", "correct horse battery staple", "shared passphrase")
	message := flag.String("message", "hello from the tunnel", "payload to send")
	flag.Parse()

	key := DeriveKey(*secret)
	left, err := net.ListenPacket("udp", "127.0.0.1:0")
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	defer left.Close()
	right, err := net.ListenPacket("udp", "127.0.0.1:0")
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	defer right.Close()

	switching := NewSwitch()
	switching.Register(10, left, key)
	switching.Register(20, right, key)

	if err := switching.Send(Packet{Src: 10, Dst: 20, Payload: []byte(*message)}); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	packet, _, err := ReadFrom(right, key)
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	fmt.Printf("received %q from virtual ip %d\n", packet.Payload, packet.Src)
}

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

This lesson ties its explanation to `README.md`, `main.go`, `vpn.go`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
