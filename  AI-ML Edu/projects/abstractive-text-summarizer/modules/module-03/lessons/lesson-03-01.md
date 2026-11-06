# FactCC Multi-task Model: Understand consistency, entailment, and semantic role objectives

**Lesson ID:** `lesson-03-01`  
**Module:** FactCC Multi-task Model  
**Source focus:** `modeling/model.py` → `forward`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by FactCheck Studio: Factual Consistency and Summarization. By the end, you can describe consistency, entailment, and semantic role objectives, trace the factcc multi-task model implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about consistency, entailment, and semantic role objectives. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### The three jointly-trained tasks

FactCC is trained on *synthetically corrupted* claim/source pairs. A transformation is applied to a claim extracted from the source document; whether the transformation preserves factuality defines the label:

| Transformation | Effect on factuality | Label |
|---|---|---|
| `SampleSentences` | claims taken verbatim from the source | positive |
| `Backtranslation` | paraphrase via Google Translate (de → en) — usually preserves facts | positive |
| `PronounSwap`, `EntitySwap`, `NumberSwap`, `DateSwap` | replaces one entity in the claim with a different one found in the source | negative |
| `NegateSentences` | inserts a negation | negative |
| `AddNoise` | injects character-level noise | negative |

Connect this explanation to `modeling/model.py` and the source focus `forward`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The shipped Flask endpoint is deterministic lexical consistency scoring; it does not load a neural checkpoint. The research model code is a separate, older stack and no trained checkpoint is bundled. WORKFLOW statements that contradict the API/UI implementation need review.

## Step-by-step source investigation

1. Open `modeling/model.py` and inspect `forward`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `modeling/model.py` (not executed during package generation):

```python
def forward(self, input_ids, token_type_ids=None, attention_mask=None, labels=None,
                position_ids=None, head_mask=None, 
                ext_mask=None, ext_start_labels=None, ext_end_labels=None,
                aug_mask=None, aug_start_labels=None, aug_end_labels=None,
                loss_lambda=1.0):
        # run through bert
        bert_outputs = self.bert(input_ids, position_ids=position_ids, token_type_ids=token_type_ids,
                                 attention_mask=attention_mask, head_mask=head_mask)

        # label classifier
        pooled_output = bert_outputs[1]
        pooled_output = self.dropout(pooled_output)
        label_logits = self.label_classifier(pooled_output)

        # extraction classifier
        output = bert_outputs[0]
        ext_mask = ext_mask.unsqueeze(-1)
        ext_start_logits = self.ext_start_classifier(output) * ext_mask
        ext_end_logits = self.ext_end_classifier(output) * ext_mask
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For factcc multi-task model, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-03-01.md`](../exercises/exercise-03-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand consistency, entailment, and semantic role objectives, identify its source location, and state a limitation. The key project-specific fact is: Understand consistency, entailment, and semantic role objectives. In this repository, the claim must be grounded in the documented behavior and source paths: modeling/model.py; modeling/utils.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
