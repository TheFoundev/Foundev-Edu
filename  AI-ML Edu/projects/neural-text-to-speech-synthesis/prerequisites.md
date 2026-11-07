# Prerequisites — Neural Text-to-Speech Synthesis

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

# Neural Text-to-Speech Synthesis

A formant-based text-to-speech engine that writes WAV files.

> Generate natural speech from text with attention-based Tacotron2 plus WaveGlow vocoders, fine-tuning on a small custom voice corpus and evaluating output quality.

## Overview

An original, self-contained implementation of the **Neural Text-to-Speech Synthesis** concept, built for the Foundev portfolio. The pipeline is explicit and every stage is testable on its own:

```text
text ──▶ G2P (src/g2p.py) ──▶ phonemes ──▶ duration model (src/duration.py)
                              │                     │
                              └──▶ prosody (src/prosody.py) ──▶ waveform
```

The engine is **not** a neural TTS: there is no acoustic model and no vocoder here, and the README says so. What it does have is a real pronunciation engine, a real prosody model and an **objective** quality measure instead of "it sounds okay to me".

## Features

- A rule-based grapheme-to-phoneme engine: digraphs (`ch`, `sh`, `th`, `ph`, `ng`, `ck`, ...), r-coloured vowels, the magic `e` (`phone` → /fow-n/), the silent `e` and a lexicon of the most frequent English words
- Formant synthesis: every vowel is rendered with its three formants (F1, F2, F3), every consonant with noise, a burst or a nasal murmur
- A duration model: a linear regression over the length of a word and its number of syllables, fitted on a corpus of 44 phrases, with the time shared between the syllables and the phonemes
- A prosody model: the pitch declines over a phrase, a question rises at the end, a stressed syllable gets an accent and is a little longer, and the voice carries a small jitter and shimmer
- WAV output and a waveform plot
- An **objective** evaluation: the formant peaks of the synthesized vowels are measured with an FFT and compared with the targets of the phonemes (the *formant error* in Hz)

## Stack

`Python; Matplotlib; NumPy; scikit-learn`
The stack is Python + Matplotlib + NumPy + scikit-learn. The duration model is a scikit-learn linear regression; the rest is NumPy. No neural framework is used (see the limitations).

## Run

```bash
pip install -r requirements.txt
python main.py train
python main.py demo
pytest -q
```

`python main.py demo` writes `artifacts/tts_demo.wav` and `artifacts/tts_waveform.png` and prints the duration MAE and the formant error.

## Structure

```text
neural-text-to-speech-synthesis/
├── main.py                 train / demo CLI
├── src/g2p.py              the letter-to-sound rules, the lexicon and the phoneme table
├── src/prosody.py          the pitch contou

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
