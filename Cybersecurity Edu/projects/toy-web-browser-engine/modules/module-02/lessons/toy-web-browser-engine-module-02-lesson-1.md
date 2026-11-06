# A beginner's model of dom and fetch

**Lesson ID:** `toy-web-browser-engine-module-02-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/dom.rs] and [src/fetch.rs]. Trace its declarations and dependencies into a caller or test. Inspect imports, declarations, and call sites in the file; filenames alone do not establish its role.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/dom.rs`, `src/fetch.rs`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/dom.rs`, `use crate::tokenizer::{tokenize, Token};` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/fetch.rs`, `use std::time::Duration;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/fetch.rs`, `use url::Url;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/fetch.rs`, `use crate::dom::{parse, Node};` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/fetch.rs`, `use super::*;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/fetch.rs`, `use std::io::{Read, Write};` brings a module or package name into this file; follow later references before claiming it is used on a running path.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### src/fetch.rs

```text
//! Fetching pages over HTTP and resolving relative URLs.

use std::time::Duration;

use url::Url;

use crate::dom::{parse, Node};

/// The outcome of a successful page fetch.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct FetchedPage {
    /// The final URL of the page (after redirects).
    pub url: String,
    pub status: u16,
    pub content_type: String,
    pub body: String,
}

/// Errors produced while fetching.
#[derive(Debug)]
pub enum FetchError {
    /// The URL could not be parsed.
    InvalidUrl(String),
    /// The request failed (DNS, TLS, connection, timeout, ...).
    Request(String),
}

impl std::fmt::Display for FetchError {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            FetchError::InvalidUrl(url) => write!(formatter, "invalid URL: {url}"),
            FetchError::Request(message) => write!(formatter, "request failed: {message}"),
        }
    }
}

impl std::error::Error for FetchError {}

/// Resolve a possibly relative `reference` against a `base` URL.
///
/// Absolute references are returned unchanged (normalized).
pub fn resolve_url(base: &str, reference: &str) -> Result<String, FetchError> {
    let reference = reference.trim();
    if reference.is_empty() {
        return Ok(base.to_string());
    }
    if let Ok(parsed_reference) = Url::parse(reference) {
        if parsed_reference.has_host() {
            return Ok(parsed_reference.to_string());
        }
    }
    let parsed_base = Url::parse(base).map_err(|_| FetchError::InvalidUrl(base.to_string()))?;
    parsed_base
        .join(reference)
        .map(|url| url.to_string())
        .map_err(|_| FetchError::InvalidUrl(reference.to_string()))
}

/// An HTTP client that can download pages.
pub struct Fetcher {
    client: reqwest::blocking::Client,
}

impl Fetcher {
    /// Create a fetcher with the given timeout and user agent.
    pub fn new(timeout: Duration, user_agent: &str) -> Fetcher {
        let client = reqwest::blocking::Client::builder()
            .timeout(timeout)
            .user_agent(user_agent)
            .build()
            .expect("failed to build the HTTP client");
        Fetcher { client }
    }

    /// Create a fetcher with the default timeout and user agent.
    pub fn default_fetcher() -> Fetcher {
        Fetcher::new(Duration::from_secs(30), "toy-web-browser-engine/0.1")
    }

    /// Download a page.
    pub fn fetch(&self, url: &str) -> Result<FetchedPage, FetchError> {
        let parsed = Url::parse(url).map_err(|_| FetchError::InvalidUrl(url.to_string()))?;
        let response = self
            .client
            .get(parsed)
            .send()
            .map_err(|error| FetchError::Request(error.to_string()))?;
        let status = response.status();
        let content_type = response
            .headers()
            .get(reqwest::header::CONTENT_TYPE)
            .and_then(|value| value.to_str().ok())
            .unwrap_or("text/html")
            .to_string();
        let body = response
            .text()
            .map_err(|error| FetchError::Request(error.to_string()))?;
        Ok(FetchedPage {
            url: url.to_string(),
            status: status.as_u16(),
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

This lesson ties its explanation to `src/dom.rs`, `src/fetch.rs`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
