# Read app and server in the source

**Lesson ID:** `signal-style-e2ee-chat-module-01-lesson-2`

## Purpose and learning objectives

Study the implementation in [public/app.js] and [src/server.js]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include toBase64, fromBase64, deriveKey, encrypt, decrypt, log, connect, send, createChatServer; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `public/app.js`, `src/server.js`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- `function toBase64(bytes) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function fromBase64(text) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `async function deriveKey(passphrase) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `async function encrypt(text) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `async function decrypt(envelope) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function log(line) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/server.js`, `const fs = require("node:fs");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/server.js`, `const path = require("node:path");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/server.js`, `const http = require("node:http");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `function createChatServer() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### src/server.js

```text
"use strict";

const fs = require("node:fs");
const path = require("node:path");
const http = require("node:http");
const { attachWebSocket, broadcast } = require("./ws");

const PUBLIC_DIR = path.join(__dirname, "..", "public");
const TYPES = {
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".css": "text/css; charset=utf-8",
};

function createChatServer() {
  const server = http.createServer((request, response) => {
    const url = new URL(request.url, "http://localhost");
    const name = url.pathname === "/" ? "index.html" : url.pathname.replace(/^\/+/, "");
    const file = path.resolve(PUBLIC_DIR, name);
    if (!file.startsWith(PUBLIC_DIR)) {
      response.writeHead(403, { "content-type": "text/plain" });
      response.end("forbidden");
      return;
    }
    fs.readFile(file, (error, data) => {
      if (error) {
        response.writeHead(404, { "content-type": "text/plain" });
        response.end("not found");
        return;
      }
      response.writeHead(200, { "content-type": TYPES[path.extname(file)] || "application/octet-stream" });
      response.end(data);
    });
  });

  attachWebSocket(server, {
    open() {},
    message(client, text, clients) {
      let message;
      try {
        message = JSON.parse(text);
      } catch (error) {
        client.send(JSON.stringify({ type: "error", error: "invalid json" }));
        return;
      }
      if (message.type === "hello" || message.type === "message") {
        // Only the envelope is relayed; the server has no key to read it.
        broadcast(clients, message);
      }
    },
  });

  return server;
}

module.exports = { createChatServer };

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

This lesson ties its explanation to `public/app.js`, `src/server.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
