# Mentor solution guide — Neural Text-to-Speech Synthesis

## Review approach

A strong submission follows the actual repository path rather than recreating features based on the catalogue title. Check `architecture.md`, all module source-file citations, and the source README.

## Expected solution characteristics
- Correctly identifies the algorithm/model and whether it is trained, pretrained, rule-based, retrieval-based, or only a heuristic.
- Names required artifacts and reports absent assets honestly.
- Keeps preprocessing consistent between training and inference.
- Selects metrics and split strategy appropriate to class balance, chronology, geography, or group structure.
- Includes understandable failure behavior and domain-specific ethical safeguards.

## Project-specific review notes

- **This is not a neural TTS.** There is no acoustic model, no attention, no vocoder and no learned pronunciation; the project implements the classical pipeline that such a system would replace. A real Tacotron2 + WaveGlow build needs a GPU, a training corpus of hours and a dependency on TensorFlow, none of which fit in this environment.
- The pronunciation is rule based: the rules cover the common patterns of English and the lexicon covers the most frequent words, but an arbitrary proper noun will be pronounced wrongly. CMUdict would be the right source; it is not bundled.
- The duration model is fitted on 44 phrases whose target durations come from the usual rule of thumb (a word costs about 140 ms, a syllable about 85 ms). It is not fitted on a recorded corpus, so the MAE (about 0.1 s) measures how well the regression fits that formula, not how well it matches a speaker.
- The formant error measures that the waveform **contains** the formants that were asked for. It is a fidelity measure, not an intelligibility score: a MOS panel or an ASR round trip (synthesise → recognise → word error rate) would be the objective test this project still lacks.
- The speech is robotic: the formants do not move inside a vowel (no coarticulation), the pitch is a simple contour and there is no stress model beyond the first vowel of a word.

Do not award correctness for fabricated benchmark scores or claims that this package's examples ran. Review source evidence, tests, and limitations before accepting the demo.
