# Architecture — Neural Text-to-Speech Synthesis

## Component map

main.py → src/data.py (syllable_count, phrase_syllables, target_duration) → src/model.py (synthesize, _render_phrase) → web/api_impl.py (summary)

## Data and control flow

Use the project-specific lessons to trace input → preprocessing → algorithm/model → postprocessing → presentation. Verify each transition against the listed source files.

## Algorithm/model details

The source README and implementation files define the behavior taught here; the lesson cites the selected code path and marks unavailable features explicitly.

## Source inventory

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

## Implemented versus proposed

Implemented behavior is limited to the source entry points and code paths described above.

- **This is not a neural TTS.** There is no acoustic model, no attention, no vocoder and no learned pronunciation; the project implements the classical pipeline that such a system would replace. A real Tacotron2 + WaveGlow build needs a GPU, a training corpus of hours and a dependency on TensorFlow, none of which fit in this environment.
- The pronunciation is rule based: the rules cover the common patterns of English and the lexicon covers the most frequent words, but an arbitrary proper noun will be pronounced wrongly. CMUdict would be the right source; it is not bundled.
- The duration model is fitted on 44 phrases whose target durations come from the usual rule of thumb (a word costs about 140 ms, a syllable about 85 ms). It is not fitted on a recorded corpus, so the MAE (about 0.1 s) measures how well the regression fits that formula, not how well it matches a speaker.
- The formant error measures that the waveform **contains** the formants that were asked for. It is a fidelity measure, not an intelligibility score: a MOS panel or an ASR round trip (synthesise → recognise → word error rate) would be the objective test this project still lacks.
- The speech is robotic: the formants do not move inside a vowel (no coarticulation), the pitch is a simple contour and there is no stress model beyond the first vowel of a word.
