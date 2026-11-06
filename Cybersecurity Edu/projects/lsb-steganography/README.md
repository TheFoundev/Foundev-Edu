# Lsb Steganography

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

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

This is a third-year student project, not a production data platform. It uses local files and SQLite so the pipeline can run on one machine. The n

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Synthetic RGB cover image
- Length-prefixed bit encoding in the blue channel
- Decode with an exact message check
- PSNR comparison between cover and stego image
- Only the blue channel is used and the payload is tiny.
- There is no encryption, error correction or resistance to image re-compression.
- The demo cover image is generated, not a photograph.

The implementation inventory includes 19 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `requirements.txt`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `main.py`
- `requirements.txt`
- `src/__init__.py`
- `src/pipeline.py`
- `tests/test_pipeline.py`
- `web/api_impl.py`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: tests/test_pipeline.py. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
