# A beginner's model of test code and evidence boundaries

**Lesson ID:** `rag-evaluation-harness-with-ragas-module-03-lesson-1`

## Purpose and learning objectives

Read test implementations tests/test_pipeline.py. Identify the behavior each assertion encodes, connect it to implementation, and distinguish a test file from an executed passing result.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `tests/test_pipeline.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `tests/test_pipeline.py`, `from src.pipeline import demo, extract_answer, retrieve, run, token_f1, tokens` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import run as build` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_tokens_are_words():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_token_f1_of_two_texts_is_a_share():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_answer_comes_from_the_context():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_retrieval_finds_a_passage():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### tests/test_pipeline.py

```text
"""Tests for the evaluation harness."""
from src.pipeline import demo, extract_answer, retrieve, run, token_f1, tokens


def test_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


def test_the_tokens_are_words():
    assert tokens("Hello, world!") == ["hello", "world"]


def test_the_token_f1_of_two_texts_is_a_share():
    assert token_f1("the cat sat", "the cat sat") == 1.0
    assert token_f1("the cat sat", "a dog ran") == 0.0
    value = token_f1("the cat sat", "the cat ran")
    assert 0 < value <= 1


def test_the_answer_comes_from_the_context():
    answer = extract_answer("When is the lab open?", "The lab opens at 9:00 on weekdays.")
    assert answer
    assert "9:00" in answer or "lab" in answer.lower()


def test_the_retrieval_finds_a_passage():
    from src.pipeline import run as build

    summary = build(quick=True, base_dir="/tmp/rag-harness-test")
    assert summary["questions"] >= 0

```

The excerpt comes from this project’s source tree and may omit context. It is not evidence that the source was executed. Never treat a listed function name alone as proof that a user-facing path reaches it.

## Expected behavior and known limits

Only behavior visible in the cited implementation or assertions can be explained as implemented. External calls, deployment settings, successful installation, performance, and test outcomes remain unverified here.

## Practical exercise

Use the module exercise to create a call/data/configuration trace for these exact files. Include a source location for every claim.

## Common mistakes and debugging

- Reading only function names: follow bodies, callers, and return paths.
- Assuming imports prove an integration ran: inspect the call site and configuration.
- Assuming tests pass because they exist: record execution separately.
- If the path is unclear, search all references to the symbol and trace from the actual entry point.

## Best practices and security

Use synthetic fixtures and isolated environments. Redact credentials and personal data. Review validation at input boundaries, dependency declarations, and error handling before suggesting a change.

## Summary

This lesson ties its explanation to `tests/test_pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).


### src/pipeline.py

### src/pipeline.py

```text
"""Retrieval, answer extraction and evaluation metrics."""
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

CONTEXTS = [
    "Students reserve a study room through the library portal. Rooms can be booked for two hours at a time.",
    "The bike share programme has twelve stations near campus. A student card unlocks a bike for thirty minutes.",
    "The counselling office is open on weekdays from nine until five. Appointments can be booked online.",
    "Laptops can be borrowed for one day from the help desk. A student card and a signed form are required.",
    "The cafeteria serves breakfast from seven until ten. Lunch is available between eleven and two.",
    "The software lab provides Python and R on every machine. Users should bring their own storage device.",
    "A lost student card should be reported to security immediately. A replacement costs fifteen dollars.",
    "The writing centre reviews drafts by appointment. Sessions last twenty-five minutes and are free.",
    "The gym is open until ten on weekdays and until eight on weekends. Lockers require a small deposit.",
    "Printing credit can be topped up at the library desk. Each page costs five cents.",
]

QA = [
    ("How do students reserve a study room?", "Students reserve a study room through the library portal.", 0),
    ("How long can a bike be unlocked?", "A student card unlocks a bike for thirty minutes.", 1),
    ("When is the counselling office open?", "The counselling office is open on weekdays from nine until five.", 2),
    ("What is needed to borrow a laptop?", "A student card and a signed form are required.", 3),
    ("When is lunch served?", "Lunch is available between eleven and two.", 4),
    ("What software is installed in the lab?", "The software lab provides Python and R on every machine.", 5),
    ("What should I do if I lose my student card?", "A lost student card should be reported to security immediately.", 6),
    ("How long is a writing centre session?", "Sessions last twenty-five minutes and are free.", 7),
    ("When does the gym close on weekends?", "The gym is open until ten on weekdays and until eight on weekends.", 8),
    ("How much does printing cost per page?", "Each page costs five cents.", 9),
]


def tokens(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def token_f1(prediction, reference):
    predicted = tokens(prediction)
    expected = tokens(reference)
    if not predicted or not expected:
        return 0.0
    overlap = 0
    remaining = list(expected)
    for word in predicted:
        if word in remaining:
            remaining.remove(word)
            overlap += 1
    if overlap == 0:
        return 0.0
    precision = overlap / len(predicted)
    recall = overlap / len(expected)
    return 2 * precision * recall / (precision + recall)


def retrieve(question, vectorizer, matrix, contexts):
    scores = (vectorizer.transform([question]) @ matrix.T).toarray()[0]
    index = int(np.argmax(scores))
    return index, contexts[index]


def extract_answer(question, context):
    question_words = set(tokens(question))
    sentences = [part.strip() for part in context.split(".") if part.strip()]
    best = max(sentences, key=lambda sentence: len(question_words & set(tokens(sentence))))
    return best + "."


def run(quick=False, base_dir="artifacts"):
    base = Path(base_dir)
    base.mkdir(parents=True, exist_ok=True)
    examples = QA[:6] if quick else QA
    contexts = CONTEXTS[:6] if quick else CONTEXTS

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(contexts)

    results = []
    for question, reference, expected_index in examples:
        index, context = retrieve(question, vectorizer, matrix, contexts)
        prediction = extract_answer(question, context)
        predicted_tokens = set(tokens(prediction))
        context_tokens = set(tokens(context))
        re
```

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
