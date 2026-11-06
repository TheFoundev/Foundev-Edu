# A beginner's model of code review and safe change 6

**Lesson ID:** `scrapy-module-06-lesson-1`

## Purpose and learning objectives

Use main.py to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

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
- In `tests/test_pipeline.py`, `import threading` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from http.server import ThreadingHTTPServer` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import QuietHandler, crawl, demo, make_site, run` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def _serve(directory):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_site_is_crawled(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_depth_is_respected(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_limit_is_respected(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_missing_page_is_reported(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### tests/test_pipeline.py

```text
"""Tests for the crawler."""
import threading
from http.server import ThreadingHTTPServer

from src.pipeline import QuietHandler, crawl, demo, make_site, run


def _serve(directory):
    """A server for the site, and the port it listens on."""
    handler = lambda *args, **kwargs: QuietHandler(*args, directory=str(directory), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, server.server_address[1], thread


def test_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


def test_the_site_is_crawled(tmp_path):
    site, _ = make_site(tmp_path, quick=True)
    server, port, _thread = _serve(site)
    try:
        seen, _broken = crawl(f"http://127.0.0.1:{port}", max_depth=2, limit=20)
    finally:
        server.shutdown()
        server.server_close()

    assert seen
    assert all("title" in page for page in seen.values())
    assert all(url.startswith("http://") for url in seen)


def test_the_depth_is_respected(tmp_path):
    site, _ = make_site(tmp_path, quick=True)
    server, port, _thread = _serve(site)
    try:
        shallow, _ = crawl(f"http://127.0.0.1:{port}", max_depth=1, limit=50)
        deep, _ = crawl(f"http://127.0.0.1:{port}", max_depth=3, limit=50)
    finally:
        server.shutdown()
        server.server_close()

    assert len(shallow) <= len(deep)


def test_the_limit_is_respected(tmp_path):
    site, _ = make_site(tmp_path, quick=True)
    server, port, _thread = _serve(site)
    try:
        seen, _ = crawl(f"http://127.0.0.1:{port}", max_depth=3, limit=3)
    finally:
        server.shutdown()
        server.server_close()

    assert len(seen) <= 3


def test_the_missing_page_is_reported(tmp_path):
    site, _ = make_site(tmp_path, quick=True)
    server, port, _thread = _serve(site)
    try:
        _seen, broken = crawl(f"http://127.0.0.1:{port}", max_depth=2, limit=20)
    finally:
        server.shutdown()
        server.server_close()

    assert any("missing" in url for url in broken)

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

This lesson ties its explanation to `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
