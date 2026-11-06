# Read runtime configuration connected to code in the source

**Lesson ID:** `sniffnet-module-03-lesson-2`

## Purpose and learning objectives

Inspect the declared manifests .github/workflows/ci.yml, Cargo.toml and trace the relevant package or setting into implementation file src/lib.rs. Separate a declaration from an imported, configured, or executed behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `.github/workflows/ci.yml`, `Cargo.toml`, `src/lib.rs`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `.github/workflows/ci.yml` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `Cargo.toml` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/lib.rs`, `use std::collections::BTreeMap;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/lib.rs`, `use super::*;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/lib.rs`, `use std::collections::VecDeque;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/lib.rs`, `use std::net::UdpSocket;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/lib.rs`, `use std::time::Duration;` brings a module or package name into this file; follow later references before claiming it is used on a running path.

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
      - name: Check the formatting
        run: cargo fmt --check
      - name: Run the tests
        run: cargo test

```

### Cargo.toml

```text
[package]
name = "sniffnet"
version = "0.1.0"
edition = "2021"

[dependencies]

```

### src/lib.rs

```text
use std::collections::BTreeMap;

#[derive(Clone, Debug, PartialEq, Eq)]
pub enum Protocol {
    Tcp,
    Udp,
    Icmp,
    Other(String),
}

impl Protocol {
    pub fn parse(text: &str) -> Protocol {
        match text.trim().to_lowercase().as_str() {
            "tcp" => Protocol::Tcp,
            "udp" => Protocol::Udp,
            "icmp" => Protocol::Icmp,
            other => Protocol::Other(other.to_string()),
        }
    }

    pub fn label(&self) -> String {
        match self {
            Protocol::Tcp => "tcp".to_string(),
            Protocol::Udp => "udp".to_string(),
            Protocol::Icmp => "icmp".to_string(),
            Protocol::Other(name) => name.clone(),
        }
    }
}

#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Packet {
    pub source: String,
    pub destination: String,
    pub protocol: Protocol,
    pub bytes: u64,
}

pub fn parse_line(line: &str) -> Option<Packet> {
    let trimmed = line.trim();
    if trimmed.is_empty() || trimmed.starts_with('#') {
        return None;
    }
    let parts: Vec<&str> = trimmed.split(',').map(|part| part.trim()).collect();
    if parts.len() < 4 {
        return None;
    }
    let bytes = parts[3].parse::<u64>().ok()?;
    Some(Packet {
        source: parts[0].to_string(),
        destination: parts[1].to_string(),
        protocol: Protocol::parse(parts[2]),
        bytes,
    })
}

#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Summary {
    pub packets: u64,
    pub bytes: u64,
    pub by_protocol: Vec<(String, u64)>,
    pub top_sources: Vec<(String, u64)>,
}

pub fn summarize(packets: &[Packet]) -> Summary {
    let mut protocols: BTreeMap<String, u64> = BTreeMap::new();
    let mut sources: BTreeMap<String, u64> = BTreeMap::new();
    let mut total_bytes = 0;
    for packet in packets {
        total_bytes += packet.bytes;
        *protocols.entry(packet.protocol.label()).or_insert(0) += packet.bytes;
        *sources.entry(packet.source.clone()).or_insert(0) += packet.bytes;
    }

    let mut by_protocol: Vec<(String, u64)> = protocols.into_iter().collect();
    by_protocol.sort_by(|left, right| right.1.cmp(&left.1).then(left.0.cmp(&right.0)));

    let mut top_sources: Vec<(String, u64)> = sources.into_iter().collect();
    top_sources.sort_by(|left, right| right.1.cmp(&left.1).then(left.0.cmp(&right.0)));
    top_sources.truncate(5);

    Summary {
        packets: packets.len() as u64,
        bytes: total_bytes,
        by_protocol,
        top_sources,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parses_a_valid_line() {
        let packet = parse_line("10.0.0.1, 10.0.0.2, TCP, 1500").expect("packet");
        assert_eq!(packet.source.as_str(), "10.0.0.1");
        assert_eq!(packet.destination.as_str(), "10.0.0.2");
        assert_eq!(packet.protocol, Protocol::Tcp);
        assert_eq!(packet.bytes, 1500);
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

This lesson ties its explanation to `.github/workflows/ci.yml`, `Cargo.toml`, `src/lib.rs`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
