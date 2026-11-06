# A beginner's model of test code and implementation evidence

**Lesson ID:** `naivecoin-module-04-lesson-1`

## Purpose and learning objectives

Read the test cases in test/blockchain.test.js, test/node.test.js, test/ws.test.js beside the implementation in src/blockchain.js. Explain the behavior asserted by the tests and trace each assertion to the implementation. A test file describes a check; it does not prove that check passed.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `test/blockchain.test.js`, `test/node.test.js`, `test/ws.test.js`, `src/blockchain.js`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `test/blockchain.test.js`, `const test = require("node:test");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/blockchain.test.js`, `const assert = require("node:assert/strict");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/node.test.js`, `const test = require("node:test");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/node.test.js`, `const assert = require("node:assert/strict");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/ws.test.js`, `const test = require("node:test");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/ws.test.js`, `const assert = require("node:assert/strict");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `function maskedFrame(text) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/blockchain.js`, `const crypto = require("node:crypto");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `function sha256(value) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function normalizeTransaction(transaction) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class Transaction {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class Block {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class Blockchain {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### test/blockchain.test.js

```text
"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { Blockchain } = require("../src/blockchain");

test("genesis chain is valid", () => {
  const chain = new Blockchain(2);
  assert.equal(chain.chain.length, 1);
  assert.equal(chain.isValid(), true);
});

test("mining adds a valid block and clears pending transactions", () => {
  const chain = new Blockchain(2);
  chain.addTransaction("alice", "bob", 10);
  const block = chain.minePending("miner");
  assert.equal(chain.chain.length, 2);
  assert.equal(chain.pending.length, 0);
  assert.equal(block.hash().startsWith("00"), true);
  assert.equal(chain.isValid(), true);
});

test("balances include transfers and mining rewards", () => {
  const chain = new Blockchain(2);
  chain.addTransaction("alice", "bob", 10);
  chain.minePending("miner");
  assert.equal(chain.balance("alice"), -10);
  assert.equal(chain.balance("bob"), 10);
  assert.equal(chain.balance("miner"), 1);
});

test("tampering makes the chain invalid", () => {
  const chain = new Blockchain(2);
  chain.addTransaction("alice", "bob", 10);
  chain.minePending("miner");
  chain.chain[1].transactions[0].amount = 1000;
  assert.equal(chain.isValid(), false);
});

test("rejects invalid transactions", () => {
  const chain = new Blockchain(2);
  assert.throws(() => chain.addTransaction("", "bob", 10));
  assert.throws(() => chain.addTransaction("alice", "bob", 0));
  assert.throws(() => chain.addTransaction("alice", "bob", "lots"));
});

```

### test/node.test.js

```text
"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { createNodeServer } = require("../src/node");
const { Blockchain } = require("../src/blockchain");

test("http api exposes, mines and validates blocks", async () => {
  const server = createNodeServer(new Blockchain(2));
  await new Promise((resolve) => server.listen(0, resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  try {
    let response = await fetch(`${base}/api/blocks`);
    assert.equal(response.status, 200);
    let blocks = await response.json();
    assert.equal(blocks.length, 1);

    response = await fetch(`${base}/api/transactions`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ from: "alice", to: "bob", amount: 5 }),
    });
    assert.equal(response.status, 201);

    response = await fetch(`${base}/api/mine`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ miner: "miner" }),
    });
    assert.equal(response.status, 200);

    response = await fetch(`${base}/api/blocks`);
    blocks = await response.json();
    assert.equal(blocks.length, 2);
  } finally {
    server.closeAllConnections();
    await new Promise((resolve) => server.close(resolve));
  }
});

```

### test/ws.test.js

```text
"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { acceptKey, encodeText, parseFrame } = require("../src/ws");

function maskedFrame(text) {
  const payload = Buffer.from(text, "utf8");
  const mask = Buffer.from([1, 2, 3, 4]);
  const masked = Buffer.from(payload.map((byte, index) => byte ^ mask[index % 4]));
  return Buffer.concat([Buffer.from([0x81, 0x80 | payload.length]), mask, masked]);
}

test("computes the RFC 6455 accept key", () => {
  assert.equal(acceptKey("dGhlIHNhbXBsZSBub25jZQ=="), "s3pPLMBiTxaQ9kYGzzhZRbK+xOo=");
});

test("parses a masked client frame", () => {
  const frame = parseFrame(maskedFrame("hello"));
  assert.equal(frame.opcode, 0x1);
  assert.equal(frame.payload.toString("utf8"), "hello");
  assert.equal(frame.rest.length, 0);
});

