# A beginner's model of test code and implementation evidence

**Lesson ID:** `signal-style-e2ee-chat-module-03-lesson-1`

## Purpose and learning objectives

Read the test cases in test/crypto.test.js, test/relay.test.js beside the implementation in public/app.js. Explain the behavior asserted by the tests and trace each assertion to the implementation. A test file describes a check; it does not prove that check passed.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `test/crypto.test.js`, `test/relay.test.js`, `public/app.js`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `test/crypto.test.js`, `const test = require("node:test");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/crypto.test.js`, `const assert = require("node:assert/strict");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/relay.test.js`, `const test = require("node:test");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/relay.test.js`, `const assert = require("node:assert/strict");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `function open(socket) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function nextMessage(socket) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function toBase64(bytes) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function fromBase64(text) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `async function deriveKey(passphrase) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `async function encrypt(text) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `async function decrypt(envelope) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function log(line) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### test/crypto.test.js

```text
"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { generateKeyPair, deriveSharedKey, encrypt, decrypt } = require("../src/crypto");

test("both sides derive the same session key", () => {
  const alice = generateKeyPair();
  const bob = generateKeyPair();
  const aliceKey = deriveSharedKey(alice.privateKey, bob.publicKey);
  const bobKey = deriveSharedKey(bob.privateKey, alice.publicKey);
  assert.equal(aliceKey.length, 32);
  assert.equal(aliceKey.equals(bobKey), true);
});

test("encrypt and decrypt round trip", () => {
  const alice = generateKeyPair();
  const bob = generateKeyPair();
  const key = deriveSharedKey(alice.privateKey, bob.publicKey);
  const envelope = encrypt(key, "hello from the other side");
  assert.equal(typeof envelope.iv, "string");
  assert.equal(decrypt(key, envelope), "hello from the other side");
});

test("a tampered tag fails decryption", () => {
  const alice = generateKeyPair();
  const bob = generateKeyPair();
  const key = deriveSharedKey(alice.privateKey, bob.publicKey);
  const envelope = encrypt(key, "important");
  envelope.tag = Buffer.from(envelope.tag, "base64").map((byte, index) => (index === 0 ? byte ^ 0xff : byte)).toString("base64");
  assert.throws(() => decrypt(key, envelope));
});

test("the wrong key cannot decrypt", () => {
  const alice = generateKeyPair();
  const bob = generateKeyPair();
  const mallory = generateKeyPair();
  const aliceKey = deriveSharedKey(alice.privateKey, bob.publicKey);
  const malloryKey = deriveSharedKey(mallory.privateKey, alice.publicKey);
  const envelope = encrypt(aliceKey, "secret");
  assert.throws(() => decrypt(malloryKey, envelope));
});

test("the salt of the key derivation tells two rooms apart", () => {
  const { generateKeyPair, deriveSharedKey, sessionSalt } = require("../src/crypto");
  const alice = generateKeyPair();
  const bob = generateKeyPair();

  const first = deriveSharedKey(alice.privateKey, bob.publicKey, sessionSalt("room-1"));
  const second = deriveSharedKey(alice.privateKey, bob.publicKey, sessionSalt("room-2"));

  assert.equal(first.length, 32);
  // A different room gives a different key.
  assert.notDeepStrictEqual(first, second);
  // The same room gives the same key on both sides.
  const other = deriveSharedKey(bob.privateKey, alice.publicKey, sessionSalt("room-1"));
  assert.deepStrictEqual(first, other);
});

test("a message that is sent again is refused", () => {
  const { encryptWithCounter, decryptWithCounter } = require("../src/crypto");
  const key = Buffer.alloc(32, 7);

  const envelope = encryptWithCounter(key, "hello", 1);
  const opened = decryptWithCounter(key, envelope, 0);
  assert.equal(opened.plaintext, "hello");
  assert.equal(opened.counter, 1);

  // The same message with the same counter is a replay.
  assert.throws(() => decryptWithCounter(key, envelope, 1), /replay/);
});

```

### test/relay.test.js

```text
"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { createChatServer } = require("../src/server");
const { generateKeyPair, deriveSharedKey, encrypt, decrypt } = require("../src/crypto");

function open(socket) {
  return new Promise((resolve, reject) => {
    socket.addEventListener("open", () => resolve(), { once: true });
    socket.addEventListener("error", () => reject(new Error("websocket failed")), { once: true });
  });
}

function nextMessage(socket) {
  return new Promise((resolve, reject) => {
    socket.addEventListener(
      "message",
      (event) => {
        try {
          resolve(JSON.parse(event.data));
        } catch (error) {
          reject(error);
        }
      },
      { once: true },
    );
  });
}

test("serves the client page", async () => {
  const server = createChatServer();
  await new Promise((resolve) => server.listen(0, resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  try {
    const response = await fetch(`${base}/`);
    const body = await response.text();
    assert.equal(response.status, 200);
    assert.equal(body.includes("Signal-style chat demo"), true);
  } finally {
    server.closeAllConnections();
    await new Promise((resolve) => server.close(resolve));
  }
});

test("relays an opaque envelope between two clients", async () => {
  const server = createChatServer();
  await new Promise((resolve) => server.listen(0, resolve));
  const port = server.address().port;
  const alice = new WebSocket(`ws://127.0.0.1:${port}`);
  const bob = new WebSocket(`ws://127.0.0.1:${port}`);
  try {
    await Promise.all([open(alice), open(bob)]);

    const aliceKeys = generateKeyPair();
    const bobKeys = generateKeyPair();
    const aliceKey = deriveSharedKey(aliceKeys.privateKey, bobKeys.publicKey);
    const bobKey = deriveSharedKey(bobKeys.privateKey, aliceKeys.publicKey);
    assert.equal(aliceKey.equals(bobKey), true);

    const received = nextMessage(bob);
    alice.send(JSON.stringify({ type: "message", name: "alice", payload: encrypt(aliceKey, "hello bob") }));
    const message = await received;
    assert.equal(message.type, "message");
    assert.equal(message.name, "alice");
    assert.equal(decrypt(bobKey, message.payload), "hello bob");
  } finally {
    alice.close();
    bob.close();
    server.closeAllConnections();
    await new Promise((resolve) => server.close(resolve));
  }
});

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

This lesson ties its explanation to `test/crypto.test.js`, `test/relay.test.js`, `public/app.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
