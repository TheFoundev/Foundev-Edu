# A beginner's model of documented goals mapped to implementation

**Lesson ID:** `naivecoin-module-06-lesson-1`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors src/blockchain.js, src/main.js, src/node.js. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `README.md`, `src/blockchain.js`, `src/main.js`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/blockchain.js`, `const crypto = require("node:crypto");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `function sha256(value) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function normalizeTransaction(transaction) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class Transaction {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class Block {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class Blockchain {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- The excerpt from `src/main.js` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.

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
# Naivecoin

A small proof-of-work blockchain with a peer relay.

> A minimal cryptocurrency implementation with a block explorer UI for learning blockchain internals safely.

## Overview

An original, self-contained implementation of the **Naivecoin** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Transactions and blocks hashed with SHA-256
- Proof-of-work mining with a configurable difficulty
- Chain validation that detects tampering
- Wallet balances derived from the chain
- HTTP API and a hand-rolled WebSocket peer relay

## Stack

`Node.js`
The CSV stack is Node.js.js + WebSockets. Node has no built-in WebSocket server, so the project includes a small RFC 6455 handshake and frame parser instead of the ws package.

## Run

```bash
npm start
node src/main.js
npm test
```

## Structure

```text
naivecoin/
├── src/blockchain.js       blocks, transactions and validation
├── src/ws.js               minimal WebSocket server
├── src/node.js             HTTP API and peer relay
├── src/server.js           server entry point
├── src/main.js             local chain demo
├── test/                   node:test suites
└── package.json
```

## Testing

```bash
# see the Run section
```

## Notes and limitations

- There is no consensus fork choice, peer discovery or persistence to disk.
- Transactions are not signed and there is no UTXO model.
- The WebSocket layer is minimal: text frames, ping/pong and close only.

## License

Apache-2.0. See `LICENSE`.

## About the scope

This is a third-year student project. It targets Node's built-in modules and has no third-party runtime dependencies, so a few upstream conveniences are missing.

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

### src/main.js

```text
"use strict";

const { Blockchain } = require("./blockchain");

const chain = new Blockchain(3);
chain.addTransaction("alice", "bob", 10);
chain.addTransaction("bob", "carol", 4);
console.log("mining block 1...");
chain.minePending("alice");
chain.addTransaction("carol", "alice", 2);
console.log("mining block 2...");
chain.minePending("alice");

for (const block of chain.chain) {
  console.log(`block ${block.index} hash=${block.hash().slice(0, 16)} nonce=${block.nonce}`);
}
console.log("alice balance:", chain.balance("alice"));
console.log("bob balance:", chain.balance("bob"));
console.log("valid chain:", chain.isValid());

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

This lesson ties its explanation to `README.md`, `src/blockchain.js`, `src/main.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
