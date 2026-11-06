# A beginner's model of code review and safe change 6

**Lesson ID:** `rag-evaluation-harness-with-ragas-module-06-lesson-1`

## Purpose and learning objectives

Use main.py to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`, `web/api_impl.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import re` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def tokens(text):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def token_f1(prediction, reference):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def retrieve(question, vectorizer, matrix, contexts):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def extract_answer(question, context):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def run(quick=False, base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def demo(base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `tests/test_pipeline.py`, `from src.pipeline import demo, extract_answer, retrieve, run, token_f1, tokens` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import run as build` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_tokens_are_words():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_token_f1_of_two_texts_is_a_share():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_answer_comes_from_the_context():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_retrieval_finds_a_passage():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `web/api_impl.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import numpy as np  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from sklearn.feature_extraction.text import TfidfVectorizer  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def _number(payload, key: str, default: int) -> int:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _report() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def handle(method, path, payload, user):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### main.py

```text
"""Pipeline entry point. Run `python main.py run` or `python main.py demo`."""
import argparse
import json

from src.pipeline import run, demo


def main() -> None:
    parser = argparse.ArgumentParser(description='Evaluate a tiny retrieval-augmented QA pipeline.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Evaluate a tiny retrieval-augmented QA pipeline.')
        print("Run `python main.py run` to execute the pipeline.")
        return

    if args.command == "demo":
        demo(base_dir=args.base_dir)
        return

    summary = run(quick=args.quick, base_dir=args.base_dir)
    print(json.dumps(summary, indent=2, default=str))


if __name__ == "__main__":
    main()

```

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

### web/api_impl.py

```text
"""The API of the evaluation harness.

The retrieval and the answer extraction of the project really run: the
questions are answered with a TF-IDF retrieval over the contexts, the answer is
a sentence of the retrieved context, and the hit rate, the token F1 and the
faithfulness are the measures the project computes and writes to
artifacts/evaluation.json.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
from sklearn.feature_extraction.text import TfidfVectorizer  # noqa: E402

from src.pipeline import (  # noqa: E402
    CONTEXTS,
    QA,
    extract_answer,
    retrieve,
    run,
    token_f1,
)

#: The directory the pipeline writes to.
BASE = ROOT / "artifacts"


def _number(payload, key: str, default: int) -> int:
    """One number of the request; a query string arrives as a list."""
    value = (payload or {}).get(key, default)
    if isinstance(value, (list, tuple)):
        value = value[0] if value else default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _report() -> dict:
    """The evaluation report the pipeline wrote."""
    path = BASE / "evaluation.json"
    if not path.exists():
        return {"examples": []}
    return json.loads(path.read_text(encoding="utf-8"))


def summary():
    result = run(quick=False, base_dir=str(BASE))
    report = _report()
    rows = report.get("examples", [])

    return {
        "stats": {
            "questions": result["questions"],
            "hit_rate": result["retrieval_hit_rate"],
            "answer_f1": result["answer_f1"],
            "faithfulness": result["faithfulness"],
        },
        "series": [{"label": row["question"][:26], "value": row["f1"]} for row in rows],
        "lists": {
            "examples": [
                {"question": row["question"], "answer": row["answer"],
                 "f1": row["f1"], "faithfulness": row["faithfulness"],
                 "hit": row["retrieval_hit"]}
                for row in rows
            ],
            "corpus": [
                {"id": index + 1, "context": context[:70]}
                for index, context in enumerate(CONTEXTS)
            ],
        },
    }


def handle(method, path, payload, user):
    if method == "POST" and path == "/api/ask":
        question = str((payload or {}).get("question", "")).strip()
        if not question:
            return 400, {"error": "no question was sent"}
        vectorizer = TfidfVectorizer(stop_words="english")
        matrix = vectorizer.fit_transform(CONTEXTS)
        index, context = retrieve(question, vectorizer, matrix, CONTEXTS)
        answer = extract_answer(question, context)

        # The reference answer of the set, when the question is one of them.
        reference = next((item[1] for item in QA if item[0] == question), "")
        expected = next((item[2] for item in QA if item[0] == question), None)
        return 200, {
            "question": question,
            "answer": answer,
            "context": context,
            "retrieved_index": index,
            "retrieval_hit": None if expected is None else int(index == expected),
            "f1": round(token_f1(answer, reference), 4) if reference else None,
        }
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

This lesson ties its explanation to `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`, `web/api_impl.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
