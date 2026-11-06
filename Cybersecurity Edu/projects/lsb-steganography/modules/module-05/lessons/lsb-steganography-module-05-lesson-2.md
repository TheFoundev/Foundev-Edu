# Read documented goals mapped to implementation in the source

**Lesson ID:** `lsb-steganography-module-05-lesson-2`

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
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from PIL import Image` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def make_cover(size=48, seed=42):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def to_bits(payload):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def embed(cover, message):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def extract(stego):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def psnr(original, stego):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def run(quick=False, base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
# LSB Steganography

Hide and recover a message in the least significant bits of an image.

> A Python tool that hides files inside images with least-significant-bit steganography for covert-channel study.

## Overview

An original, self-contained implementation of the **LSB Steganography** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Synthetic RGB cover image
- Length-prefixed bit encoding in the blue channel
- Decode with an exact message check
- PSNR comparison between cover and stego image

## Stack

`Python; NumPy; Pillow`
The CSV stack is Python + NumPy + Pillow. OpenCV is not installed, so this build uses Pillow and NumPy for the same least-significant-bit workflow.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
lsb-steganography/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
pytest -q
```

6 tests (`pytest -q`), up from 2.

## Notes and limitations

- Only the blue channel is used and the payload is tiny.
- There is no encryption, error correction or resistance to image re-compression.
- The demo cover image is generated, not a photograph.

## License

MIT. See `LICENSE`.

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
