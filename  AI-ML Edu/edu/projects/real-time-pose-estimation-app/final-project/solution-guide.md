# Mentor solution guide — Real-Time Pose Estimation App

## Review approach

A strong submission follows the actual repository path rather than recreating features based on the catalogue title. Check `architecture.md`, all module source-file citations, and the source README.

## Expected solution characteristics
- Correctly identifies the algorithm/model and whether it is trained, pretrained, rule-based, retrieval-based, or only a heuristic.
- Names required artifacts and reports absent assets honestly.
- Keeps preprocessing consistent between training and inference.
- Selects metrics and split strategy appropriate to class balance, chronology, geography, or group structure.
- Includes understandable failure behavior and domain-specific ethical safeguards.

## Project-specific review notes

- MediaPipe is not used, so the regressor is a ridge regression over the brightness of a small grid of the person, not a neural network. The detector also assumes bright figures on a dark background.
- The camera needs OpenCV and a camera; without them the simulator and the upload are the inputs.
- The person is found by the bright pixels, so a person on a bright background is not found.

Do not award correctness for fabricated benchmark scores or claims that this package's examples ran. Review source evidence, tests, and limitations before accepting the demo.
