# A beginner's model of model and data

**Lesson ID:** `ai-recruitment-and-resume-screening-team-module-02-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/model.py] and [src/data.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include resume_features, draft_interview_questions, _matrix, train, make_resume, parse_resume, load_data; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/model.py`, `src/data.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/model.py`, `import re` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/model.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/model.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/model.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/model.py`, `from sklearn.feature_extraction.text import TfidfVectorizer` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def resume_features(resume):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def draft_interview_questions(resume, job_description=""):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _matrix(rows, vectorizer):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def train(data, quick=False, db_path="artifacts/candidates.db"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def rank_candidates(model, data):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def demo(data):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/data.py`, `import re` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/data.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def make_resume(index, seed=0, skills=None):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def parse_resume(text):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def load_data(seed=42, quick=False):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/model.py

```text
"""A logistic regression over the text of a resume, with the questions for the
interview drafted from what the resume says."""
import re
import sqlite3
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score

from src.data import SKILLS, parse_resume

#: The questions that are asked when the resume says nothing about a skill.
GENERIC_QUESTIONS = [
    "Tell me about a project you finished on your own. What was hard about it?",
    "How do you decide what to build first when everything feels urgent?",
    "Describe a time you had to hand something over to someone else. What went wrong?",
]

#: The question that goes with every skill, so the interviewer can go deeper.
SKILL_QUESTIONS = {
    "python": "Where did you use Python in production, and what did you have to learn the hard way?",
    "sql": "How do you tell the difference between a slow SQL query and a wrong one?",
    "rest": "How do you decide what belongs in a REST answer and what does not?",
    "testing": "What do you test, and what do you deliberately not test?",
    "docker": "What broke the first time you put this in Docker?",
    "flask": "How do you keep a Flask service from becoming a pile of routes?",
    "pandas": "What did the data look like before you cleaned it with pandas?",
    "git": "How do you and your team handle a Git branch that is two weeks old?",
    "linux": "What is the first thing you check on Linux when a service is slow?",
    "react": "How do you decide what a React screen should show before it loads?",
    "typescript": "What does TypeScript catch for you that a test would not?",
}


def resume_features(resume):
    """The features of a resume.

    The facts come from the text of the resume, so the parser is used and not
    the fields the generator filled in.
    """
    parsed = parse_resume(resume["text"])
    text = resume["text"].lower()
    found = [skill for skill in SKILLS if skill in text]

    return {
        "text": resume["text"],
        "years": parsed["years"],
        "projects": parsed["projects"],
        "education": parsed["education"],
        "skills": found,
    }


def draft_interview_questions(resume, job_description=""):
    """The questions for the interview, drafted from the resume.

    Every skill the resume mentions gets a question of its own, and the
    questions of the job are added when the resume says nothing about them.
    """
    parsed = parse_resume(resume["text"])
    questions = []

    for skill in parsed["skills"]:
        question = SKILL_QUESTIONS.get(skill)
        if question:
            questions.append(question)

    if parsed["projects"] == 0:
        questions.append("You have not listed a project. What have you built so far?")

    if parsed["years"] < 2:
        questions.append("How do you keep up with a codebase that is bigger than you are?")

    # Every word of the job the resume says nothing about gets a question.
    wanted = [
        word
        for word in re.findall(r"[a-zA-Z][a-zA-Z\-]{3,}", job_description.lower())
        if word not in parsed["skills"]
    ]
    for word in wanted:
        if len(questions) >= 5:
            break
        questions.append(f"The job needs {word}. What have you done with it?")

    for question in GENERIC_QUESTIONS:
        if len(questions) >= 5:
            break
        questions.append(question)

    return questions[:6]


def _matrix(rows, vectorizer):
    """The matrix of the features, the text and the numbers together."""
    text = vectorizer.transform([row["text"] for row in rows]).toarray()
    numbers = np.array(
        [[row["years"], row["projects"], len(row["skills"])] for row in rows],
        dtype=float,
```

### src/data.py

```text
"""Synthetic resumes with skills, experience and a hiring label."""
import re

import numpy as np

SKILLS = [
    "python", "sql", "pandas", "flask", "docker", "git", "javascript",
    "react", "testing", "linux", "rest", "typescript",
]

JOB_DESCRIPTION = (
    "We need a junior backend developer with Python, SQL, REST APIs and testing. "
    "Flask, Docker and Git experience are a plus."
)

NAMES = [f"Candidate {index:02d}" for index in range(64)]


def make_resume(index, seed=0, skills=None):
    """A resume, as the text a person would send.

    The hiring label comes from what the resume shows about the work and the
    studies, not from the skills: the skills are what the model has to learn
    from the text, so the label may not be a function of them.
    """
    rng = np.random.default_rng(seed + index)
    if skills is None:
        chosen = list(rng.choice(SKILLS, size=int(rng.integers(3, 8)), replace=False))
    else:
        chosen = list(skills)
    years = int(rng.integers(0, 8))
    education = str(rng.choice(["diploma", "bachelor", "master"]))
    projects = int(rng.integers(0, 5))
    summary = (
        f"{NAMES[index]} has {years} years of experience and a {education} degree. "
        f"Recent work used {', '.join(chosen[:3])}. "
        f"Completed {projects} portfolio projects and collaborated in small teams."
    )

    # The panel scores the work, the studies and the experience, and not the
    # skills: the label is what the model has to predict from the text.
    panel = 0.9 * projects + 1.4 * years + (1.0 if education == "master" else 0.0)
    label = int(panel + rng.normal(0, 1.2) >= 5.5)
    if rng.random() < 0.08:
        label = 1 - label  # a little label noise
    return {
        "name": NAMES[index],
        "text": summary,
        "skills": chosen,
        "years": years,
        "education": education,
        "projects": projects,
        "label": label,
    }


def parse_resume(text):
    """Read a resume and pull the facts out of it.

    The parser works on the text of the resume, the way a real one would: the
    years of experience, the degree, the number of the projects and the
    skills that are mentioned.
    """
    lowered = text.lower()

    years = 0
    match = re.search(r"has (\d+) years of experience", lowered)
    if match:
        years = int(match.group(1))

    education = ""
    match = re.search(r"a (diploma|bachelor|master) degree", lowered)
    if match:
        education = match.group(1)

    projects = 0
    match = re.search(r"completed (\d+) portfolio projects", lowered)
    if match:
        projects = int(match.group(1))

    mentioned = [skill for skill in SKILLS if skill in lowered]

    return {
        "years": years,
        "education": education,
        "projects": projects,
        "skills": mentioned,
    }


def load_data(seed=42, quick=False):
    count = 16 if quick else 24
    resumes = [make_resume(index, seed) for index in range(count)]
    split = int(count * 0.7)
    return {
        "train": resumes[:split],
        "test": resumes[split:],
        "job_description": JOB_DESCRIPTION,
        "skills": SKILLS,
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

This lesson ties its explanation to `src/model.py`, `src/data.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
