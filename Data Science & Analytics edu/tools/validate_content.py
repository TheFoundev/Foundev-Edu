#!/usr/bin/env python3
"""Validate package structure only; does not establish educational accuracy or runtime behavior."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
errors = []

def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None

def check(project):
    slug = project.name
    manifest = load(project / "manifest.json")
    details = load(project / "project.json")
    required = ["README.md", "prerequisites.md", "setup-guide.md", "architecture.md",
                "glossary.md", "references.json", "final-project/requirements.md",
                "final-project/evaluation-rubric.json", "final-project/solution-guide.md"]
    for name in required:
        if not (project / name).is_file():
            errors.append(f"{slug}: missing {name}")
    if not manifest or not details:
        return
    if details.get("slug") != slug or manifest.get("project_slug") != slug:
        errors.append(f"{slug}: project/manifest slug mismatch")
    files = sorted(p.relative_to(project).as_posix() for p in project.rglob("*")
                   if p.is_file() and p.name != "manifest.json")
    if sorted(manifest.get("included_files", [])) != files:
        errors.append(f"{slug}: manifest file list mismatch")
    module_dirs = sorted((project / "modules").glob("module-*"))
    module_ids, lesson_ids, question_ids = set(), set(), set()
    lesson_count = question_count = 0
    for folder in module_dirs:
        module = load(folder / "module.json")
        assessment = load(folder / "assessment.json")
        key = load(folder / "answer-key.json")
        if not module or not assessment or not key:
            continue
        mid = module.get("module_id")
        if mid in module_ids:
            errors.append(f"{slug}: duplicate module ID {mid}")
        module_ids.add(mid)
        declared = module.get("ordered_lesson_ids", [])
        found = []
        for lesson in sorted((folder / "lessons").glob("*.md")):
            match = re.search(r"Lesson ID:\*\*\s*`([^`]+)`", lesson.read_text(encoding="utf-8"))
            if match:
                found.append(match.group(1))
        if found != declared:
            errors.append(f"{slug}/{folder.name}: lesson references mismatch")
        for lid in found:
            if lid in lesson_ids:
                errors.append(f"{slug}: duplicate lesson ID {lid}")
            lesson_ids.add(lid)
        lesson_count += len(found)
        questions = assessment.get("questions", [])
        answers = key.get("answers", [])
        question_count += len(questions)
        if len(questions) != 10:
            errors.append(f"{slug}/{folder.name}: expected exactly 10 questions")
        qids = set()
        for q in questions:
            qid = q.get("question_id")
            qids.add(qid)
            if qid in question_ids:
                errors.append(f"{slug}: duplicate question ID {qid}")
            question_ids.add(qid)
            options = q.get("options", [])
            option_ids = [o.get("option_id") for o in options]
            if len(options) != 4 or len(set(option_ids)) != 4:
                errors.append(f"{slug}: {qid} must have four distinct options")
            if q.get("related_lesson_id") not in found:
                errors.append(f"{slug}: invalid lesson reference on {qid}")
        if len(answers) != len(questions):
            errors.append(f"{slug}/{folder.name}: answer count mismatch")
        answer_ids = set()
        for answer in answers:
            qid = answer.get("question_id")
            answer_ids.add(qid)
            if qid not in qids:
                errors.append(f"{slug}: orphan answer {qid}")
                continue
            question = next(q for q in questions if q.get("question_id") == qid)
            options = {o.get("option_id") for o in question.get("options", [])}
            correct = answer.get("correct_option_id")
            if correct not in options:
                errors.append(f"{slug}: invalid correct option for {qid}")
            explanations = answer.get("incorrect_option_explanations", [])
            incorrect_options = options - {correct}
            if {x.get("option_id") for x in explanations} != incorrect_options or any(not x.get("explanation") for x in explanations):
                errors.append(f"{slug}: incomplete distractor explanations for {qid}")
            if not answer.get("correct_explanation") or not answer.get("tested_concept") or not answer.get("related_lesson_id"):
                errors.append(f"{slug}: incomplete answer explanation metadata for {qid}")
        if answer_ids != qids:
            errors.append(f"{slug}/{folder.name}: one answer per question required")
    expected = {"modules": len(module_dirs), "lessons": lesson_count, "questions": question_count}
    if manifest.get("counts") != expected:
        errors.append(f"{slug}: manifest counts mismatch")
    print(f"{slug}: {expected['modules']} modules, {lesson_count} lessons, {question_count} questions")

for package in sorted((ROOT / "projects").iterdir()):
    if package.is_dir():
        check(package)
if errors:
    print("ERRORS:\n" + "\n".join(errors))
    sys.exit(1)
print("PASS: structural checks only. No educational accuracy or runtime validity is implied.")
