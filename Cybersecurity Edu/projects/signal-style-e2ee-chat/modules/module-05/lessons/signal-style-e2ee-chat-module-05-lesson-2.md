# Read documented goals mapped to implementation in the source

**Lesson ID:** `signal-style-e2ee-chat-module-05-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors public/app.js, src/crypto.js, src/server.js. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `public/app.js`, `src/crypto.js`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- `function toBase64(bytes) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function fromBase64(text) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `async function deriveKey(passphrase) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `async function encrypt(text) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `async function decrypt(envelope) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function log(line) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/crypto.js`, `const crypto = require("node:crypto");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `function generateKeyPair() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function toPublicKey(base64) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function toPrivateKey(base64) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function deriveSharedKey(privateKeyBase64, publicKeyBase64, salt) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function sessionSalt(roomId) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function encryptWithCounter(key, plaintext, counter) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
# Signal-style E2EE Chat

A chat relay where the server only sees encrypted envelopes.

> An educational end-to-end encrypted chat that implements core Signal Protocol ideas over WebSockets.

## Overview

An original, self-contained implementation of the **Signal-style E2EE Chat** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- X25519 key exchange with HKDF-derived session keys
- AES-256-GCM encryption with authenticated tags
- Hand-rolled WebSocket relay that forwards opaque envelopes
- Browser client that shares a room passphrase for end-to-end encryption

## Stack

`Node.js`
The CSV stack is Node.js.js + WebSockets + libsignal. libsignal is not available, so the project uses node:crypto X25519 and AES-GCM; it is not the Signal protocol and there is no double ratchet.

## Run

```bash
npm start
npm test
```

## Structure

```text
signal-style-e2ee-chat/
├── src/crypto.js           X25519 and AES-GCM helpers
├── src/ws.js               minimal WebSocket server
├── src/server.js            static files and the relay
├── public/index.html        chat page
├── public/app.js            browser key derivation and encryption
├── test/                    crypto and relay tests
└── package.json
```

## Testing

```bash
# see the Run section
```

## Notes and limitations

- There is no forward secrecy per message, prekey bundle or group session.
- The room passphrase is typed into the browser; key distribution is manual.
- The relay keeps no history and stores nothing, but it is not audited.

## License

Apache-2.0. See `LICENSE`.

## About the scope

This is a third-year student project. It targets Node's built-in modules and has no third-party runtime dependencies, so a few upstream conveniences are missing.

```

### public/app.js

```text
"use strict";

const state = { socket: null, key: null };

const encoder = new TextEncoder();
const decoder = new TextDecoder();

function toBase64(bytes) {
  let binary = "";
  for (const byte of bytes) {
    binary += String.fromCharCode(byte);
  }
  return btoa(binary);
}

function fromBase64(text) {
  return Uint8Array.from(atob(text), (character) => character.charCodeAt(0));
}

async function deriveKey(passphrase) {
  const material = await crypto.subtle.importKey("raw", encoder.encode(passphrase), "PBKDF2", false, ["deriveKey"]);
  return crypto.subtle.deriveKey(
    { name: "PBKDF2", salt: encoder.encode("signal-style-chat"), iterations: 120000, hash: "SHA-256" },
    material,
    { name: "AES-GCM", length: 256 },
    false,
    ["encrypt", "decrypt"],
  );
}

async function encrypt(text) {
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const data = await crypto.subtle.encrypt({ name: "AES-GCM", iv }, state.key, encoder.encode(text));
  return { iv: toBase64(iv), data: toBase64(new Uint8Array(data)) };
}

async function decrypt(envelope) {
  const iv = fromBase64(envelope.iv);
  const data = fromBase64(envelope.data);
  const plain = await crypto.subtle.decrypt({ name: "AES-GCM", iv }, state.key, data);
  return decoder.decode(plain);
}

function log(line) {
  const element = document.createElement("p");
  element.textContent = line;
  document.getElementById("log").appendChild(element);
}

async function connect() {
  const name = document.getElementById("name").value || "guest";
  const passphrase = document.getElementById("passphrase").value || "change-me";
  state.key = await deriveKey(passphrase);

  const protocol = location.protocol === "https:" ? "wss:" : "ws:";
  state.socket = new WebSocket(`${protocol}//${location.host}`);

  state.socket.addEventListener("open", () => {
    document.getElementById("status").textContent = "connected";
    document.getElementById("send").disabled = false;
    state.socket.send(JSON.stringify({ type: "hello", name }));
  });

  state.socket.addEventListener("message", async (event) => {
    const message = JSON.parse(event.data);
    if (message.type !== "message") {
      return;
    }
    try {
      const text = await decrypt(message.payload);
      log(`${message.name}: ${text}`);
    } catch (error) {
      log("[could not decrypt a message from another room]");
    }
  });

  state.socket.addEventListener("close", () => {
    document.getElementById("status").textContent = "offline";
    document.getElementById("send").disabled = true;
  });
}

