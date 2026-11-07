# Mentor solution guide — Offline Speech Recognition Engine

## Review approach

A strong submission follows the actual repository path rather than recreating features based on the catalogue title. Check `architecture.md`, all module source-file citations, and the source README.

## Expected solution characteristics
- Correctly identifies the algorithm/model and whether it is trained, pretrained, rule-based, retrieval-based, or only a heuristic.
- Names required artifacts and reports absent assets honestly.
- Keeps preprocessing consistent between training and inference.
- Selects metrics and split strategy appropriate to class balance, chronology, geography, or group structure.
- Includes understandable failure behavior and domain-specific ethical safeguards.

## Project-specific review notes

- Audio is synthetic and limited to eight command words.
- DTW template matching does not scale to a real vocabulary.
- There is no language model; every frame sequence is independent.

Do not award correctness for fabricated benchmark scores or claims that this package's examples ran. Review source evidence, tests, and limitations before accepting the demo.
