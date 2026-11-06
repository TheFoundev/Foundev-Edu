# A beginner's model of pipeline and api impl

**Lesson ID:** `dnstwist-module-02-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/pipeline.py] and [web/api_impl.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include split_domain, permutations, probe, lookup, run, demo, scan, state, families; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/pipeline.py`, `web/api_impl.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/pipeline.py`, `import socket` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import threading` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from concurrent.futures import ThreadPoolExecutor` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def split_domain(domain):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def permutations(domain):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def probe(host, timeout=1.5):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def lookup():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def run(quick=False, base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def demo(base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `web/api_impl.py`, `from __future__ import annotations` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import csv` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from concurrent.futures import ThreadPoolExecutor` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def scan(domain: str) -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def state() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def families(domain: str) -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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
"""Domain permutation and a simple DNS probe."""
import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

KEYBOARD = {
    "a": "s", "s": "a", "d": "s", "f": "g", "g": "h", "h": "g", "j": "k",
    "q": "w", "w": "q", "e": "r", "r": "e", "t": "y", "y": "t",
    "u": "i", "i": "o", "o": "p", "p": "o", "z": "x", "x": "z",
    "c": "v", "v": "c", "b": "n", "n": "b", "m": "n",
}
HOMOGLYPHS = {"o": "0", "l": "1", "i": "1", "e": "3", "a": "4", "s": "5"}
TLDS = ["com", "net", "org", "io"]


def split_domain(domain):
    parts = domain.split(".")
    return parts[0], ".".join(parts[1:])


def permutations(domain):
    name, tld = split_domain(domain)
    results = set()
    for index in range(len(name)):
        results.add(name[:index] + name[index + 1:] + "." + tld)
        results.add(name[:index] + name[index] * 2 + name[index + 1:] + "." + tld)
        if name[index] in KEYBOARD:
            results.add(name[:index] + KEYBOARD[name[index]] + name[index + 1:] + "." + tld)
        if name[index] in HOMOGLYPHS:
            results.add(name[:index] + HOMOGLYPHS[name[index]] + name[index + 1:] + "." + tld)
    for index in range(len(name) - 1):
        swapped = name[:index] + name[index + 1] + name[index] + name[index + 2:]
        results.add(swapped + "." + tld)
    for other in TLDS:
        results.add(name + "." + other)
    results.discard(domain)
    return sorted(results)


def probe(host, timeout=1.5):
    """The address of a host, or None when there is none.

    The lookup runs in a thread that is given the time it may take, so the
    timeout belongs to this call and not to the whole process.
    """
    answer = {}

    def lookup():
        try:
            answer["address"] = socket.gethostbyname(host)
        except (socket.gaierror, socket.timeout, OSError):
            answer["address"] = None

    worker = threading.Thread(target=lookup, daemon=True)
    worker.start()
    worker.join(timeout)
    return answer.get("address")


def run(quick=False, base_dir="artifacts"):
    base = Path(base_dir)
    base.mkdir(parents=True, exist_ok=True)
    # A domain that really exists, so the demo shows what a result looks
    # like. A name under .test never resolves.
    domain = "example.com"
    candidates = permutations(domain)
    if quick:
        candidates = candidates[:12]
    rows = []
    with ThreadPoolExecutor(max_workers=16) as pool:
        addresses = list(pool.map(probe, candidates))
    for candidate, address in zip(candidates, addresses):
        rows.append({"domain": candidate, "resolved": bool(address), "address": address or ""})

    report = base / "candidates.csv"
    report.write_text(
        "domain,resolved,address\n" + "\n".join(
            f"{row['domain']},{int(row['resolved'])},{row['address']}" for row in rows
        ) + "\n",
        encoding="utf-8",
    )
    resolved = [row for row in rows if row["resolved"]]
    return {
        "domain": domain,
        "candidates": len(rows),
        "resolved": len(resolved),
        "unresolved": len(rows) - len(resolved),
        "sample": rows[0]["domain"] if rows else "",
        "report": str(report),
    }


def demo(base_dir="artifacts"):
    summary = run(quick=True, base_dir=base_dir)
    rows = (Path(base_dir) / "candidates.csv").read_text().strip().splitlines()[1:]
    print(f"Generated {summary['candidates']} candidates for {summary['domain']}")
    for line in rows[:10]:
        print("  " + line)
    print(f"Resolved: {summary['resolved']}, unresolved: {summary['unresolved']}")
```

### web/api_impl.py

```text
"""The API of the project: the typosquatting candidates of a domain.

The numbers come from the real engine of the project: the permutations are
built by `permutations()` and every candidate is looked up by `probe()`, the
same way `run()` of the project does it.
"""

from __future__ import annotations

import csv
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import (  # noqa: E402
    HOMOGLYPHS,
    KEYBOARD,
    TLDS,
    permutations,
    probe,
    run,
    split_domain,
)

#: Where the report of the scan is written.
BASE_DIR = ROOT / "artifacts"
REPORT = BASE_DIR / "candidates.csv"

#: The domain the project scans and the result of the last scan.
_STATE: dict = {}


def scan(domain: str) -> dict:
    """Scan a domain: build the candidates and look every one of them up."""
    candidates = permutations(domain)
    with ThreadPoolExecutor(max_workers=16) as pool:
        addresses = list(pool.map(probe, candidates))
    rows = [
        {"domain": candidate, "resolved": bool(address), "address": address or ""}
        for candidate, address in zip(candidates, addresses)
    ]
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["domain", "resolved", "address"])
        for row in rows:
            writer.writerow([row["domain"], int(row["resolved"]), row["address"]])
    resolved = [row for row in rows if row["resolved"]]
    return {
        "domain": domain,
        "candidates": len(rows),
        "resolved": len(resolved),
        "unresolved": len(rows) - len(resolved),
        "sample": rows[0]["domain"] if rows else "",
        "report": str(REPORT),
        "rows": rows,
    }


def state() -> dict:
    """Run the scan of the project and keep its result."""
    if "run" not in _STATE:
        result = run(quick=False, base_dir=str(BASE_DIR))
        rows = []
        if REPORT.exists():
            with REPORT.open(encoding="utf-8") as handle:
                for row in csv.DictReader(handle):
                    rows.append({
                        "domain": row["domain"],
                        "resolved": row["resolved"] == "1",
                        "address": row["address"],
                    })
        result["rows"] = rows
        _STATE["run"] = result
    return _STATE


def families(domain: str) -> list:
    """How many candidates every family of the typos gives.

    The families are the ones the permutations are built from; a candidate
    can belong to more than one of them.
    """
    name, tld = split_domain(domain)
    dropped = {name[:i] + name[i + 1:] + "." + tld for i in range(len(name))}
    doubled = {name[:i] + name[i] * 2 + name[i + 1:] + "." + tld for i in range(len(name))}
    keyboard = {
        name[:i] + KEYBOARD[name[i]] + name[i + 1:] + "." + tld
        for i in range(len(name)) if name[i] in KEYBOARD
    }
    homoglyph = {
        name[:i] + HOMOGLYPHS[name[i]] + name[i + 1:] + "." + tld
        for i in range(len(name)) if name[i] in HOMOGLYPHS
    }
    swapped = {
        name[:i] + name[i + 1] + name[i] + name[i + 2:] + "." + tld
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
