# Read pipeline and api impl in the source

**Lesson ID:** `ssh-audit-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/pipeline.py] and [web/api_impl.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include encode_string, build_kexinit, make_server, serve, read_packet, read_string, parse_kexinit, audit, _number, _audit, _report, summary, handle; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/pipeline.py`, `web/api_impl.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import socket` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import struct` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import threading` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def encode_string(value: str) -> bytes:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def build_kexinit(kex, host_keys, ciphers, macs):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def make_server(good=True):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def serve(ready):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def read_packet(stream):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def read_string(payload, offset):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `web/api_impl.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import threading` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from src.pipeline import audit, make_server  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def _number(payload, key: str, default: int) -> int:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _audit(good: bool) -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _report(good: bool = False) -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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
"""SSH banner/KEXINIT audit against a local fake server."""
import json
import socket
import struct
import threading
from pathlib import Path

WEAK = {
    "diffie-hellman-group1-sha1", "diffie-hellman-group14-sha1", "ssh-dss",
    "3des-cbc", "arcfour", "arcfour128", "hmac-md5", "hmac-md5-96",
    "hmac-sha1-96", "blowfish-cbc", "cast128-cbc",
}


def encode_string(value: str) -> bytes:
    raw = value.encode()
    return struct.pack(">I", len(raw)) + raw


def build_kexinit(kex, host_keys, ciphers, macs):
    cookie = b"0123456789abcdef"
    payload = bytes([20]) + cookie
    for group in (kex, host_keys, ciphers, ciphers, macs, macs, ["none"], ["none"], [], []):
        payload += encode_string(",".join(group))
    payload += b"\x00" + struct.pack(">I", 0)  # first_kex_packet_follows + reserved
    padding_length = 8 - ((len(payload) + 5) % 8)
    if padding_length < 4:
        padding_length += 8
    packet = struct.pack(">I", len(payload) + padding_length + 1) + bytes([padding_length]) + payload
    packet += b"\x00" * padding_length
    return packet


def make_server(good=True):
    # A good server offers the modern key exchange only. The old
    # diffie-hellman-group14-sha1 is on the weak list, so it may not be in
    # the good one.
    weak_kex = ["curve25519-sha256", "sntrup761x25519-sha512@openssh.com"] if good else ["diffie-hellman-group1-sha1"]
    ciphers = ["aes128-gcm@openssh.com"] if good else ["3des-cbc", "aes128-cbc"]
    macs = ["hmac-sha2-256"] if good else ["hmac-md5"]

    def serve(ready):
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("127.0.0.1", 0))
        server.listen(1)
        ready.append(server.getsockname()[1])
        connection, _ = server.accept()
        with connection:
            connection.sendall(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5\r\n")
            connection.sendall(build_kexinit(weak_kex, ["rsa-sha2-512", "ssh-rsa"], ciphers, macs))
        server.close()

    return serve


def read_packet(stream):
    header = stream.read(4)
    if len(header) < 4:
        return b""
    length = struct.unpack(">I", header)[0]
    body = stream.read(length)
    padding_length = body[0]
    return body[1:len(body) - padding_length]


def read_string(payload, offset):
    size = struct.unpack(">I", payload[offset:offset + 4])[0]
    start = offset + 4
    return payload[start:start + size].decode(errors="replace"), start + size


def parse_kexinit(payload):
    offset = 17  # message type + 16-byte cookie
    names = ["kex", "host_keys", "enc_c2s", "enc_s2c", "mac_c2s", "mac_s2c"]
    result = {}
    for name in names:
        value, offset = read_string(payload, offset)
        result[name] = value.split(",")
    return result


def audit(port):
    with socket.create_connection(("127.0.0.1", port), timeout=3) as client:
        client.settimeout(3)
        stream = client.makefile("rb")
        banner = stream.readline(256).decode(errors="replace").strip()
        payload = read_packet(stream)
    algorithms = parse_kexinit(payload)
    findings = []
    for name, values in algorithms.items():
        for value in values:
            if value in WEAK:
                findings.append({"group": name, "algorithm": value})
    score = max(0, 100 - 20 * len(findings))
    grade = "A" if score >= 90 else "B" if score >= 70 else "C" if score >= 50 else "D"
    return banner, algorithms, findings, score, grade


def run(quick=False, base_dir="artifacts"):
```

### web/api_impl.py

```text
"""The API of the SSH audit.

The numbers are the real ones: a server of the project is started on the
loopback interface, the audit of the project connects to it, reads the banner
and the key exchange packet and looks at every algorithm it offers. The score
and the grade come out of that audit, so the console shows the report of a
real handshake and not of a table of constants.
"""

import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.pipeline import audit, make_server  # noqa: E402

#: The report of the last audit, so a page does not audit again for every call.
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


def _audit(good: bool) -> dict:
    """The audit of a server of the project.

    The server is started on a port of its own, the audit connects to it and
    the report is put together from what the handshake really said.
    """
    ready: list[int] = []
    thread = threading.Thread(target=make_server(good=good), args=(ready,), daemon=True)
    thread.start()
    for _ in range(100):
        if ready:
            break
        threading.Event().wait(0.05)
    try:
        banner, algorithms, findings, score, grade = audit(ready[0])
    finally:
        thread.join(timeout=2)
    return {
        "banner": banner,
        "server": banner.split("-")[-1] if "-" in banner else banner,
        "algorithms": algorithms,
        "findings": findings,
        "score": score,
        "grade": grade,
    }


def _report(good: bool = False) -> dict:
    key = "good" if good else "weak"
    if key not in _CACHE:
        _CACHE[key] = _audit(good)
    return _CACHE[key]


def summary():
    report = _report(good=False)
    good = _report(good=True)

    return {
        "stats": {
            "score": report["score"],
            "grade": report["grade"],
            "weak_findings": len(report["findings"]),
            "groups": len(report["algorithms"]),
        },
        "series": [
            {"label": "modern server", "value": good["score"]},
            {"label": "weak server", "value": report["score"]},
        ],
        "lists": {
            "findings": [
                {"group": finding["group"], "algorithm": finding["algorithm"]}
                for finding in report["findings"]
            ],
            "algorithms": [
                {"group": group, "algorithms": ", ".join(values)}
                for group, values in report["algorithms"].items()
            ],
        },
    }


def handle(method, path, payload, user):
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
