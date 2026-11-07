# Neural Text-to-Speech Synthesis

## Overview and purpose

A formant-based text-to-speech engine that writes WAV files.

## Real-world context and scope

Generate natural speech from text with attention-based Tacotron2 plus WaveGlow vocoders, fine-tuning on a small custom voice corpus and evaluating output quality. Actual implementation note: A rule-based grapheme-to-phoneme engine: digraphs (`ch`, `sh`, `th`, `ph`, `ng`, `ck`, ...), r-coloured vowels, the magic `e` (`phone` → /fow-n/), the silent `e` and a lexicon of the most frequent English words

The material describes the repository as supplied. **Implemented behavior** is based on the source README and entry points; **proposed or missing functionality** is listed separately below. Do not infer production readiness from a polished interface or project title.

### Verified implementation notes

- A rule-based grapheme-to-phoneme engine: digraphs (`ch`, `sh`, `th`, `ph`, `ng`, `ck`, ...), r-coloured vowels, the magic `e` (`phone` → /fow-n/), the silent `e` and a lexicon of the most frequent English words
- Formant synthesis: every vowel is rendered with its three formants (F1, F2, F3), every consonant with noise, a burst or a nasal murmur
- A duration model: a linear regression over the length of a word and its number of syllables, fitted on a corpus of 44 phrases, with the time shared between the syllables and the phonemes
- A prosody model: the pitch declines over a phrase, a question rises at the end, a stressed syllable gets an accent and is a little longer, and the voice carries a small jitter and shimmer
- WAV output and a waveform plot
- An **objective** evaluation: the formant peaks of the synthesized vowels are measured with an FFT and compared with the targets of the phonemes (the *formant error* in Hz)

### Proposed, absent, or uncertain behavior

- **This is not a neural TTS.** There is no acoustic model, no attention, no vocoder and no learned pronunciation; the project implements the classical pipeline that such a system would replace. A real Tacotron2 + WaveGlow build needs a GPU, a training corpus of hours and a dependency on TensorFlow, none of which fit in this environment.
- The pronunciation is rule based: the rules cover the common patterns of English and the lexicon covers the most frequent words, but an arbitrary proper noun will be pronounced wrongly. CMUdict would be the right source; it is not bundled.
- The duration model is fitted on 44 phrases whose target durations come from the usual rule of thumb (a word costs about 140 ms, a syllable about 85 ms). It is not fitted on a recorded corpus, so the MAE (about 0.1 s) measures how well the regression fits that formula, not how well it matches a speaker.
- The formant error measures that the waveform **contains** the formants that were asked for. It is a fidelity measure, not an intelligibility score: a MOS panel or an ASR round trip (synthesise → recognise → word error rate) would be the objective test this project still lacks.
- The speech is robotic: the formants do not move inside a vowel (no coarticulation), the pitch is a simple contour and there is no stress model beyond the first vowel of a word.

## Technology stack

- `Python`
- `Matplotlib`
- `NumPy`
- `scikit-learn`

## System requirements and setup

Use a supported Python environment appropriate to the source dependency pins. Some projects also require data files, trained weights, external APIs, cameras, GPU resources, a database, or an LLM runtime. These are identified in `setup-guide.md`; they are not assumed to be included. Follow the setup instructions in the source `README.md` and do not paste credentials into tracked files.

## Architecture and important components

main.py → src/data.py (syllable_count, phrase_syllables, target_duration) → src/model.py (synthesize, _render_phrase) → web/api_impl.py (summary)

## Directory structure

Source paths central to the learning material:

- `.github/workflows/ci.yml`
- `README.md`
- `main.py`
- `requirements.txt`
- `src/__init__.py`
- `src/data.py`
- `src/duration.py`
- `src/g2p.py`
- `src/model.py`
- `src/prosody.py`
- `tests/test_duration.py`
- `tests/test_g2p.py`
- `tests/test_pipeline.py`
- `tests/test_synthesis.py`
- `tests/test_wav.py`
- `web/api_impl.py`
- `web/assets/app.js`
- `web/console.html`
- `web/index.html`
- `web/server.py`

## Installation, environment, and database

See [`setup-guide.md`](setup-guide.md) for repository-specific commands, environment variables, optional services, and data/model requirements. Database setup is only applicable when the source workflow documents a database.

## Testing

Use only tests and checks present in the source repository. This learning package has not run the source application or trained a model. Expected test behavior and missing coverage are described in the source README and lessons.

## Security, privacy, and responsible use

Treat credentials, uploaded data, biometric data, student/financial records, and generated outputs as sensitive where relevant. Apply data minimization, consent and access controls, retention limits, secure secret handling, documented error handling, and human review. For consequential decisions, model outputs are educational signals only. Project-specific hazards appear in the final project guide and source review report.

## Troubleshooting

Start with missing assets and dependency versions, then validate input shape/schema, check configured API/database/model services, inspect logs, and compare observed behavior with the exact source path described in `architecture.md`. Many repositories contain a static UI or stub that is not wired to the model.

## Expected outcome

Complete the final project to explain and reproduce the repository's actual data-to-output path, demonstrate a tested source-aligned extension, and document its limitations.

## Further learning

See `references.json` for official framework references and the source repository README plus cited files for implementation details.