test("returns null for a partial frame", () => {
  const frame = maskedFrame("hello");
  assert.equal(parseFrame(frame.subarray(0, 4)), null);
});

test("encodes a server text frame", () => {
  const frame = encodeText("hi");
  assert.equal(frame[0], 0x81);
  assert.equal(frame[1], 2);
  assert.equal(frame.subarray(2).toString("utf8"), "hi");
});

test("a client masks its frames", () => {
  const { encodeFrame, parseFrame } = require("../src/ws");
  const frame = encodeFrame(0x1, Buffer.from("hi"), true);
  // The mask bit is set.
  assert.strictEqual(frame[1] & 0x80, 0x80);
  const parsed = parseFrame(frame);
  assert.strictEqual(parsed.payload.toString(), "hi");
});

test("a frame that is too large is refused", () => {
  const { parseFrame } = require("../src/ws");
  const header = Buffer.alloc(10);
  header[0] = 0x81;
  header[1] = 127;
  header.writeBigUInt64BE(BigInt(10 * 1024 * 1024), 2);
  assert.throws(() => parseFrame(header), /too large/);
});

test("a client frame without a mask is refused by the server", () => {
  const { encodeFrame, parseFrame } = require("../src/ws");
  const frame = encodeFrame(0x1, Buffer.from("hi"), false);
  assert.throws(() => parseFrame(frame, { requireMask: true }), /mask/);
});

test("the fragments of a message are put together", () => {
  const { encodeFrame, parseFrames } = require("../src/ws");
  const first = encodeFrame(0x1, Buffer.from("he"), true);
  const rest = encodeFrame(0x0, Buffer.from("llo"), true);
  const { frames } = parseFrames(Buffer.concat([first, rest]), { requireMask: true });
  assert.strictEqual(frames.length, 1);
  assert.strictEqual(frames[0].payload.toString(), "hello");
});

```

### src/blockchain.js

```text
"use strict";

const crypto = require("node:crypto");

function sha256(value) {
  return crypto.createHash("sha256").update(value).digest("hex");
}

function normalizeTransaction(transaction) {
  return {
    from: String(transaction.from),
    to: String(transaction.to),
    amount: Number(transaction.amount),
    timestamp: Number(transaction.timestamp || 0),
  };
}

class Transaction {
  constructor(from, to, amount, timestamp = Date.now()) {
    this.from = String(from);
    this.to = String(to);
    this.amount = Number(amount);
    this.timestamp = Number(timestamp);
  }

  toJSON() {
    return normalizeTransaction(this);
  }
}

class Block {
  constructor(index, timestamp, transactions, previousHash, nonce = 0) {
    this.index = index;
    this.timestamp = timestamp;
    this.transactions = transactions.map(normalizeTransaction);
    this.previousHash = previousHash;
    this.nonce = nonce;
  }

  hash() {
    return sha256(JSON.stringify(this.toJSON()));
  }

  toJSON() {
    return {
      index: this.index,
      timestamp: this.timestamp,
      transactions: this.transactions,
      previousHash: this.previousHash,
      nonce: this.nonce,
    };
  }

  static fromJSON(value) {
    const block = new Block(value.index, value.timestamp, value.transactions, value.previousHash, value.nonce);
    return block;
  }
}

class Blockchain {
  constructor(difficulty = 3) {
    this.difficulty = difficulty;
    this.chain = [new Block(0, 0, [], "0".repeat(64))];
    this.pending = [];
  }

  get lastBlock() {
    return this.chain[this.chain.length - 1];
  }

  addTransaction(from, to, amount) {
    const value = Number(amount);
    if (!from || !to || !Number.isFinite(value) || value <= 0) {
      throw new Error("transaction needs a sender, a recipient and a positive amount");
    }
    const transaction = new Transaction(from, to, value);
    this.pending.push(transaction);
    return transaction;
  }

  minePending(miner = "miner") {
    const reward = new Transaction("network", miner, 1, Date.now());
    const block = new Block(
      this.chain.length,
      Date.now(),
      [...this.pending, reward],
      this.lastBlock.hash(),
    );
    const prefix = "0".repeat(this.difficulty);
    while (!block.hash().startsWith(prefix)) {
      block.nonce += 1;
    }
    this.chain.push(block);
    this.pending = [];
    return block;
  }

  isValid() {
    if (!Array.isArray(this.chain) || this.chain.length === 0) {
      return false;
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

This lesson ties its explanation to `test/blockchain.test.js`, `test/node.test.js`, `test/ws.test.js`, `src/blockchain.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
