# Read code review and safe change 6 in the source

**Lesson ID:** `lsb-steganography-module-06-lesson-2`

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
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from PIL import Image` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def make_cover(size=48, seed=42):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def to_bits(payload):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def embed(cover, message):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def extract(stego):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def psnr(original, stego):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def run(quick=False, base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `tests/test_pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import demo, embed, extract, make_cover, psnr, run, to_bits` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_payload_becomes_bits():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_message_is_hidden_in_the_cover_and_found_again():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_an_empty_message_is_found_again():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_cover_and_the_hidden_message_are_close():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_another_cover_gives_another_message():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
    parser = argparse.ArgumentParser(description='Encode and decode a message with least-significant-bit steganography.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Encode and decode a message with least-significant-bit steganography.')
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
"""Least-significant-bit steganography over a generated image."""
from pathlib import Path

import numpy as np
from PIL import Image

MESSAGE = "foundev lsb demo: meet at the library at four."


def make_cover(size=48, seed=42):
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:size, 0:size]
    red = (128 + 60 * np.sin(xx / 5.0)).astype(np.uint8)
    green = (110 + 50 * np.cos(yy / 6.0)).astype(np.uint8)
    blue = (90 + 40 * np.sin((xx + yy) / 8.0)).astype(np.uint8)
    noise = rng.integers(-4, 5, (size, size, 3))
    return np.clip(np.stack([red, green, blue], axis=2) + noise, 0, 255).astype(np.uint8)


def to_bits(payload):
    data = payload.encode("utf-8")
    header = len(data).to_bytes(4, "big")
    stream = []
    for byte in header + data:
        stream.extend((byte >> shift) & 1 for shift in range(7, -1, -1))
    return stream


def embed(cover, message):
    bits = to_bits(message)
    capacity = cover[:, :, 2].size
    if len(bits) > capacity:
        raise ValueError("message does not fit in the image")
    stego = cover.copy()
    flat = stego[:, :, 2].reshape(-1)
    for index, bit in enumerate(bits):
        flat[index] = (flat[index] & 0xFE) | bit
    return stego


def extract(stego):
    flat = stego[:, :, 2].reshape(-1)
    bits = [int(value) & 1 for value in flat]
    header = bits[:32]
    length = 0
    for bit in header:
        length = (length << 1) | bit
    if length <= 0 or length * 8 + 32 > len(bits):
        return ""
    payload_bits = bits[32:32 + length * 8]
    data = bytearray()
    for index in range(0, len(payload_bits), 8):
        value = 0
        for bit in payload_bits[index:index + 8]:
            value = (value << 1) | bit
        data.append(value)
    return data.decode("utf-8", errors="replace")


def psnr(original, stego):
    difference = original.astype(float) - stego.astype(float)
    mse = float(np.mean(difference ** 2))
    if mse == 0:
        return 99.0
    return round(10 * np.log10((255.0 ** 2) / mse), 2)


def run(quick=False, base_dir="artifacts"):
    base = Path(base_dir)
    base.mkdir(parents=True, exist_ok=True)
    cover = make_cover(40 if quick else 64)
    message = MESSAGE if not quick else "short demo message"
    stego = embed(cover, message)
    recovered = extract(stego)
    Image.fromarray(cover).save(base / "cover.png")
    Image.fromarray(stego).save(base / "stego.png")
    return {
        "capacity_bits": int(cover[:, :, 2].size),
        "message_bits": len(to_bits(message)),
        "psnr": psnr(cover, stego),
        "decoded_ok": recovered == message,
        "cover": str(base / "cover.png"),
        "stego": str(base / "stego.png"),
    }


def demo(base_dir="artifacts"):
    summary = run(quick=True, base_dir=base_dir)
    stego = np.asarray(Image.open(Path(base_dir) / "stego.png"))
    print(f"Encoded {summary['message_bits']} bits into {summary['capacity_bits']} channels.")
    print(f"Decoded correctly: {summary['decoded_ok']}, PSNR: {summary['psnr']} dB")
    print("Recovered:", extract(stego))

```

### tests/test_pipeline.py

```text
"""Tests for the steganography."""
import numpy as np

from src.pipeline import demo, embed, extract, make_cover, psnr, run, to_bits


def test_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


def test_the_payload_becomes_bits():
    bits = to_bits("A")
    assert len(bits) == 40, "the length of the message is in the first four bytes"
    assert all(bit in (0, 1) for bit in bits)


def test_the_message_is_hidden_in_the_cover_and_found_again():
    cover = make_cover(size=48, seed=2)
    stego = embed(cover, "hello")
    assert stego.shape == cover.shape
    assert extract(stego) == "hello"


def test_an_empty_message_is_found_again():
    cover = make_cover(size=48, seed=2)
    stego = embed(cover, "")
    assert extract(stego) == ""


def test_the_cover_and_the_hidden_message_are_close():
    cover = make_cover(size=48, seed=2)
    stego = embed(cover, "hello")
    assert psnr(cover, stego) > 25


def test_another_cover_gives_another_message():
    """A message that was not hidden in the picture is not found in it."""
    other = make_cover(size=48, seed=9)
    assert extract(other) != "hello"

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
