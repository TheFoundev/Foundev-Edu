# Read pipeline and api impl in the source

**Lesson ID:** `lsb-steganography-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/pipeline.py] and [web/api_impl.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include make_cover, to_bits, embed, extract, psnr, run, demo, _run, summary, handle; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/pipeline.py`, `web/api_impl.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from PIL import Image` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def make_cover(size=48, seed=42):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def to_bits(payload):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def embed(cover, message):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def extract(stego):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def psnr(original, stego):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def run(quick=False, base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `web/api_impl.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import numpy as np  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from PIL import Image  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from src.pipeline import MESSAGE, embed, extract, make_cover, psnr, to_bits  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def _run(base="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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

### web/api_impl.py

```text
"""The domain logic behind the API of the steganography demo.

The cover image is built, the message is embedded in the least significant
bit of the blue channel, and the image is read back: the numbers are the
real ones of the pipeline.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
from PIL import Image  # noqa: E402

from src.pipeline import MESSAGE, embed, extract, make_cover, psnr, to_bits  # noqa: E402

MESSAGE = MESSAGE  # the message of the project


def _run(base="artifacts"):
    base = Path(base)
    base.mkdir(parents=True, exist_ok=True)
    cover = make_cover(64)
    stego = embed(cover, MESSAGE)
    recovered = extract(stego)
    Image.fromarray(cover).save(base / "cover.png")
    Image.fromarray(stego).save(base / "stego.png")
    return cover, stego, recovered


def summary():
    cover, stego, recovered = _run()
    return {
        "stats": {
            "capacity_bits": int(cover[:, :, 2].size),
            "message_bits": len(to_bits(MESSAGE)),
            "psnr": round(psnr(cover, stego), 3),
            "decoded_ok": recovered == MESSAGE,
        },
        "series": [
            {"label": "blue channel", "value": int(cover[:, :, 2].size)},
            {"label": "bits of the message", "value": len(to_bits(MESSAGE))},
        ],
        "lists": {
            "channels": [
                {"channel": name, "mean": round(float(stego[:, :, index].mean()), 3),
                 "changed": int(np.count_nonzero(cover[:, :, index] != stego[:, :, index]))}
                for index, name in enumerate(("red", "green", "blue"))
            ]
        },
    }


def handle(method, path, payload, user):
    if method == "GET" and path.endswith("/message"):
        return 200, {"message": MESSAGE, "bits": len(to_bits(MESSAGE))}
    if method == "POST" and path.endswith("/encode"):
        message = str(payload.get("message") or MESSAGE)
        cover = make_cover(64)
        stego = embed(cover, message)
        recovered = extract(stego)
        return 200, {
            "message": message,
            "bits": len(to_bits(message)),
            "psnr": round(psnr(cover, stego), 3),
            "decoded_ok": recovered == message,
        }
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
