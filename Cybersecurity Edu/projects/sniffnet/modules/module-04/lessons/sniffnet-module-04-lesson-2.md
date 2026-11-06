# Read documented goals mapped to implementation in the source

**Lesson ID:** `sniffnet-module-04-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors src/lib.rs, src/main.rs, web/server.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `src/lib.rs`, `src/main.rs`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/lib.rs`, `use std::collections::BTreeMap;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/lib.rs`, `use super::*;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/lib.rs`, `use std::collections::VecDeque;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/lib.rs`, `use std::net::UdpSocket;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/lib.rs`, `use std::time::Duration;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main.rs`, `use sniffnet::{parse_line, summarize, LiveCapture, Packet, Source, UdpSource};` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main.rs`, `use std::time::Duration;` brings a module or package name into this file; follow later references before claiming it is used on a running path.

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
# Sniffnet

Summarise a packet capture from a simple CSV trace.

> A cross-platform network traffic monitor written in Rust that makes packet capture approachable and visual.

## Overview

An original, self-contained implementation of the **Sniffnet** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Capture records parsed from source, destination, protocol and bytes
- Per-protocol byte totals
- Top talkers ranked by bytes
- Library API with unit tests and a small CLI

## Stack

`Rust`
The CSV stack is Rust. This build has no external crates, so it reads a small CSV trace format instead of a live pcap device, and prints a terminal summary instead of a GUI.

## Run

```bash
cargo run --release
cargo test --offline
```

## Structure

```text
sniffnet/
├── src/lib.rs            capture parsing and statistics
├── src/main.rs           command line summary
└── Cargo.toml
```

## Testing

```bash
cargo test
```

7 tests (`cargo test`), up from 3.


## Notes and limitations

- There is no live capture, network interface access or GUI.
- The parser expects four comma-separated fields per line.
- Statistics are simple totals, not time-series or flow analysis.

## License

MIT. See `LICENSE`.

## About the scope

This is a third-year student project in Rust with no external crates. It is not a production implementation; the notes list what was skipped.

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

### src/main.rs

```text
use sniffnet::{parse_line, summarize, LiveCapture, Packet, Source, UdpSource};
use std::time::Duration;

const SAMPLE: &str = "\
# source, destination, protocol, bytes
10.0.0.1, 10.0.0.2, tcp, 1500
10.0.0.1, 10.0.0.2, tcp, 900
10.0.0.3, 8.8.8.8, udp, 120
10.0.0.2, 10.0.0.1, icmp, 64
10.0.0.3, 1.1.1.1, tcp, 2500
";

fn main() {
    let arguments: Vec<String> = std::env::args().collect();
    let mut live = false;
    let mut address = String::from("127.0.0.1:0");
    let mut file: Option<String> = None;

    let mut index = 1;
    while index < arguments.len() {
        match arguments[index].as_str() {
            "--live" => live = true,
            "--listen" => {
                index += 1;
                if index < arguments.len() {
                    address = arguments[index].clone();
                }
            }
            other => file = Some(other.to_string()),
        }
        index += 1;
    }

    if live {
        live_capture(&address);
        return;
    }

    let text = match file {
        Some(path) => std::fs::read_to_string(&path).unwrap_or_else(|error| {
            eprintln!("could not read {}: {}", path, error);
            std::process::exit(1);
        }),
        None => SAMPLE.to_string(),
    };

    let packets: Vec<_> = text.lines().filter_map(parse_line).collect();
    let summary = summarize(&packets);

    println!("packets: {}", summary.packets);
    println!("bytes:   {}", summary.bytes);
    println!("by protocol:");
    for (protocol, bytes) in &summary.by_protocol {
        println!("  {:<8} {}", protocol, bytes);
    }
    println!("top sources:");
    for (source, bytes) in &summary.top_sources {
        println!("  {:<15} {}", source, bytes);
    }
}

/// Listen on a socket and show the traffic while it comes in.
fn live_capture(address: &str) {
    let mut source = match UdpSource::bind(address) {
        Ok(source) => source,
        Err(error) => {
            eprintln!("could not listen on {}: {}", address, error);
            std::process::exit(1);
        }
    };
    let local = source
        .socket
        .local_addr()
        .map(|address| address.to_string())
        .unwrap_or_else(|_| address.to_string());
    println!("listening on {} - press Ctrl-C to stop", local);

    let mut capture = LiveCapture::new();
    let mut packets: Vec<Packet> = Vec::new();

    loop {
        // The datagrams that arrived are put in the capture and kept for
        // the summary.
        let mut taken = 0;
        while let Some(packet) = source.next_packet() {
            capture.push(packet.clone());
            packets.push(packet);
            taken += 1;
        }

        if taken > 0 {
            let _ = summarize(&packets);
            println!(
                "packets: {}  bytes: {}  busiest second: {}",
                capture.packets(),
                capture.bytes(),
                capture
                    .busiest_second()
                    .map(|sample| format!("{} bytes", sample.bytes))
                    .unwrap_or_else(|| "-".to_string())
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

This lesson ties its explanation to `README.md`, `src/lib.rs`, `src/main.rs`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