async function send() {
  const input = document.getElementById("message");
  const text = input.value;
  if (!text || !state.socket || state.socket.readyState !== WebSocket.OPEN) {
    return;
  }
  const name = document.getElementById("name").value || "guest";
  const payload = await encrypt(text);
  state.socket.send(JSON.stringify({ type: "message", name, payload }));
  log(`${name}: ${text}`);
  input.value = "";
}

document.getElementById("connect").addEventListener("click", connect);
document.getElementById("send").addEventListener("click", send);
document.getElementById("message").addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    send();
```

### src/crypto.js

```text
"use strict";

const crypto = require("node:crypto");

const ALGORITHM = "aes-256-gcm";
const INFO = "signal-style-chat-v1";

function generateKeyPair() {
  const { publicKey, privateKey } = crypto.generateKeyPairSync("x25519");
  return {
    publicKey: publicKey.export({ type: "spki", format: "der" }).toString("base64"),
    privateKey: [REDACTED] type: "pkcs8", format: "der" }).toString("base64"),
  };
}

function toPublicKey(base64) {
  return crypto.createPublicKey({ key: Buffer.from(base64, "base64"), format: "der", type: "spki" });
}

function toPrivateKey(base64) {
  return crypto.createPrivateKey({ key: Buffer.from(base64, "base64"), format: "der", type: "pkcs8" });
}

function deriveSharedKey(privateKeyBase64, publicKeyBase64, salt) {
  const secret = [REDACTED]
    privateKey: [REDACTED],
    publicKey: toPublicKey(publicKeyBase64),
  });
  // The salt is what tells two sessions apart. Both sides have to use the
  // same one, so it is derived from the room and not made up on the spot.
  const used = salt === undefined ? sessionSalt("default") : salt;
  return Buffer.from(crypto.hkdfSync("sha256", secret, used, INFO, 32));
}

/**
 * The salt of a room.
 *
 * Both sides of a room derive the same salt from its name, so they come to
 * the same key without having to send it.
 */
function sessionSalt(roomId) {
  return crypto.createHash("sha256").update(String(roomId)).digest();
}

/**
 * Encrypt a message with a counter.
 *
 * The counter is part of the data that is authenticated, so a message that
 * is sent again with the same number is refused.
 */
function encryptWithCounter(key, plaintext, counter) {
  const iv = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv(ALGORITHM, key, iv);
  const header = Buffer.alloc(8);
  header.writeBigUInt64BE(BigInt(counter));
  cipher.setAAD(header);
  const ciphertext = Buffer.concat([cipher.update(String(plaintext), "utf8"), cipher.final()]);
  return {
    iv: iv.toString("base64"),
    ciphertext: ciphertext.toString("base64"),
    tag: cipher.getAuthTag().toString("base64"),
    counter: String(counter),
  };
}

/**
 * Open a message and check its counter.
 *
 * The counter has to be bigger than the last one that was seen, or the
 * message is a replay.
 */
function decryptWithCounter(key, envelope, lastCounter) {
  const iv = Buffer.from(envelope.iv, "base64");
  const decipher = crypto.createDecipheriv(ALGORITHM, key, iv);
  decipher.setAuthTag(Buffer.from(envelope.tag, "base64"));
  const header = Buffer.alloc(8);
  header.writeBigUInt64BE(BigInt(envelope.counter || 0));
  decipher.setAAD(header);
  const plaintext = Buffer.concat([
    decipher.update(Buffer.from(envelope.ciphertext, "base64")),
    decipher.final(),
  ]).toString("utf8");

  const counter = Number(envelope.counter || 0);
  if (lastCounter !== undefined && counter <= lastCounter) {
    throw new Error("the message is a replay");
  }
  return { plaintext, counter };
}

function encrypt(key, plaintext) {
  const iv = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv(ALGORITHM, key, iv);
  const ciphertext = Buffer.concat([cipher.update(plaintext, "utf8"), cipher.final()]);
  return {
    iv: iv.toString("base64"),
    ciphertext: ciphertext.toString("base64"),
    tag: cipher.getAuthTag().toString("base64"),
  };
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

This lesson ties its explanation to `README.md`, `public/app.js`, `src/crypto.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
