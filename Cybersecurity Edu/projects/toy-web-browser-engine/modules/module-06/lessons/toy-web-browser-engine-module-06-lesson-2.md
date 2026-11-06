# Read runtime configuration connected to code in the source

**Lesson ID:** `toy-web-browser-engine-module-06-lesson-2`

## Purpose and learning objectives

Inspect the declared manifests .github/workflows/ci.yml, Cargo.toml and trace the relevant package or setting into implementation file src/css.rs. Separate a declaration from an imported, configured, or executed behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `.github/workflows/ci.yml`, `Cargo.toml`, `src/css.rs`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `.github/workflows/ci.yml` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `Cargo.toml` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/css.rs`, `use std::collections::HashMap;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/css.rs`, `use crate::dom::{is_invisible_element, is_void_element, Node, NodeKind};` brings a module or package name into this file; follow later references before claiming it is used on a running path.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### .github/workflows/ci.yml

```text
name: CI

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
        with:
          components: clippy, rustfmt
      - name: Check the formatting
        run: cargo fmt --check
      - name: Lint
        run: cargo clippy --all-targets -- -D warnings
      - name: Run the tests
        run: cargo test

```

### Cargo.toml

```text
[package]
name = "toy_web_browser_engine"
version = "0.1.0"
edition = "2021"

[dependencies]
reqwest = { version = "0.12", default-features = false, features = ["blocking", "rustls-tls"] }
url = "2"

[profile.release]
opt-level = 3

```

### src/css.rs

```text
//! A small CSS engine: stylesheet parsing, selector matching and cascade.

use std::collections::HashMap;

use crate::dom::{is_invisible_element, is_void_element, Node, NodeKind};

/// A compound selector such as `div.card#main`.
#[derive(Clone, Debug, PartialEq, Eq, Default)]
pub struct SimpleSelector {
    /// `None` matches any element (`*`).
    pub tag: Option<String>,
    pub id: Option<String>,
    pub classes: Vec<String>,
}

impl SimpleSelector {
    /// Parse a single compound selector.
    pub fn parse(text: &str) -> SimpleSelector {
        let mut selector = SimpleSelector::default();
        let mut rest = text.trim();
        if rest == "*" {
            return selector;
        }
        while let Some(stripped) = rest.strip_prefix('*') {
            rest = stripped;
        }
        let name_end = rest
            .find(|character: char| ['.', '#'].contains(&character))
            .unwrap_or(rest.len());
        let name = &rest[..name_end];
        if !name.is_empty() {
            selector.tag = Some(name.to_ascii_lowercase());
        }
        rest = &rest[name_end..];
        while let Some(remainder) = rest.strip_prefix('.') {
            let end = remainder
                .find(|character: char| ['.', '#'].contains(&character))
                .unwrap_or(remainder.len());
            selector.classes.push(remainder[..end].to_ascii_lowercase());
            rest = &remainder[end..];
        }
        while let Some(remainder) = rest.strip_prefix('#') {
            let end = remainder
                .find(|character: char| ['.', '#'].contains(&character))
                .unwrap_or(remainder.len());
            selector.id = Some(remainder[..end].to_ascii_lowercase());
            rest = &remainder[end..];
        }
        selector
    }

    /// Does this selector match the given element?
    pub fn matches(&self, node: &Node) -> bool {
        if node.kind != NodeKind::Element {
            return false;
        }
        if let Some(tag) = &self.tag {
            if node.name != *tag {
                return false;
            }
        }
        if let Some(id) = &self.id {
            if node.attribute("id").map(|value| value.to_ascii_lowercase()) != Some(id.clone()) {
                return false;
            }
        }
        if !self.classes.is_empty() {
            let classes: Vec<String> = node
                .classes()
                .into_iter()
                .map(|class| class.to_ascii_lowercase())
                .collect();
            for required in &self.classes {
                if !classes.contains(required) {
                    return false;
                }
            }
        }
        true
    }
}

/// A full selector: a chain of compound selectors joined by descendant
/// combinators.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Selector {
    pub parts: Vec<SimpleSelector>,
}

impl Selector {
    /// Parse a descendant-combinator selector.
    pub fn parse(text: &str) -> Selector {
        let parts = text.split_whitespace().map(SimpleSelector::parse).collect();
        Selector { parts }
    }

    /// Specificity of the selector, as a comparable number.
    pub fn specificity(&self) -> u32 {
        let mut ids = 0;
        let mut classes = 0;
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

This lesson ties its explanation to `.github/workflows/ci.yml`, `Cargo.toml`, `src/css.rs`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
