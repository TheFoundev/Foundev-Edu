# Toy Web Browser Engine

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

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
The stack i

## Actual features and limits

README feature statements (verify each against code before relying on it):
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
- Malformed HTML is handled leniently; the full HTML5 tree-construction algorithm (active formatting elements, adoption agency) is not implemented.

The implementation inventory includes 19 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `the repository dependency/configuration files`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `Cargo.lock`
- `Cargo.toml`
- `README.md`
- `src/css.rs`
- `src/dom.rs`
- `src/fetch.rs`
- `src/layout.rs`
- `src/lib.rs`
- `src/main.rs`
- `src/tokenizer.rs`
- `tests/integration.rs`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: tests/integration.rs. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
