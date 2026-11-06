# A beginner's model of main

**Lesson ID:** `sniffnet-module-02-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/main.rs]. Trace its declarations and dependencies into a caller or test. Inspect imports, declarations, and call sites in the file; filenames alone do not establish its role.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/main.rs`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

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

This lesson ties its explanation to `src/main.rs`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
