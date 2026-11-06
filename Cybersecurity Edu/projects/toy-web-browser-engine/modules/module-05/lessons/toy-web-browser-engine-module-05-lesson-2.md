# Read test code and implementation evidence in the source

**Lesson ID:** `toy-web-browser-engine-module-05-lesson-2`

## Purpose and learning objectives

Read the test cases in tests/integration.rs beside the implementation in src/css.rs. Explain the behavior asserted by the tests and trace each assertion to the implementation. A test file describes a check; it does not prove that check passed.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `tests/integration.rs`, `src/css.rs`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `tests/integration.rs`, `use toy_web_browser_engine::fetch::{resolve_links, Fetcher};` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/integration.rs`, `use toy_web_browser_engine::{layout, parse, parse_stylesheet, render, serialize};` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/integration.rs`, `use std::io::{Read, Write};` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/integration.rs`, `use std::net::TcpListener;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/integration.rs`, `use std::thread;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
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

### tests/integration.rs

```text
use toy_web_browser_engine::fetch::{resolve_links, Fetcher};
use toy_web_browser_engine::{layout, parse, parse_stylesheet, render, serialize};

const PAGE: &str = r#"<!doctype html>
<html>
  <head>
    <title>Demo</title>
    <style>
      body { margin: 0 }
      .card { padding: 10px; border-width: 2px }
      #hero { width: 400px; height: 50px }
    </style>
  </head>
  <body>
    <h1 id="hero">Hello</h1>
    <p class="card">Body text</p>
    <a href="/next">next</a>
  </body>
</html>"#;

#[test]
fn parses_and_serializes_a_full_page() {
    let document = parse(PAGE);
    assert!(document.find("title").is_some());
    let serialized = serialize(&document);
    assert!(serialized.contains("<title>Demo</title>"));
    assert!(serialized.contains("id=\"hero\""));
    // The document must round-trip.
    assert_eq!(parse(&serialized), document);
}

#[test]
fn renders_visible_text_only() {
    let text = render(PAGE);
    assert!(text.contains("Hello"));
    assert!(text.contains("Body text"));
    assert!(!text.contains("body { margin"));
}

#[test]
fn applies_the_box_model() {
    let document = parse(PAGE);
    let rules = parse_stylesheet("body { margin: 0 } .card { padding: 10px; border-width: 2px } #hero { width: 400px; height: 50px }");
    let boxes = layout(&document, &rules, 800.0);

    let hero = boxes
        .iter()
        .find(|entry| entry.id.as_deref() == Some("hero"))
        .unwrap();
    assert_eq!(hero.metrics.content_width, 400.0);
    assert_eq!(hero.metrics.content_height, 50.0);

    let card = boxes.iter().find(|entry| entry.name == "p").unwrap();
    // Auto width shrinks the content box so that the border box fills the
    // containing block.
    assert_eq!(card.width(), 800.0);
    assert_eq!(card.metrics.content_width, 800.0 - 20.0 - 4.0);
    assert_eq!(card.metrics.padding.top, 10.0);
    assert_eq!(card.metrics.border.left, 2.0);
}

#[test]
fn resolves_links_against_the_page_url() {
    let document = parse(PAGE);
    let links = resolve_links(&document, "https://example.com/docs/index.html");
    assert_eq!(links, vec!["https://example.com/next".to_string()]);
}

#[test]
fn fetches_a_page_from_a_local_server() {
    use std::io::{Read, Write};
    use std::net::TcpListener;
    use std::thread;

    let listener = TcpListener::bind("127.0.0.1:0").expect("bind");
    let address = listener.local_addr().expect("addr");
    let handle = thread::spawn(move || {
        let (mut stream, _) = listener.accept().expect("accept");
        let mut buffer = [0u8; 1024];
        let _ = stream.read(&mut buffer);
        let body = "<html><body><h1>Remote</h1></body></html>";
        let response = format!(
            "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{}",
            body.len(),
            body
        );
        let _ = stream.write_all(response.as_bytes());
        let _ = stream.flush();
    });

    let url = format!("http://{address}/");
    let fetcher = Fetcher::default_fetcher();
    let (document, page) = fetcher.fetch_document(&url).expect("fetch");
    assert_eq!(page.status, 200);
    assert!(document.find("h1").is_some());
    assert!(render(&page.body).contains("Remote"));
    let _ = handle.join();
}

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

This lesson ties its explanation to `tests/integration.rs`, `src/css.rs`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
