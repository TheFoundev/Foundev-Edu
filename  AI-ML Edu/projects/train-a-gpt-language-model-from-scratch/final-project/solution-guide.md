# Mentor solution guide — Train a GPT Language Model from Scratch

## Review approach

A strong submission follows the actual repository path rather than recreating features based on the catalogue title. Check `architecture.md`, all module source-file citations, and the source README.

## Expected solution characteristics
- Correctly identifies the algorithm/model and whether it is trained, pretrained, rule-based, retrieval-based, or only a heuristic.
- Names required artifacts and reports absent assets honestly.
- Keeps preprocessing consistent between training and inference.
- Selects metrics and split strategy appropriate to class balance, chronology, geography, or group structure.
- Includes understandable failure behavior and domain-specific ethical safeguards.

## Project-specific review notes

- The corpus is a few paragraphs, so the model memorises rather than generalises.
- There is no tokeniser training, positional encoding study or large-scale pretraining.
- Sampling is temperature-based and often produces odd words.

Do not award correctness for fabricated benchmark scores or claims that this package's examples ran. Review source evidence, tests, and limitations before accepting the demo.
