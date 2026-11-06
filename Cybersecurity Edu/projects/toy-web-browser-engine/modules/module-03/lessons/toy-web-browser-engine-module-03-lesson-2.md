# Read layout and lib in the source

**Lesson ID:** `toy-web-browser-engine-module-03-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/layout.rs] and [src/lib.rs]. Trace its declarations and dependencies into a caller or test. Inspect imports, declarations, and call sites in the file; filenames alone do not establish its role.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/layout.rs`, `src/lib.rs`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/layout.rs`, `use crate::css::{compute_all_styles, ComputedStyle, StyleRule};` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/layout.rs`, `use crate::dom::{is_invisible_element, is_void_element, Node, NodeKind};` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/layout.rs`, `use super::*;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/layout.rs`, `use crate::css::parse_stylesheet;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/layout.rs`, `use crate::dom::parse;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/lib.rs`, `use super::*;` brings a module or package name into this file; follow later references before claiming it is used on a running path.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/layout.rs

```text
//! A small block-layout engine implementing the CSS box model.

use crate::css::{compute_all_styles, ComputedStyle, StyleRule};
use crate::dom::{is_invisible_element, is_void_element, Node, NodeKind};

/// The four sides of a box.
#[derive(Clone, Copy, Debug, Default, PartialEq)]
pub struct Edges {
    pub top: f64,
    pub right: f64,
    pub bottom: f64,
    pub left: f64,
}

impl Edges {
    /// Build edges from a CSS shorthand such as `1px 2px` or `1px 2px 3px 4px`.
    pub fn from_shorthand(value: &str) -> Edges {
        let mut parts = Vec::new();
        for part in value.split_whitespace() {
            if let Ok(number) = part.trim_end_matches("px").parse::<f64>() {
                parts.push(number);
            }
        }
        match parts.len() {
            0 => Edges::default(),
            1 => Edges {
                top: parts[0],
                right: parts[0],
                bottom: parts[0],
                left: parts[0],
            },
            2 => Edges {
                top: parts[0],
                right: parts[1],
                bottom: parts[0],
                left: parts[1],
            },
            3 => Edges {
                top: parts[0],
                right: parts[1],
                bottom: parts[2],
                left: parts[1],
            },
            _ => Edges {
                top: parts[0],
                right: parts[1],
                bottom: parts[2],
                left: parts[3],
            },
        }
    }
}

/// The computed geometry of a single box.
#[derive(Clone, Debug, PartialEq)]
pub struct BoxMetrics {
    pub margin: Edges,
    pub border: Edges,
    pub padding: Edges,
    /// Width of the content box in pixels.
    pub content_width: f64,
    /// Height of the content box in pixels.
    pub content_height: f64,
}

impl BoxMetrics {
    /// Total width of the box including margin, border and padding.
    pub fn total_width(&self) -> f64 {
        self.content_width
            + self.padding.left
            + self.padding.right
            + self.border.left
            + self.border.right
            + self.margin.left
            + self.margin.right
    }

    /// Total height of the box including margin, border and padding.
    pub fn total_height(&self) -> f64 {
        self.content_height
            + self.padding.top
            + self.padding.bottom
            + self.border.top
            + self.border.bottom
            + self.margin.top
            + self.margin.bottom
    }
}

/// A box placed on the canvas.
#[derive(Clone, Debug, PartialEq)]
pub struct LayoutBox {
    /// Tag name of the element.
    pub name: String,
    /// `id` attribute, when present.
    pub id: Option<String>,
    pub x: f64,
    pub y: f64,
    pub metrics: BoxMetrics,
}
```

### src/lib.rs

```text
//! A toy browser engine.
//!
//! The crate provides a small but complete pipeline:
//!
//! * [`tokenizer`] turns HTML text into tokens,
//! * [`dom`] builds a tree from those tokens and serializes it back to HTML,
//! * [`css`] parses stylesheets, matches selectors and computes styles,
//! * [`layout`] implements the CSS box model and a block layout algorithm,
//! * [`fetch`] downloads pages and resolves relative URLs.

pub mod css;
pub mod dom;
pub mod fetch;
pub mod layout;
pub mod tokenizer;

pub use css::{compute_style, parse_stylesheet, ComputedStyle, Selector, StyleRule};
pub use dom::{parse, render, serialize, text_content, Node, NodeKind};
pub use fetch::{resolve_url, Fetcher};
pub use layout::{layout, BoxMetrics, Edges, LayoutBox};
pub use tokenizer::{decode_entities, tokenize, Token};

/// Everything needed to display a page: its tree, its styles and its layout.
pub struct RenderedPage {
    pub document: Node,
    pub rules: Vec<StyleRule>,
    pub boxes: Vec<LayoutBox>,
    pub text: String,
}

/// The CSS contained in the `<style>` elements of a document.
pub fn extract_styles(document: &Node) -> String {
    document
        .elements()
        .into_iter()
        .filter(|node| node.name == "style")
        .map(|node| node.raw_text())
        .collect::<Vec<String>>()
        .join("\n")
}

/// Parse HTML, apply a stylesheet and lay the document out.
///
/// Stylesheets inside `<style>` elements of the document are applied before
/// the stylesheet passed in `css`.
pub fn render_page(html: &str, css: &str, viewport_width: f64) -> RenderedPage {
    let document = parse(html);
    let inline_css = extract_styles(&document);
    let mut combined = inline_css;
    if !css.trim().is_empty() {
        combined.push('\n');
        combined.push_str(css);
    }
    let rules = parse_stylesheet(&combined);
    let boxes = layout(&document, &rules, viewport_width);
    let text = text_content(&document);
    RenderedPage {
        document,
        rules,
        boxes,
        text,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn end_to_end_render_of_a_document() {
        let page = render_page(
            "<html><head><style>p { color: red; width: 200px }</style></head>\
             <body><h1>Title</h1><p class=\"lead\">Body text</p></body></html>",
            "p.lead { color: blue }",
            800.0,
        );
        assert!(page.text.contains("Title"));
        assert!(page.text.contains("Body text"));
        let paragraph = page
            .boxes
            .iter()
            .find(|entry| entry.name == "p")
            .expect("p box");
        assert_eq!(paragraph.metrics.content_width, 200.0);
        assert_eq!(page.rules.len(), 2);
    }
}

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

This lesson ties its explanation to `src/layout.rs`, `src/lib.rs`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
