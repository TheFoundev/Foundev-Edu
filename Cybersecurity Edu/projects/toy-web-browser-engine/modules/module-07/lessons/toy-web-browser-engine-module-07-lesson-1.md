# A beginner's model of documented goals mapped to implementation

**Lesson ID:** `toy-web-browser-engine-module-07-lesson-1`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors src/css.rs, src/dom.rs, src/fetch.rs. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `README.md`, `src/css.rs`, `src/dom.rs`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/css.rs`, `use std::collections::HashMap;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/css.rs`, `use crate::dom::{is_invisible_element, is_void_element, Node, NodeKind};` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/dom.rs`, `use crate::tokenizer::{tokenize, Token};` brings a module or package name into this file; follow later references before claiming it is used on a running path.

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
# Toy Web Browser Engine

A small, self-contained browser engine in Rust: HTML tokenizer, DOM tree builder, HTML serializer, CSS cascade with selector matching, a CSS box-model layout engine and an HTTP fetcher.

## Overview

An original implementation of the **Toy Web Browser Engine** concept, built for the Foundev portfolio. The pipeline mirrors what a real engine does, in a size you can read end to end:

```text
HTML text ──▶ tokenizer ──▶ tree builder ──▶ DOM ──▶ serializer
                                    │
                                    ├──▶ CSS parser ──▶ selector matching ──▶ computed styles
                                    └──▶ layout engine ──▶ boxes (content/padding/border/margin)
```

## Features

- HTML tokenizer with tags, attributes, text, comments, doctypes and self-closing tags
- Attribute values may contain spaces, `>` characters and character references
- Entity decoding for text and attribute values (named and numeric)
- Tree builder with void-element handling, implicit end tags and stray end-tag recovery
- DOM with element, text and comment nodes
- HTML serializer that round-trips the parsed document
- CSS parser: rules, declarations, comments, selector lists
- Selector matching for type, `.class`, `#id` and descendant combinators, with specificity-based cascade and property inheritance
- Layout engine implementing the CSS box model (content-box and border-box), margin/border/padding, percentage widths and block flow
- HTTP fetching with URL resolution for relative links and assets
- 34 unit and integration tests

## Stack

`Rust`
The stack is Rust. The engine depends on `reqwest` (blocking client with rustls) and `url` (RFC 3986 URL parsing and resolution); everything else is handwritten.

## Run

```bash
cargo run --release                       # render the built-in sample page
cargo run -- --file page.html             # render a local HTML file
cargo run -- --fetch https://example.com  # download a page and resolve its links
```

## Structure

```text
toy-web-browser-engine/
├── src/lib.rs           public API (parse, render_page, re-exports)
├── src/tokenizer.rs     HTML tokenizer and entity decoding
├── src/dom.rs           DOM tree, tree builder and serializer
├── src/css.rs           stylesheet parsing, selector matching and cascade
├── src/layout.rs        box model and block layout
├── src/fetch.rs         HTTP fetching and URL resolution
├── src/main.rs          command line demo
├── tests/integration.rs end-to-end tests
└── Cargo.toml
```

## Testing

```bash
cargo test
```

The suite covers the tokenizer (quoted attributes, entities, self-closing tags, stray `<`), the tree builder (void elements, implicit closes, unmatched end tags), the serializer (round-trip and escaping), CSS (parsing, specificity, inheritance, lengths), the box model (content-box, border-box, auto width, percentages, vertical stacking) and fetching (URL resolution plus a real HTTP round-trip against a local server).

## Notes and limitations

- Malformed HTML is handled leniently; the full HTML5 tree-construction algorithm (active formatting elements, adoption agency) is not implemented.
- The layout engine implements block flow only: there is no inline layout, no flexbox or grid, no text measurement and no painting.
- CSS support covers type, class, id and descendant selectors; attribute selectors, pseudo-classes and at-rules are not implemented.
- There is no JavaScript engine.
- `reqwest` is used with the `rustls-tls` backend; plain HTTP and HTTPS are supported.

## License

MIT. See `LICENSE`.

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

### src/dom.rs

```text
//! DOM tree, tree builder and HTML serializer.

use crate::tokenizer::{tokenize, Token};

/// The kind of a DOM node.
#[derive(Clone, Debug, PartialEq, Eq)]
pub enum NodeKind {
    Document,
    Element,
    Text,
    Comment,
}

/// A node in the document tree.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Node {
    pub kind: NodeKind,
    /// Tag name for elements, empty for text/comment nodes.
    pub name: String,
    pub attributes: Vec<(String, String)>,
    /// Raw text of a text or comment node.
    pub text: String,
    pub children: Vec<Node>,
}

impl Node {
    /// Create an element node.
    pub fn element(name: &str) -> Node {
        Node {
            kind: NodeKind::Element,
            name: name.to_string(),
            attributes: Vec::new(),
            text: String::new(),
            children: Vec::new(),
        }
    }

    /// Create a text node.
    pub fn text_node(text: &str) -> Node {
        Node {
            kind: NodeKind::Text,
            name: "#text".to_string(),
            attributes: Vec::new(),
            text: text.to_string(),
            children: Vec::new(),
        }
    }

    /// Create a comment node.
    pub fn comment(text: &str) -> Node {
        Node {
            kind: NodeKind::Comment,
            name: "#comment".to_string(),
            attributes: Vec::new(),
            text: text.to_string(),
            children: Vec::new(),
        }
    }

    /// Value of an attribute, if present.
    pub fn attribute(&self, name: &str) -> Option<&str> {
        self.attributes
            .iter()
            .find(|(key, _)| key == name)
            .map(|(_, value)| value.as_str())
    }

    /// All classes listed in the `class` attribute.
    pub fn classes(&self) -> Vec<String> {
        self.attribute("class")
            .map(|value| {
                value
                    .split_whitespace()
                    .map(|class| class.to_string())
                    .collect()
            })
            .unwrap_or_default()
    }

    /// The visible text of this subtree.
    pub fn text_content(&self) -> String {
        text_content(self)
    }

    /// The raw text of this subtree, including invisible elements.
    pub fn raw_text(&self) -> String {
        let mut output = String::new();
        collect_raw_text(self, &mut output);
        output
    }

    /// Direct child elements with the given tag name.
    pub fn children_named(&self, name: &str) -> Vec<&Node> {
        self.children
            .iter()
            .filter(|child| child.kind == NodeKind::Element && child.name == name)
            .collect()
    }

    /// Depth-first search for the first descendant (or self) with `name`.
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

This lesson ties its explanation to `README.md`, `src/css.rs`, `src/dom.rs`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
