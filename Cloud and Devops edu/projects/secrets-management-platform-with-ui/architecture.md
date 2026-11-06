# Architecture

## Implemented system

Crypto helper, JSON file SecretStore, single-token API, static UI, node:test suite.

## Data and control flow

HTTP request with token → SecretStore set/get/delete → PBKDF2-derived key → AES-GCM envelope → JSON file and bounded audit list.

## Module source map

- **Threat Model and Secret Boundaries:** The server checks x-api-token for API routes; it has no user roles or key rotation.
- **Derive a Key from a Password:** deriveKey uses PBKDF2-SHA256, 120000 iterations, and 32-byte output.
- **Encrypt with AES-GCM:** encrypt uses AES-256-GCM with a random 12-byte IV and returns IV/ciphertext/tag as Base64.
- **Store Envelopes and Audit Records:** SecretStore.set encrypts and saves; record trims audit to last 200 items.
- **Use Set/Get/Delete Operations:** get returns plaintext after decrypt; list never returns secret values.
- **Authorize API Calls:** API paths require x-api-token; constant-time equal checks equal-length buffers.
- **Review Defaults and HTTP Exposure:** When SECRETS_PASSWORD absent, main uses change-me; generated TOKEN is logged.
- **Test Crypto and API Behavior:** The Node test cases cover secret round trips, incorrect-password errors, and API authorization; they do not prove deployment hardening.
- **Plan Production Hardening:** SecretStore.set writes encrypted envelopes to a local JSON store; the README limits this sample to one API token and no key rotation.

## Boundaries and risks

- Default password is change-me when SECRETS_PASSWORD is absent, and the API token is printed to console at startup.
- One API token provides broad access; no role-based access control or key rotation exists.
- Audit history is capped at 200 records and stored beside secrets; it is not an immutable audit system.
- File writes are direct, not an atomic database transaction; no TLS is provided by the basic Node server.
- Read API reveals plaintext to any holder of the API token.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
