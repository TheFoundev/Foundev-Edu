# A beginner's model of node and ws

**Lesson ID:** `naivecoin-module-03-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/node.js] and [src/ws.js]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include readBody, createNodeServer, acceptKey, encodeFrame, encodeText, parseFrame, parseFrames; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/node.js`, `src/ws.js`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/node.js`, `const http = require("node:http");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `function readBody(request) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function createNodeServer(blockchain = new Blockchain(3)) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/ws.js`, `const crypto = require("node:crypto");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `function acceptKey(key) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function encodeFrame(opcode, payload, mask = false) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function encodeText(text, mask = false) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function parseFrame(buffer, options = {}) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function parseFrames(buffer, options = {}) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function attachWebSocket(httpServer, handlers) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/node.js

```text
"use strict";

const http = require("node:http");
const { attachWebSocket, broadcast } = require("./ws");
const { Blockchain } = require("./blockchain");

function readBody(request) {
  return new Promise((resolve, reject) => {
    let data = "";
    request.on("data", (chunk) => {
      data += chunk;
    });
    request.on("end", () => {
      if (!data) {
        resolve({});
        return;
      }
      try {
        resolve(JSON.parse(data));
      } catch (error) {
        reject(new Error("request body is not valid JSON"));
      }
    });
    request.on("error", reject);
  });
}

function createNodeServer(blockchain = new Blockchain(3)) {
  const server = http.createServer(async (request, response) => {
    const url = new URL(request.url, "http://localhost");
    const send = (status, body) => {
      response.writeHead(status, { "content-type": "application/json; charset=utf-8" });
      response.end(JSON.stringify(body));
    };

    try {
      if (request.method === "GET" && url.pathname === "/") {
        send(200, {
          name: "naivecoin",
          blocks: blockchain.chain.length,
          pending: blockchain.pending.length,
          valid: blockchain.isValid(),
        });
        return;
      }
      if (request.method === "GET" && url.pathname === "/api/blocks") {
        send(200, blockchain.chain);
        return;
      }
      if (request.method === "GET" && url.pathname === "/api/balance") {
        const address = url.searchParams.get("address") || "";
        send(200, { address, balance: blockchain.balance(address) });
        return;
      }
      if (request.method === "POST" && url.pathname === "/api/transactions") {
        const body = await readBody(request);
        const transaction = blockchain.addTransaction(body.from, body.to, body.amount);
        broadcast(server.clients || new Set(), { type: "transaction", transaction });
        send(201, transaction);
        return;
      }
      if (request.method === "POST" && url.pathname === "/api/mine") {
        const body = await readBody(request).catch(() => ({}));
        const block = blockchain.minePending(body.miner || "miner");
        broadcast(server.clients || new Set(), { type: "block", block });
        send(200, block);
        return;
      }
      send(404, { error: "not found" });
    } catch (error) {
      send(400, { error: error.message });
    }
  });

  const clients = attachWebSocket(server, {
    open(client) {
      client.send(JSON.stringify({ type: "chain", chain: blockchain.chain }));
    },
    message(client, text, peers) {
      let message;
      try {
        message = JSON.parse(text);
      } catch (error) {
        client.send(JSON.stringify({ type: "error", error: "invalid json" }));
        return;
      }
      if (message.type === "transaction") {
        try {
          const transaction = blockchain.addTransaction(message.from, message.to, message.amount);
          broadcast(peers, { type: "transaction", transaction });
        } catch (error) {
          client.send(JSON.stringify({ type: "error", error: error.message }));
        }
      } else if (message.type === "request-chain") {
        client.send(JSON.stringify({ type: "chain", chain: blockchain.chain }));
      }
    },
  });
  server.clients = clients;
  return server;
```

### src/ws.js

```text
"use strict";

const crypto = require("node:crypto");

const GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11";

function acceptKey(key) {
  return crypto.createHash("sha1").update(key + GUID).digest("base64");
}

// The biggest frame the server accepts.
const MAX_FRAME_BYTES = 1024 * 1024;

/**
 * A frame of the websocket protocol.
 *
 * A client has to mask its frames, a server must not, so the mask is a
 * parameter of the function.
 */
function encodeFrame(opcode, payload, mask = false) {
  const body = Buffer.isBuffer(payload) ? payload : Buffer.from(String(payload), "utf8");
  const masked = mask ? 0x80 : 0x00;

  let header;
  if (body.length < 126) {
    header = Buffer.alloc(2);
    header[0] = 0x80 | opcode;
    header[1] = masked | body.length;
  } else if (body.length < 65536) {
    header = Buffer.alloc(4);
    header[0] = 0x80 | opcode;
    header[1] = masked | 126;
    header.writeUInt16BE(body.length, 2);
  } else {
    header = Buffer.alloc(10);
    header[0] = 0x80 | opcode;
    header[1] = masked | 127;
    header.writeBigUInt64BE(BigInt(body.length), 2);
  }

  if (!mask) {
    return Buffer.concat([header, body]);
  }

  // The mask is four bytes that change for every frame.
  const key = Buffer.alloc(4);
  for (let index = 0; index < 4; index += 1) {
    key[index] = Math.floor(Math.random() * 256);
  }
  const maskedBody = Buffer.from(body);
  for (let index = 0; index < maskedBody.length; index += 1) {
    maskedBody[index] ^= key[index % 4];
  }
  return Buffer.concat([header, key, maskedBody]);
}

/**
 * A text frame.
 *
 * A server sends its frames without a mask, a client has to mask its frames.
 */
function encodeText(text, mask = false) {
  return encodeFrame(0x1, text, mask);
}

/**
 * One frame of the websocket protocol.
 *
 * The size of a frame is limited, and the fragments of a message are put
 * together.
 */
function parseFrame(buffer, options = {}) {
  const maxBytes = options.maxBytes || MAX_FRAME_BYTES;
  const requireMask = options.requireMask === true;
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
    if (big > BigInt(maxBytes)) {
      throw new Error("frame too large");
    }
    length = Number(big);
    offset = 10;
  }
  if (length > maxBytes) {
    throw new Error("frame too large");
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

This lesson ties its explanation to `src/node.js`, `src/ws.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
