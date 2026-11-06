# Read code review and safe change 6 in the source

**Lesson ID:** `owasp-nodegoat-module-06-lesson-2`

## Purpose and learning objectives

Use src/app.js to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/app.js`, `src/server.js`, `src/store.js`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/app.js`, `const http = require("node:http");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/app.js`, `const crypto = require("node:crypto");` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `function escapeHtml(text) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function forOutput(text) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function csrfToken(sessionId) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function csrfValid(sessionId, token) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function roleCookie(role) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function roleFromCookie(value) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- The excerpt from `src/server.js` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- `function reset() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/app.js

```text
"use strict";

const http = require("node:http");
const crypto = require("node:crypto");
const { users, comments } = require("./store");

// The app is vulnerable on purpose. With NODEGOAT_HARDENED=1 the fixes are
// applied as well, so the two ways can be compared.
const HARDENED = process.env.NODEGOAT_HARDENED === "1";

// The key of the signed cookies and of the CSRF tokens.
const SECRET = [REDACTED] || crypto.randomBytes(32).toString("hex");

/**
 * The text of a page, with the markup of the text taken out.
 *
 * The vulnerable version puts the text into the page as it is, which is the
 * XSS of the exercise.
 */
function escapeHtml(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

/** The value that goes into a page. */
function forOutput(text) {
  return HARDENED ? escapeHtml(text) : String(text);
}

/**
 * A token that ties a form to the session.
 *
 * The token is the signature of the session id, so it cannot be made up.
 */
function csrfToken(sessionId) {
  return crypto.createHmac("sha256", SECRET).update(String(sessionId)).digest("hex");
}

/** True when the token of a form belongs to the session. */
function csrfValid(sessionId, token) {
  if (!HARDENED) return true;
  const expected = csrfToken(sessionId);
  if (!token || token.length !== expected.length) return false;
  return crypto.timingSafeEqual(Buffer.from(token), Buffer.from(expected));
}

/**
 * A cookie with the role, signed.
 *
 * The vulnerable version reads the role straight from the cookie, so a
 * visitor can make themself an administrator.
 */
function roleCookie(role) {
  const value = Buffer.from(String(role)).toString("base64");
  if (!HARDENED) return `role=${role}; Path=/`;
  const signature = crypto.createHmac("sha256", SECRET).update(value).digest("base64");
  return `role=${value}.${signature}; Path=/; HttpOnly; SameSite=Lax`;
}

/** The role of a signed cookie, or an empty string when it is not right. */
function roleFromCookie(value) {
  if (!HARDENED) return value;
  const parts = String(value || "").split(".");
  if (parts.length !== 2) return "";
  const expected = crypto.createHmac("sha256", SECRET).update(parts[0]).digest("base64");
  if (expected.length !== parts[1].length) return "";
  if (!crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(parts[1]))) return "";
  return Buffer.from(parts[0], "base64").toString("utf8");
}

/** The password of a user, hashed. */
function hashPassword(password) {
  const salt = crypto.randomBytes(16).toString("hex");
  const hash = crypto.scryptSync(String(password), salt, 32).toString("hex");
  return `${salt}:${hash}`;
}

/** True when the password is the one of the user. */
function passwordMatches(user, password) {
  if (!HARDENED) return user.password =[REDACTED] password;
  const [salt, hash] = String(user.password || "").split(":");
  if (!salt || !hash) return false;
  const candidate = crypto.scryptSync(String(password), salt, 32).toString("hex");
  return crypto.timingSafeEqual(Buffer.from(candidate), Buffer.from(hash));
}

const INDEX = `<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>NodeGoat practice app</title></head>
<body>
  <h1>NodeGoat practice app</h1>
  <p>This application is intentionally vulnerable. Run it locally only.</p>
  <h2>Search</h2>
  <form action="/search" method="get">
    <input name="q" placeholder="username">
    <button type="submit">Search</button>
```

### src/server.js

```text
"use strict";

const { createApp } = require("./app");

const port = Number(process.env.PORT || 3000);
const server = createApp();
server.listen(port, () => {
  console.log(`NodeGoat practice app on http://localhost:${port}`);
  console.log("WARNING: intentionally vulnerable, run locally only.");
});

```

### src/store.js

```text
"use strict";

const users = [
  { id: 1, username: "alice", password: [REDACTED], role: "user", ssn: "[SYNTHETIC IDENTIFIER REDACTED]" },
  { id: 2, username: "bob", password: [REDACTED], role: "user", ssn: "[SYNTHETIC IDENTIFIER REDACTED]" },
  { id: 3, username: "admin", password: [REDACTED], role: "admin", ssn: "[SYNTHETIC IDENTIFIER REDACTED]" },
];

const comments = [];

function reset() {
  comments.length = 0;
}

module.exports = { users, comments, reset };

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

This lesson ties its explanation to `src/app.js`, `src/server.js`, `src/store.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
