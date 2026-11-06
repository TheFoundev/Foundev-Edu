# A beginner's model of test code and implementation evidence

**Lesson ID:** `dnstwist-module-03-lesson-1`

## Purpose and learning objectives

Read the test cases in tests/test_pipeline.py beside the implementation in src/pipeline.py. Explain the behavior asserted by the tests and trace each assertion to the implementation. A test file describes a check; it does not prove that check passed.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `tests/test_pipeline.py`, `src/pipeline.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `tests/test_pipeline.py`, `import socket` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_letter_is_left_out():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_letter_is_written_twice():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_keyboard_is_used():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_homoglyphs_are_used():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_two_letters_are_swapped():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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

### tests/test_pipeline.py

```text
"""Tests for the permutations and the probe."""
import socket

from src.pipeline import (
    HOMOGLYPHS,
    KEYBOARD,
    permutations,
    probe,
    run,
    demo,
)


def test_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


def test_a_letter_is_left_out():
    assert "gogle.com" in permutations("google.com")


def test_a_letter_is_written_twice():
    assert "gooogle.com" in permutations("google.com")


def test_the_keyboard_is_used():
    assert "gopgle.com" in permutations("google.com")


def test_the_homoglyphs_are_used():
    assert "g0ogle.com" in permutations("google.com")


def test_two_letters_are_swapped():
    assert "ogogle.com" in permutations("google.com")


def test_the_domain_itself_is_not_a_candidate():
    assert "google.com" not in permutations("google.com")


def test_the_other_top_level_domains_are_tried():
    assert "google.io" in permutations("google.com")


def test_the_candidates_are_unique():
    candidates = permutations("example.com")
    assert len(candidates) == len(set(candidates))


def test_the_probe_does_not_change_the_timeout_of_the_process():
    """The timeout is set for the call, not for the whole process."""
    before = socket.getdefaulttimeout()
    probe("this-host-does-not-exist.invalid")
    assert socket.getdefaulttimeout() == before


def test_the_probe_of_a_host_that_does_not_exist_is_none():
    assert probe("this-host-does-not-exist.invalid") is None


def test_the_report_holds_the_candidates(tmp_path):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert summary["candidates"] > 0

    lines = (tmp_path / "candidates.csv").read_text().splitlines()
    assert lines[0].startswith("domain,")
    assert len(lines) - 1 == summary["candidates"]

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

This lesson ties its explanation to `tests/test_pipeline.py`, `src/pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
