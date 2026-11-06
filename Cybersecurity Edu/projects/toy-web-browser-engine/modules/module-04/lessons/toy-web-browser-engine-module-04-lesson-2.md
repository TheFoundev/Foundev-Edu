# Read main and tokenizer in the source

**Lesson ID:** `toy-web-browser-engine-module-04-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/main.rs] and [src/tokenizer.rs]. Trace its declarations and dependencies into a caller or test. Inspect imports, declarations, and call sites in the file; filenames alone do not establish its role.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/main.rs`, `src/tokenizer.rs`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/main.rs`, `use toy_web_browser_engine::{` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/tokenizer.rs`, `use std::collections::HashMap;` brings a module or package name into this file; follow later references before claiming it is used on a running path.

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
use toy_web_browser_engine::{
    fetch::Fetcher, layout::layout, parse, parse_stylesheet, render, tokenize,
};

const SAMPLE: &str = "<!doctype html><html><head><title>Demo</title></head><body><!-- page --><h1>Hello</h1><p>A tiny browser engine.</p><a href=\"https://example.com\">link</a></body></html>";

fn main() {
    let arguments: Vec<String> = std::env::args().collect();
    let mut fetch_url: Option<String> = None;
    let mut file_path: Option<String> = None;
    let mut index = 1;
    while index < arguments.len() {
        match arguments[index].as_str() {
            "--fetch" => {
                index += 1;
                fetch_url = arguments.get(index).cloned();
            }
            "--file" => {
                index += 1;
                file_path = arguments.get(index).cloned();
            }
            "--help" | "-h" => {
                println!("usage: toy_web_browser_engine [--fetch <url>] [--file <path>]");
                return;
            }
            other => {
                if other.starts_with("http://") || other.starts_with("https://") {
                    fetch_url = Some(other.to_string());
                } else {
                    file_path = Some(other.to_string());
                }
            }
        }
        index += 1;
    }

    let (html, base_url) = match (&fetch_url, &file_path) {
        (Some(url), _) => {
            let fetcher = Fetcher::default_fetcher();
            match fetcher.fetch(url) {
                Ok(page) => (page.body, Some(page.url)),
                Err(error) => {
                    eprintln!("could not fetch {}: {}", url, error);
                    std::process::exit(1);
                }
            }
        }
        (None, Some(path)) => {
            let html = std::fs::read_to_string(path).unwrap_or_else(|error| {
                eprintln!("could not read {}: {}", path, error);
                std::process::exit(1);
            });
            (html, None)
        }
        (None, None) => (SAMPLE.to_string(), None),
    };

    println!("tokens: {}", tokenize(&html).len());

    let document = parse(&html);
    let rules = parse_stylesheet("");
    let boxes = layout(&document, &rules, 1024.0);
    println!("boxes: {}", boxes.len());
    for entry in &boxes {
        println!(
            "  <{}> x={:.0} y={:.0} w={:.0} h={:.0}",
            entry.name,
            entry.x,
            entry.y,
            entry.width(),
            entry.height()
        );
    }

    if let Some(base) = base_url {
        let links = toy_web_browser_engine::fetch::resolve_links(&document, &base);
        println!("--- resolved links ---");
        for link in links {
            println!("  {link}");
        }
    }

    println!("--- rendered text ---");
    print!("{}", render(&html));
}

```

### src/tokenizer.rs

```text
//! HTML tokenizer.
//!
//! The tokenizer turns a byte string into a flat list of tokens. It is
//! intentionally forgiving (like the HTML5 tokenizer in "script data" states
//! it is not) but it does implement the parts of the spec that matter for a
//! usable browser engine:
//!
//! * quoted attribute values may contain spaces and `>` characters,
//! * attribute values and text are entity-decoded,
//! * comments, doctypes and bogus comments are recognised,
//! * `<` followed by a non-letter is treated as literal text.

use std::collections::HashMap;

/// A single token produced by [`tokenize`].
#[derive(Clone, Debug, PartialEq, Eq)]
pub enum Token {
    Doctype,
    Comment(String),
    OpenTag {
        name: String,
        attributes: Vec<(String, String)>,
        self_closing: bool,
    },
    CloseTag(String),
    Text(String),
}

impl Token {
    /// Convenience accessor for the tag name of an open tag.
    pub fn open_tag_name(&self) -> Option<&str> {
        match self {
            Token:[REDACTED] { name, .. } => Some(name.as_str()),
            _ => None,
        }
    }
}

const NAMED_ENTITIES: &[(&str, &str)] = &[
    ("amp", "&"),
    ("lt", "<"),
    ("gt", ">"),
    ("quot", "\""),
    ("apos", "'"),
    ("nbsp", "\u{a0}"),
    ("copy", "\u{a9}"),
    ("reg", "\u{ae}"),
    ("hellip", "\u{2026}"),
    ("mdash", "\u{2014}"),
    ("ndash", "\u{2013}"),
    ("lsquo", "\u{2018}"),
    ("rsquo", "\u{2019}"),
    ("ldquo", "\u{201c}"),
    ("rdquo", "\u{201d}"),
    ("trade", "\u{2122}"),
    ("euro", "\u{20ac}"),
    ("pound", "\u{a3}"),
    ("yen", "\u{a5}"),
    ("sect", "\u{a7}"),
    ("para", "\u{b6}"),
    ("middot", "\u{b7}"),
    ("bull", "\u{2022}"),
    ("dagger", "\u{2020}"),
    ("permil", "\u{2030}"),
    ("deg", "\u{b0}"),
    ("plusmn", "\u{b1}"),
    ("times", "\u{d7}"),
    ("divide", "\u{f7}"),
    ("frac12", "\u{bd}"),
    ("frac14", "\u{bc}"),
    ("frac34", "\u{be}"),
    ("sup2", "\u{b2}"),
    ("sup3", "\u{b3}"),
    ("micro", "\u{b5}"),
    ("alpha", "\u{3b1}"),
    ("beta", "\u{3b2}"),
    ("gamma", "\u{3b3}"),
    ("delta", "\u{3b4}"),
    ("pi", "\u{3c0}"),
    ("sigma", "\u{3c3}"),
    ("omega", "\u{3c9}"),
    ("larr", "\u{2190}"),
    ("uarr", "\u{2191}"),
    ("rarr", "\u{2192}"),
    ("darr", "\u{2193}"),
    ("harr", "\u{2194}"),
    ("spades", "\u{2660}"),
    ("clubs", "\u{2663}"),
    ("hearts", "\u{2665}"),
    ("diams", "\u{2666}"),
];

/// Decode HTML character references in `input`.
///
/// Numeric references (`&#65;` and `&#x41;`) and the common named
/// references are supported. Unknown references are left untouched, which
/// matches browser behaviour.
pub fn decode_entities(input: &str) -> String {
    if !input.contains('&') {
        return input.to_string();
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

This lesson ties its explanation to `src/main.rs`, `src/tokenizer.rs`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
