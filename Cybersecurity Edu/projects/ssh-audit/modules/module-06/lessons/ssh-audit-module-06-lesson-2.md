# Read code review and safe change 6 in the source

**Lesson ID:** `ssh-audit-module-06-lesson-2`

## Purpose and learning objectives

Use main.py to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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
- In `tests/test_pipeline.py`, `import socket` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `import threading` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def _start(serve):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_string_is_encoded_with_its_length():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_string_is_read_at_its_offset():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_kexinit_is_parsed():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_audit_of_a_good_server_finds_nothing():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
    parser = argparse.ArgumentParser(description='Audit SSH banner and key-exchange algorithms.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Audit SSH banner and key-exchange algorithms.')
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

### tests/test_pipeline.py

```text
"""Tests for the SSH audit."""
import socket
import threading

from src.pipeline import (
    audit,
    build_kexinit,
    demo,
    encode_string,
    make_server,
    parse_kexinit,
    read_string,
    run,
)


def _start(serve):
    """Start the fake server and give back the port it listens on."""
    ready = []
    thread = threading.Thread(target=serve, args=(ready,), daemon=True)
    thread.start()
    while not ready:
        pass
    return ready[0], thread


def test_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


def test_a_string_is_encoded_with_its_length():
    encoded = encode_string("abc")
    assert len(encoded) == 7
    assert encoded[:4] == b"\x00\x00\x00\x03"
    assert encoded[4:] == b"abc"


def test_a_string_is_read_at_its_offset():
    """The string is read and the offset behind it is given back."""
    payload = b"\x00\x00\x00\x03abc"
    value, offset = read_string(payload, 0)
    assert value == "abc"
    assert offset == 7


def test_the_kexinit_is_parsed():
    packet = build_kexinit(
        ["diffie-hellman-group14-sha256"], ["ssh-rsa"], ["aes128-ctr"], ["hmac-sha2-256"]
    )
    # The packet starts with its length and the padding length; the parser
    # works on the message behind them.
    parsed = parse_kexinit(packet[5:])

    assert parsed["kex"]
    assert "diffie-hellman-group14-sha256" in parsed["kex"]
    assert "aes128-ctr" in parsed["enc_c2s"]
    assert "hmac-sha2-256" in parsed["mac_c2s"]


def test_the_audit_of_a_good_server_finds_nothing():
    port, thread = _start(make_server(good=True))
    try:
        banner, _algorithms, findings, _score, grade = audit(port)
        assert banner.startswith("SSH-2.0")
        assert findings == []
        assert grade == "A"
    finally:
        thread.join(timeout=2)


def test_the_audit_of_a_weak_server_finds_the_weak_algorithms():
    port, thread = _start(make_server(good=False))
    try:
        _banner, _algorithms, findings, _score, grade = audit(port)
        assert findings
        assert grade in ("C", "D")
    finally:
        thread.join(timeout=2)

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
