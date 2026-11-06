# Read documented goals mapped to implementation in the source

**Lesson ID:** `dnstwist-module-05-lesson-2`

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
# dnstwist

Generate typosquatting candidates and check whether they resolve.

> A domain permutation engine that detects typosquatting and brand-impersonation phishing domains.

## Overview

An original, self-contained implementation of the **dnstwist** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- The permutations of a domain: a letter left out, a letter written twice,
  the keyboard next door, the homoglyphs, two letters swapped and the other
  top level domains
- The lookup of a host runs in a thread with the time it may take, so the
  timeout belongs to the call and not to the whole process
- The candidates are looked up at the same time, so a hundred of them do not
  take minutes
- The report of every candidate

## Stack

`Python`
The CSV stack is Python. The standard library resolver is used instead of a DNS library, so probes are simple A lookups and there is no WHOIS or certificate data.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
dnstwist/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
pytest -q
```

12 tests: the permutations (a letter left out, a letter written twice, the
keyboard, the homoglyphs, two letters swapped, the other top level domains),
that the timeout of the lookup does not leak into the process and the report.

## Notes and limitations

- DNS probes need network access; offline runs report every candidate as unresolved.
- There is no WHOIS, TLS certificate or screenshot enrichment.
- Homoglyphs are a short hard-coded map, not a full Unicode confusables list.

## License

Apache-2.0. See `LICENSE`.

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
    parser = argparse.ArgumentParser(description='Generate and probe typosquatting domains.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Generate and probe typosquatting domains.')
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
