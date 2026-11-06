# Read documented goals mapped to implementation in the source

**Lesson ID:** `scrapy-module-05-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors main.py, src/pipeline.py, web/api_impl.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `main.py`, `src/pipeline.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import threading` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import urllib.error` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import urllib.parse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import urllib.request` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class LinkParser(HTMLParser):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def handle_starttag(self, tag, attrs):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def handle_endtag(self, tag):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def handle_data(self, data):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def make_site(base, quick=True):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
# Scrapy

A small breadth-first crawler over a locally served site.

> A fast crawling framework used to build polite web spiders that scope authorised reconnaissance targets.

## Overview

An original, self-contained implementation of the **Scrapy** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Generated test site served on localhost
- HTML parser for titles, links and paragraphs
- Breadth-first crawl with a depth limit
- JSONL page index and broken-link report

## Stack

`Python`
The CSV stack is Python. Scrapy and Twisted are not installed, so this build uses urllib, html.parser and the standard library HTTP server.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
scrapy/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
pytest -q
```

6 tests (`pytest -q`), up from 2: the crawl, the depth, the limit and the broken links.


## Notes and limitations

- There is no scheduler, retry middleware, robots.txt handling or CSS selector language.
- The crawl target is a generated local site.
- Only same-host links are followed.

## License

BSD-3-Clause. See `LICENSE`.

## About the scope

This is a third-year student project, not a production data platform. It uses local files and SQLite so the pipeline can run on one machine. The notes above list the production pieces that were replaced or skipped.

```

### main.py

```text
"""Pipeline entry point. Run `python main.py run` or `python main.py demo`."""
import argparse
import json

from src.pipeline import run, demo


def main() -> None:
    parser = argparse.ArgumentParser(description='Crawl a small local site and index its pages.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Crawl a small local site and index its pages.')
        print("Run `python main.py run` to execute the pipeline.")
        return

    if args.command == "demo":
        demo(base_dir=args.base_dir)
        return

    summary = run(quick=args.quick, base_dir=args.base_dir)
    print(json.dumps(summary, indent=2, default=str))


if __name__ == "__main__":
    main()

```

### src/pipeline.py

```text
"""A small same-host crawler with an HTML link parser."""
import json
import threading
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "a" and attributes.get("href"):
            self.links.append(attributes["href"])
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data.strip()


def make_site(base, quick=True):
    site = base / "site"
    (site / "guides").mkdir(parents=True, exist_ok=True)
    pages = {
        "index.html": '<title>Home</title><a href="guides/start.html">start</a>'
                      '<a href="guides/tools.html">tools</a><a href="missing.html">missing</a>',
        "guides/start.html": '<title>Start</title><a href="../index.html">home</a>'
                             '<a href="tools.html">tools</a>',
        "guides/tools.html": '<title>Tools</title><a href="start.html">start</a>'
                             '<a href="../index.html">home</a>',
    }
    if not quick:
        pages["guides/notes.html"] = '<title>Notes</title><a href="tools.html">tools</a>'
    for name, html in pages.items():
        (site / name).write_text(f"<!doctype html><html><body>{html}</body></html>", encoding="utf-8")
    return site, len(pages)


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def crawl(root, max_depth=2, limit=20):
    seen = {}
    broken = []
    # The root is a path and the urls are strings, so the first url is built
    # from the path.
    start = str(root).rstrip("/") + "/index.html"
    queue = [(start, 0)]
    while queue and len(seen) < limit:
        url, depth = queue.pop(0)
        if url in seen:
            continue
        try:
            with urllib.request.urlopen(url, timeout=3) as response:
                body = response.read().decode("utf-8", errors="replace")
        except (urllib.error.URLError, OSError):
            broken.append(url)
            continue

        parser = LinkParser()
        parser.feed(body)
        seen[url] = {"title": parser.title, "links": len(parser.links)}
        if depth < max_depth:
            for link in parser.links:
                if link.startswith("http"):
                    continue
                target = urllib.parse.urljoin(url, link)
                if target.startswith(root):
                    queue.append((target, depth + 1))
    return seen, broken


def run(quick=False, base_dir="artifacts"):
    base = Path(base_dir)
    base.mkdir(parents=True, exist_ok=True)
    site, page_count = make_site(base, quick=quick)

    handler = lambda *args, **kwargs: QuietHandler(*args, directory=str(site), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        seen, broken = crawl(f"http://127.0.0.1:{port}", max_depth=3 if quick else 4)
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

This lesson ties its explanation to `README.md`, `main.py`, `src/pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
