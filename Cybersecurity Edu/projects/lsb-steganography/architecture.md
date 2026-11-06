# Architecture and source map

## Repository evidence

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

## Reading path

Start with the README, then identify entry points and trace calls into reusable modules. Inspect inputs and outputs at each boundary, then compare tests and configuration. Filenames suggest roles but do not prove execution order.

## Documentation versus implementation

README excerpt for comparison (truncated to 8,000 characters):

> # LSB Steganography
> 
> Hide and recover a message in the least significant bits of an image.
> 
> > A Python tool that hides files inside images with least-significant-bit steganography for covert-channel study.
> 
> ## Overview
> 
> An original, self-contained implementation of the **LSB Steganography** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.
> 
> ## Features
> 
> - Synthetic RGB cover image
> - Length-prefixed bit encoding in the blue channel
> - Decode with an exact message check
> - PSNR comparison between cover and stego image
> 
> ## Stack
> 
> `Python; NumPy; Pillow`
> The CSV stack is Python + NumPy + Pillow. OpenCV is not installed, so this build uses Pillow and NumPy for the same least-significant-bit workflow.
> 
> ## Run
> 
> ```bash
> pip install -r requirements.txt
> python main.py run
> python main.py demo
> pytest -q
> ```
> 
> ## Structure
> 
> ```text
> lsb-steganography/
> ├── main.py                 pipeline CLI
> ├── src/pipeline.py         data pipeline
> ├── tests/test_pipeline.py  smoke test
> ├── requirements.txt
> ```
> 
> ## Testing
> 
> ```bash
> pytest -q
> ```
> 
> 6 tests (`pytest -q`), up from 2.
> 
> ## Notes and limitations
> 
> - Only the blue channel is used and the payload is tiny.
> - There is no encryption, error correction or resistance to image re-compression.
> - The demo cover image is generated, not a photograph.
> 
> ## License
> 
> MIT. See `LICENSE`.
> 
> ## About the scope
> 
> This is a third-year student project, not a production data platform. It uses local files and SQLite so the pipeline can run on one machine. The notes above list the production pieces that were replaced or skipped.
> 

Treat these statements as claims. Confirm each against implementation. This package does not assert that every README feature exists, any test passes, or external integrations are live.
