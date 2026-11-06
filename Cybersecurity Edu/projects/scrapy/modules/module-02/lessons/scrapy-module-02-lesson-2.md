# Read pipeline and api impl in the source

**Lesson ID:** `scrapy-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/pipeline.py] and [web/api_impl.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include LinkParser, __init__, handle_starttag, handle_endtag, handle_data, make_site, QuietHandler, log_message, _number, _crawl, summary, handle; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/pipeline.py`, `web/api_impl.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

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
- In `web/api_impl.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from src.pipeline import run  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def _number(payload, key: str, default: int) -> int:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _crawl(base_dir: str = "artifacts") -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def handle(method, path, payload, user):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### web/api_impl.py

```text
"""The API of the crawler.

The numbers are the real ones: the site is written by the project, the
crawler of the project walks it and the index of the pages and the broken
links come out of that walk. The crawl is run inside the process that answers
the request, on a server of its own on the loopback interface, so no network
and no permission are needed.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.pipeline import run  # noqa: E402

#: The result of the last crawl, so a page does not crawl again for every call.
_CACHE: dict[str, dict] = {}


def _number(payload, key: str, default: int) -> int:
    """One number of the request.

    The query string of a GET arrives as a dictionary of lists, so the first
    value of the list is taken.
    """
    value = (payload or {}).get(key, default)
    if isinstance(value, (list, tuple)):
        value = value[0] if value else default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _crawl(base_dir: str = "artifacts") -> dict:
    """The crawl of the site, with the index and the broken links."""
    key = str(base_dir)
    if key not in _CACHE:
        summary = run(quick=False, base_dir=base_dir)
        pages = []
        index = Path(base_dir) / "pages.jsonl"
        if index.exists():
            import json

            for line in index.read_text(encoding="utf-8").strip().splitlines():
                if line:
                    row = json.loads(line)
                    pages.append({
                        "page": row["url"],
                        "title": row["title"] or "(no title)",
                        "links": row["links"],
                    })
        broken = []
        broken_file = Path(base_dir) / "broken.txt"
        if broken_file.exists():
            for line in broken_file.read_text(encoding="utf-8").strip().splitlines():
                if line:
                    broken.append({"broken link": line})
        _CACHE[key] = {"summary": summary, "pages": pages, "broken": broken}
    return _CACHE[key]


def summary():
    state = _crawl()
    numbers = state["summary"]
    pages = state["pages"]

    return {
        "stats": {
            "crawled_pages": numbers["crawled_pages"],
            "links_seen": numbers["links_seen"],
            "broken_links": numbers["broken_links"],
            "generated_pages": numbers["generated_pages"],
        },
        "series": [
            {"label": row["title"], "value": row["links"]}
            for row in pages
        ],
        "lists": {
            "pages": pages,
            "broken": state["broken"],
        },
    }


def handle(method, path, payload, user):
    if method == "GET" and path == "/api/pages":
        return 200, {"pages": _crawl()["pages"]}

    if method == "GET" and path == "/api/broken":
        return 200, {"broken": _crawl()["broken"]}

    if method == "POST" and path == "/api/crawl":
        _CACHE.clear()
        state = summary()
        return 200, {"crawled": True, "summary": state}

    return 404, {"error": "not found"}
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

This lesson ties its explanation to `src/pipeline.py`, `web/api_impl.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
