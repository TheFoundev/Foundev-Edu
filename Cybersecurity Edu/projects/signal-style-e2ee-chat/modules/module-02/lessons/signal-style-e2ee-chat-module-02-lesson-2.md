# Read crypto and ws in the source

**Lesson ID:** `signal-style-e2ee-chat-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/crypto.js] and [src/ws.js]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include generateKeyPair, toPublicKey, toPrivateKey, deriveSharedKey, sessionSalt, encryptWithCounter, decryptWithCounter, encrypt, acceptKey, encodeFrame, encodeText, parseFrame, attachWebSocket, broadcast; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/crypto.js`, `src/ws.js`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/crypto.js`, `const crypto = require("node:crypto");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `function generateKeyPair() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function toPublicKey(base64) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function toPrivateKey(base64) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function deriveSharedKey(privateKeyBase64, publicKeyBase64, salt) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function sessionSalt(roomId) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function encryptWithCounter(key, plaintext, counter) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/ws.js`, `const crypto = require("node:crypto");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `function acceptKey(key) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function encodeFrame(opcode, payload) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function encodeText(text) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function parseFrame(buffer) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function attachWebSocket(httpServer, handlers) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function broadcast(clients, data, except) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### src/ws.js

```text
"use strict";

const crypto = require("node:crypto");

const GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11";

function acceptKey(key) {
  return crypto.createHash("sha1").update(key + GUID).digest("base64");
}

function encodeFrame(opcode, payload) {
  const body = Buffer.isBuffer(payload) ? payload : Buffer.from(String(payload), "utf8");
  let header;
  if (body.length < 126) {
    header = Buffer.alloc(2);
    header[0] = 0x80 | opcode;
    header[1] = body.length;
  } else if (body.length < 65536) {
    header = Buffer.alloc(4);
    header[0] = 0x80 | opcode;
    header[1] = 126;
    header.writeUInt16BE(body.length, 2);
  } else {
    header = Buffer.alloc(10);
    header[0] = 0x80 | opcode;
    header[1] = 127;
    header.writeBigUInt64BE(BigInt(body.length), 2);
  }
  return Buffer.concat([header, body]);
}

function encodeText(text) {
  return encodeFrame(0x1, text);
}

function parseFrame(buffer) {
  if (buffer.length < 2) {
    return null;
  }
  const opcode = buffer[0] & 0x0f;
  const masked = (buffer[1] & 0x80) !== 0;
  let length = buffer[1] & 0x7f;
  let offset = 2;
  if (length === 126) {
    if (buffer.length < 4) {
      return null;
    }
    length = buffer.readUInt16BE(2);
    offset = 4;
  } else if (length === 127) {
    if (buffer.length < 10) {
      return null;
    }
    const big = buffer.readBigUInt64BE(2);
    if (big > BigInt(Number.MAX_SAFE_INTEGER)) {
      throw new Error("frame too large");
    }
    length = Number(big);
    offset = 10;
  }
  let mask = null;
  if (masked) {
    if (buffer.length < offset + 4) {
      return null;
    }
    mask = buffer.subarray(offset, offset + 4);
    offset += 4;
  }
  if (buffer.length < offset + length) {
    return null;
  }
  const payload = Buffer.from(buffer.subarray(offset, offset + length));
  if (mask) {
    for (let index = 0; index < payload.length; index++) {
      payload[index] ^= mask[index % 4];
    }
  }
  return { opcode, payload, rest: buffer.subarray(offset + length) };
}

function attachWebSocket(httpServer, handlers) {
  const clients = new Set();
  httpServer.on("upgrade", (request, socket) => {
    const key = request.headers["sec-websocket-key"];
    if (!key) {
      socket.destroy();
      return;
    }
    socket.write([
      "HTTP/1.1 101 Switching Protocols",
      "Upgrade: websocket",
      "Connection: Upgrade",
      "Sec-WebSocket-Accept: " + acceptKey(key),
      "",
      "",
    ].join("\r\n"));

    const client = {
      socket,
      send(text) {
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

This lesson ties its explanation to `src/crypto.js`, `src/ws.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
