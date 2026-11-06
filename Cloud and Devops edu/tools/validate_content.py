#!/usr/bin/env python3
"""Validate portable Foundev content packages for structural consistency."""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "projects"
REPORTS = ROOT / "reports"
SOURCE_ROOT = Path("/home/aziz/foundev/verified-projects-main/06-cloud-devops")
REQUIRED_PROJECT_FILES = (
    "manifest.json", "project.json", "README.md", "prerequisites.md",
    "setup-guide.md", "architecture.md", "glossary.md", "references.json",
    "final-project/requirements.md", "final-project/evaluation-rubric.json",
    "final-project/solution-guide.md",
)
REQUIRED_MODULE_FILES = ("module.json", "assessment.json", "answer-key.json")
ALLOWED_TOP = {"manifest.json", "project.json", "README.md", "prerequisites.md", "setup-guide.md", "architecture.md", "glossary.md", "references.json", "modules", "final-project"}
SOURCE_REVIEW_ITEMS = {
    "resume-github-pages": ["Source has no in-page fragment links or section IDs; the observer adds .visible but style.css has no matching rule; profile-placeholder.png is referenced but absent."],
    "portfolio-netlify": ["The Home anchor targets #home while the hero ID is #hero; the contact form simulates success without sending data; the API redirect has no function implementation in the source."],
    "firebase-hosting-devlog": ["The supplied .firebaserc contains a placeholder and must be checked against the learner's actual Firebase project; review the catch-all rewrite for intended site routing."],
    "vercel-fun-facts": ["The setup instructions upload index.html without the linked JavaScript/CSS dependencies; verify the supplied legacy-style vercel.json against current Vercel documentation."],
    "aws-s3-photo-gallery": ["The S3 instructions upload only index.html although the site needs other assets; page copy mentions CloudFront but the guide does not configure it; public-read access needs a security review."],
    "hello-world-docker": ["The default CMD prints help rather than greeting; tests are not copied into the image, and the health check only verifies that a greeting command exits."],
    "nginx-static-site": ["The Dockerfile references an assets directory absent from the supplied file list and copies style.css to the wrong document-root location."],
    "interactive-quote-generator": ["The app reads quotes.txt while the image copies quotes.json; the advertised QuoteGenerator class and category CLI are absent, and tests import that absent class."],
    "docker-hub-mad-libs": ["The health check invokes --help rather than checking application behavior; tests are copied without installing pytest; interactive input does not validate the selected index."],
    "compose-todo-redis": ["Compose builds root app.py rather than src/app.py; the root app has no /health route or To-Do API, To-Do data in src/app.py is in memory, and the Compose wget health check may fail."],
    "github-actions-project-showcase": ["Setup instructions omit required CSS/JavaScript assets; the workflow uploads and deploys but has no build or test step; instructions describe branch publishing instead of artifact-based publishing."],
    "github-actions-pytest-pipeline": ["The workflow invokes pytest but does not explicitly install pytest; test_calculator.py is at repository root although its docstring mentions tests/."],
    "docker-hub-ci-todo-api": ["The workflow pushes a placeholder image name until edited and does not run tests; Dockerfile ignores requirements.txt and app data is in memory."],
    "link-in-bio-github-pages": ["Setup instructions omit required CSS/JavaScript assets; the Updated timestamp is the visitor's local clock, not deployment metadata; link clicks show alerts."],
    "markdown-to-web": ["Only README.md is converted; workflow generates index.html in its runner artifact, does not test output, and installs an unpinned Markdown dependency."],
    "s3-photo-gallery-serverless": ["The policy and ACL instructions enable broad public reads; source photos are placeholders, the page's CloudFront claim is not configured, and no upload code exists."],
    "aws-lambda-contact-form": ["The HTML endpoint placeholder does not match the placeholder name in instructions; browser JSON requests require deliberate CORS setup; SES region is hard-coded and fetch errors show a demo success message."],
    "netlify-fortune-api": ["No Netlify function source file exists; the configured /api/fortune rewrite is not the path the frontend fetches, and the response schema is unsupported by present source."],
    "formspree-contact-form": ["The Formspree endpoint must be configured; a rejected request displays a success-style demo message, and a declared phone pattern is unused."],
    "upstash-serverless-visitor-counter": ["The guide supplies Upstash REST credentials but code uses a Redis-protocol client; redis is undeclared, each poll increments the counter, reset also increments, and the UI expects an online field the API omits."],
    "color-tap-challenge": ["TinyDB is listed but unused; the .bky uses custom Blockly-like types and lacks Designer metadata, so native App Inventor import compatibility needs review."],
    "emoji-reaction-button": ["The guide presents two alternative click handlers; the .bky omits an explicit emoji_reactions declaration and uses an index offset that should be tested."],
    "magic-8-ball-fortune-teller": ["magic_8ball.bky is malformed XML; its documented debounce is absent from blocks and the acceleration expression is incomplete."],
    "simple-soundboard": ["Only event blocks are supplied; Designer component metadata and audio assets are absent, and the optional StopAllButton is not part of the base UI table."],
    "step-counter-pet": ["step_counter_pet.bky is malformed XML, includes a misspelled Accelerometer start call despite using Pedometer, and needs a consistent persisted-step baseline."],
    "quick-tip-calculator": ["Tip value is rounded to a whole unit before display; invalid input silently becomes zero and the text controller is not disposed."],
    "digital-dice-roller": ["The source rolls ten random values synchronously and displays the last; project.md contains an additional double-dice implementation not present in lib/main.dart."],
    "unit-converter": ["Invalid input silently becomes zero; volume/time are one-way conversions and category switching resets stored state but not the TextField's visible text."],
    "daily-quote-generator": ["The app selects a random quote rather than a date-specific daily quote; _showPunchline is unused and no quote state is persisted."],
    "basic-to-do-list": ["Tasks remain in an in-memory list and disappear on restart; TextEditingController is not disposed."],
    "rock-paper-scissors": ["Choice controls use GestureDetector rather than semantic button widgets, and no score reset is implemented."],
    "number-guessing-game": ["TextEditingController is not disposed and guess controls remain active after game completion."],
    "memory-card-match": ["On a matching pair, _firstCard and _secondCard are not cleared, preventing further card selection; delayed callbacks also lack mounted checks."],
    "whack-a-mole": ["Independent 1500ms hide callbacks overlap an 800ms spawn timer and can hide a newer mole; those delayed timers are not tracked for disposal."],
    "simple-drawing-canvas": ["An onPanStart localToGlobal result is unused; the app has no image export or drawing persistence."],
    "weather-checker": ["The API key is a client-source placeholder, city input is interpolated into the URL, request has no timeout, and controller/lifecycle cleanup is missing."],
    "joke-of-the-day": ["The app fetches random jokes rather than date-persisted daily content; fetchTenJokes is unused and HTTP requests lack timeout/lifecycle guards."],
    "cat-picture-generator": ["Fallback URLs rely on an external placeholder host, fallback clears its warning, delayed setState lacks a mounted check, and image-load failure does not trigger a new fallback."],
    "crypto-price-tracker": ["main.dart imports intl but pubspec.yaml does not declare it; mock data has five of eight requested coins and API failures silently show mock values."],
    "news-headline-reader": ["The NewsAPI key is embedded in client code; source has pageSize but no pagination, request failures silently show mock articles, and last-updated time records request start."],
    "audited-escrow-and-tokenization-contracts": ["No independent audit report is supplied; tests do not prove contract security; use only local/testnet funds and review the placeholder deployment key."],
    "auto-configuring-reverse-proxy-with-service-discovery": ["Health is manually marked, not actively probed; Docker socket access is privileged; parser is a small line format, not general YAML."],
    "chaos-engineering-experiment-platform": ["Local delay sleeps in both executor and runner; Recover is a no-op; stress magnitude is unused and actions can affect the host."],
    "cloud-cost-monitoring-dashboard-for-iac": ["Estimates use hard-coded prices/simplified fields; only immediate child modules are traversed; endpoint serves a precomputed summary rather than a dashboard."],
    "cron-dead-man-switch-monitoring": ["Schedule syntax is simplified; a separate poller must run; UUID ping URLs behave like credentials and need protection."],
    "decentralized-storage-dapp-on-ipfs": ["Storage is local, not an IPFS peer network; there is no pinning/replication, and CID behavior is limited to raw single-block data."],
    "distributed-rate-limiter-service": ["Memory backend is token bucket but Redis backend is fixed-window; store errors fail open; Redis metrics are incomplete."],
    "distributed-tracing-and-apm-platform": ["OTLPHandler parses custom JSON, is not mounted by main, and does not implement official OTLP JSON/Protobuf fields."],
    "encrypted-configuration-management-in-git": ["SOPS upstream status and binary provenance need current review; CI identities can decrypt authorized data; audit chain is tamper-evident, not proof against a full rewrite."],
    "encrypted-deduplicated-backup-system": ["Cryptography/chunking are custom code; there is no remote object storage, retention, or snapshot manager; restore must be verified before relying on data."],
    "event-streaming-platform-kafka-lite": ["Separate fake-registry smoke mode from real Kafka/registry integration; verify exactly-once configuration and dashboard origin in the full stack."],
    "kubernetes-control-plane-for-cloud-resources": ["This is a local model, not Kubernetes/Crossplane; unregistered kinds are accepted; optional FileStore exists despite README wording that suggests memory-only state."],
    "lightweight-event-messaging-and-queue-system": ["Messages and offsets are in memory; no replication, persistence, durable groups, flow control, or DLQ is implemented."],
    "lightweight-kubernetes-edge-cluster": ["Scripts use privileged host operations; no cluster was provisioned here; local-path is node-local and NetworkPolicy needs an enforcing CNI."],
    "message-broker-backend-for-microservices": ["Inventory and payment services are simulated; broker credentials, retry/dead-letter topology, and public ports need operational review."],
    "metrics-monitoring-and-alerting-platform": ["This is an in-memory metrics subset, not PromQL or Prometheus scraping; alerts are logged rather than delivered to Alertmanager."],
    "programmable-ci-cd-engine-with-dagger": ["Despite the name, source uses host execution and no Dagger engine; only run trusted pipeline definitions in a disposable environment."],
    "secrets-management-platform-with-ui": ["Default password is change-me and API token is printed at startup; JSON storage has mutable bounded audit history and the server has no TLS."],
    "secure-container-registry-with-vulnerability-scanning": ["Registry holds metadata only; scanner uses a small local vulnerability list; image blobs, signatures, and verification are not implemented."],
    "self-hosted-git-platform-with-actions-runner": ["Workflow runner executes commands on the host without container isolation or auth; README's recorded-step wording conflicts with HostRunner behavior."],
    "tekton-kubernetes-pipeline-engine": ["This is a local Go runner, not Tekton/Kubernetes; commands run on the host; README limitation text conflicts with implemented retry/timeout/workspace code."],
    "uptime-and-status-monitoring-service": ["Checks are HTTP GET only and dashboard polls; no TCP/DNS/TLS-expiry/content matching or multi-node guarantee is implemented."],
    "web3-dapp-frontend-with-wallet-integration": ["Use test wallets only; no contract deployment or receipt confirmation; custom Keccak/address helpers need validation before financial use."],
    "woodpecker-ci-pipeline-server": ["HostRunner executes commands locally without isolation; no auth/queue/retry/cancel; parser is a limited format rather than full Woodpecker YAML."],
    "audited-escrow-and-tokenization-contracts": ["The project has no independent security audit; tests are not a safety guarantee. Use test networks only, and review the placeholder deployment key."],
    "auto-configuring-reverse-proxy-with-service-discovery": ["Discovery is label-based and health is manually marked; Docker socket access is highly privileged; config parsing is not full YAML."],
    "chaos-engineering-experiment-platform": ["Local delay is applied in both executor and runner, kill recovery is a no-op, and stress magnitude is ignored; isolate any local experiment."],
    "cloud-cost-monitoring-dashboard-for-iac": ["Price tables are hard-coded examples, plan traversal is only one child level, and some cost inputs/defaults are simplified."],
    "cron-dead-man-switch-monitoring": ["Schedule syntax is simplified; the poller must run separately; UUID ping URLs behave as credentials and need protection."],
    "decentralized-storage-dapp-on-ipfs": ["Content store is local rather than connected to IPFS peers; no replication/pinning and no full UnixFS DAG support are implemented."],
    "distributed-rate-limiter-service": ["Memory backend is token bucket but Redis backend is fixed-window; store errors fail open; Redis counters are omitted from exported stats."],
    "distributed-tracing-and-apm-platform": ["The OTLP-labeled handler is custom JSON, is not mounted in main, and is not protocol-compatible with official OTLP payload semantics."],
    "encrypted-configuration-management-in-git": ["SOPS upstream/release status and binary provenance need human review; CI identities can decrypt authorized files; hash-chained audit is tamper-evident, not tamper-proof."],
    "encrypted-deduplicated-backup-system": ["KDF/chunking/encryption are custom code; no remote storage or retention is implemented; verify restored bytes before relying on backups."],
    "event-streaming-platform-kafka-lite": ["Separate fake registry from full Kafka/Schema Registry integration; confirm exactly-once settings and dashboard origin in the deployed stack."],
    "kubernetes-control-plane-for-cloud-resources": ["This is a local control-plane model, not a Kubernetes API server/Crossplane provider; unregistered kinds are accepted and optional FileStore contradicts README memory-only wording."],
    "lightweight-event-messaging-and-queue-system": ["Messages and offsets are in memory; there is no persistence, replication, durable consumer groups, flow control, or DLQ."],
    "lightweight-kubernetes-edge-cluster": ["Bootstrap scripts perform privileged host changes; no cluster was provisioned here; local-path is node-local and NetworkPolicy needs an enforcing CNI."],
    "message-broker-backend-for-microservices": ["Inventory/payment are simulations; review broker credentials, retry/dead-letter behavior, and exposed ports before deployment."],
    "metrics-monitoring-and-alerting-platform": ["This is an in-memory metrics subset, not PromQL or a Prometheus scraper; alerts are logged and not delivered to Alertmanager."],
    "programmable-ci-cd-engine-with-dagger": ["Despite the name, source runs host commands and does not invoke Dagger; only use trusted definitions in a disposable workspace."],
    "secrets-management-platform-with-ui": ["Default password is change-me and the API token is printed at startup; JSON storage/audit is local, mutable, and has no TLS."],
    "secure-container-registry-with-vulnerability-scanning": ["Registry is in-memory metadata; scanner has a small local vulnerability list; image blobs, signing, and verification are absent."],
    "self-hosted-git-platform-with-actions-runner": ["Workflow runner executes host commands without container isolation/auth; README's recorded-step wording conflicts with HostRunner execution; prebuilt binaries have unverified provenance."],
    "tekton-kubernetes-pipeline-engine": ["This is a local Go runner rather than Tekton/Kubernetes; host commands run directly; README's limitation text conflicts with retry/timeout/workspace code."],
    "uptime-and-status-monitoring-service": ["Only HTTP GET checks and polling dashboard are implemented; no TCP/DNS/TLS-expiry/content checks or multi-node guarantee."],
    "web3-dapp-frontend-with-wallet-integration": ["Use only test wallets; no contract deployment or receipt confirmation; custom Keccak/address helpers require independent vectors before financial use."],
}


class Audit:
    def __init__(self, project: Path):
        self.project = project
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.passed: list[str] = []
        self.review: list[str] = []

    def check(self, condition: bool, message: str) -> None:
        (self.passed if condition else self.errors).append(message)

    def load(self, relative: str):
        path = self.project / relative
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            self.errors.append(f"{relative}: cannot read valid JSON ({error})")
            return None


def validate(project: Path) -> Audit:
    audit = Audit(project)
    for name in REQUIRED_PROJECT_FILES:
        audit.check((project / name).is_file(), f"Required file exists: {name}")
    for name in sorted(p.name for p in project.iterdir()):
        audit.check(name in ALLOWED_TOP, f"No unexpected top-level entry: {name}")
    project_data = audit.load("project.json")
    if isinstance(project_data, dict):
        for key in ("title", "slug", "description", "problem_solved", "target_audience", "technology_stack", "difficulty_level", "prerequisites", "learning_outcomes", "estimated_completion_time", "content_schema_version"):
            audit.check(key in project_data, f"project.json contains {key}")
        audit.check(project_data.get("slug") == project.name, "Project slug matches directory")
    modules_dir = project / "modules"
    module_dirs = sorted(p for p in modules_dir.iterdir() if p.is_dir()) if modules_dir.is_dir() else []
    audit.check(bool(module_dirs), "At least one module exists")
    audit.check(6 <= len(module_dirs) <= 12, "Project contains six to twelve modules, scaled to project complexity")
    all_module_ids: set[str] = set()
    lesson_count = question_count = 0
    for module_dir in module_dirs:
        for name in REQUIRED_MODULE_FILES:
            audit.check((module_dir / name).is_file(), f"Required module file exists: {module_dir.name}/{name}")
        module = audit.load(f"modules/{module_dir.name}/module.json")
        assessment = audit.load(f"modules/{module_dir.name}/assessment.json")
        answers = audit.load(f"modules/{module_dir.name}/answer-key.json")
        if not isinstance(module, dict):
            continue
        module_id = module.get("module_id")
        audit.check(bool(module_id) and module_id not in all_module_ids, f"Unique module ID: {module_id}")
        if module_id:
            all_module_ids.add(module_id)
        source_files = module.get("source_files", [])
        focus = module.get("source_code_focus", {})
        audit.check(bool(source_files), f"{module_dir.name}: source files are mapped")
        for relative in source_files:
            audit.check((SOURCE_ROOT / project.name / relative).exists(), f"{module_dir.name}: mapped source exists: {relative}")
        audit.check(isinstance(focus, dict) and bool(focus.get("excerpt_file")) and bool(focus.get("symbol_or_search_term")), f"{module_dir.name}: source code focus is recorded")
        if isinstance(focus, dict) and focus.get("excerpt_file"):
            audit.check(any(focus["excerpt_file"] == item or focus["excerpt_file"].startswith(item.rstrip("/") + "/") for item in source_files), f"{module_dir.name}: excerpt is declared in source map")
            audit.check((SOURCE_ROOT / project.name / focus["excerpt_file"]).is_file(), f"{module_dir.name}: excerpt path is a source file")
        lesson_files = sorted((module_dir / "lessons").glob("*.md")) if (module_dir / "lessons").is_dir() else []
        lesson_ids = [re.sub(r"\.md$", "", f.name) for f in lesson_files]
        module_lesson_ids: set[str] = set()
        lesson_count += len(lesson_files)
        declared = module.get("lesson_ids", [])
        audit.check(set(declared) == set(lesson_ids), f"{module_dir.name}: declared lesson IDs match lesson files")
        for lesson_id, path in zip(lesson_ids, lesson_files):
            audit.check(lesson_id not in module_lesson_ids, f"{module_dir.name}: unique lesson ID {lesson_id}")
            module_lesson_ids.add(lesson_id)
            audit.check(path.stat().st_size > 100, f"Lesson has substantive content: {path.relative_to(project)}")
            body = path.read_text(encoding="utf-8", errors="replace")
            audit.check(body.find("## Topic in plain language") < body.find("## Source-code walkthrough"), f"{module_dir.name}/{lesson_id}: lay explanation precedes source walkthrough")
            if isinstance(focus, dict) and focus.get("excerpt_file"):
                citation = f"**Source:** `{focus['excerpt_file']}:{focus['line_start']}–{focus['line_end']}`"
                audit.check(citation in body, f"{module_dir.name}/{lesson_id}: excerpt citation matches module focus")
                excerpt_match = re.search(r"`{4}[A-Za-z0-9_+-]*\n(.*?)\n`{4}", body, re.S)
                normalize = lambda value: re.sub(r"[^a-z0-9]", "", str(value).lower())
                excerpt = excerpt_match.group(1) if excerpt_match else ""
                audit.check(normalize(focus.get("symbol_or_search_term", "")) in normalize(excerpt), f"{module_dir.name}/{lesson_id}: source focus cue appears in excerpt")
        if isinstance(assessment, dict):
            questions = assessment.get("questions", [])
            question_count += len(questions)
            audit.check(assessment.get("module_id") == module_id, f"{module_dir.name}: assessment module ID matches")
            audit.check(len(questions) == 10, f"{module_dir.name}: exactly 10 questions")
            levels = [question.get("difficulty_level") for question in questions]
            audit.check(levels.count("basic") == 3 and levels.count("intermediate") == 5 and levels.count("advanced") == 2, f"{module_dir.name}: difficulty mix is 3 basic, 5 intermediate, 2 advanced")
            question_ids: set[str] = set()
            question_texts: set[str] = set()
            valid_option_ids: dict[str, set[str]] = {}
            for question in questions:
                qid = question.get("question_id", "")
                audit.check(bool(qid) and qid not in question_ids, f"{module_dir.name}: unique question ID {qid}")
                question_ids.add(qid)
                question_text = question.get("question_text", "").strip()
                audit.check(bool(question_text) and question_text not in question_texts, f"{module_dir.name}/{qid}: non-duplicate question text")
                question_texts.add(question_text)
                options = question.get("options", [])
                option_ids = [option.get("option_id") for option in options]
                option_texts = [option.get("text", "").strip() for option in options]
                audit.check(len(options) == 4 and len(set(option_ids)) == 4 and len(set(option_texts)) == 4, f"{module_dir.name}/{qid}: exactly four distinct options")
                valid_option_ids[qid] = set(option_ids)
                audit.check(question.get("related_lesson_id") in declared, f"{module_dir.name}/{qid}: related lesson exists")
                audit.check(question.get("related_learning_objective") in module.get("learning_objectives", []), f"{module_dir.name}/{qid}: learning objective belongs to module")
            if isinstance(answers, dict):
                entries = answers.get("answers", answers.get("answer_key", []))
                if isinstance(entries, dict):
                    entries = [{"question_id": key, **value} for key, value in entries.items()]
                keyed: dict[str, list[dict]] = {}
                for entry in entries if isinstance(entries, list) else []:
                    keyed.setdefault(entry.get("question_id", ""), []).append(entry)
                audit.check(set(keyed) == question_ids and all(len(v) == 1 for v in keyed.values()), f"{module_dir.name}: exactly one answer entry per question")
                for qid, rows in keyed.items():
                    if len(rows) != 1:
                        continue
                    answer = rows[0]
                    correct_id = answer.get("correct_option_id")
                    audit.check(correct_id in valid_option_ids.get(qid, set()), f"{module_dir.name}/{qid}: correct option exists")
                    audit.check(len(answer.get("explanation", "").strip()) >= 20, f"{module_dir.name}/{qid}: correct explanation is complete")
                    wrong = answer.get("incorrect_option_explanations", {})
                    expected_wrong = valid_option_ids.get(qid, set()) - {correct_id}
                    audit.check(set(wrong) == expected_wrong and all(isinstance(v, str) and len(v.strip()) >= 10 for v in wrong.values()), f"{module_dir.name}/{qid}: all distractors explained")
                    audit.check(bool(answer.get("concept_tested")), f"{module_dir.name}/{qid}: concept documented")
                    audit.check(bool(answer.get("source_file")), f"{module_dir.name}/{qid}: source file documented")
                    audit.check(answer.get("related_lesson_id") in declared, f"{module_dir.name}/{qid}: answer lesson exists")
        exercises = list((module_dir / "exercises").glob("*.md")) if (module_dir / "exercises").is_dir() else []
        audit.check(bool(exercises), f"{module_dir.name}: at least one exercise exists")
    manifest = audit.load("manifest.json")
    if isinstance(manifest, dict):
        audit.check(manifest.get("project_slug") == project.name, "Manifest slug matches directory")
        audit.check(manifest.get("module_count") == len(module_dirs), "Manifest module count matches")
        audit.check(manifest.get("lesson_count") == lesson_count, "Manifest lesson count matches")
        audit.check(manifest.get("assessment_question_count") == question_count, "Manifest question count matches")
        included = set(manifest.get("included_files", []))
        actual = {str(p.relative_to(project)) for p in project.rglob("*") if p.is_file() and p.name != "manifest.json"}
        audit.check(included == actual, "Manifest included file list matches package")
    audit.warnings.append("Automated checks cannot establish educational accuracy or confirm provider interfaces, pricing, security policy, or code behavior.")
    audit.review.extend(SOURCE_REVIEW_ITEMS.get(project.name, []))
    audit.review.extend(["Review technical claims and code examples against current official documentation.", "Review public access, credential handling, cost exposure, accessibility, and deployment teardown instructions."])
    return audit


def main() -> int:
    REPORTS.mkdir(parents=True, exist_ok=True)
    projects = sorted(p for p in PROJECTS.iterdir() if p.is_dir()) if PROJECTS.exists() else []
    if not projects:
        print("No project packages found.")
        return 1
    overall = 0
    audit_rows = []
    for project in projects:
        audit = validate(project)
        status = "PASS" if not audit.errors else "FAIL"
        overall |= bool(audit.errors)
        manifest = audit.load("manifest.json") or {}
        source_notes = SOURCE_REVIEW_ITEMS.get(project.name, [])
        audit_rows.append((project.name, status, manifest.get("module_count", 0), manifest.get("lesson_count", 0), manifest.get("assessment_question_count", 0), source_notes))
        lines = [f"# Validation report: {project.name}", "", f"Generated: {datetime.now(timezone.utc).isoformat()}", f"Status: {status}", "", "## Passed checks"]
        lines += [f"- {item}" for item in audit.passed] or ["- None"]
        lines += ["", "## Errors"] + ([f"- {item}" for item in audit.errors] or ["- None"])
        lines += ["", "## Warnings"] + [f"- {item}" for item in audit.warnings]
        lines += ["", "## Human review"] + [f"- {item}" for item in audit.review]
        (REPORTS / f"{project.name}-validation.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"{project.name}: {status} ({len(audit.errors)} errors)")
    summary = ["# Source-to-Content Audit", "", f"Generated: {datetime.now(timezone.utc).isoformat()}", "", "## Scope", "", "Reviewed each package's module source references, source excerpts/findings, student-facing assessment items, answer keys, and the corresponding supplied project files/instructions. Structural checks confirm IDs, lesson links, unique question text, options, answers, manifest counts, and included files. They do not execute mobile apps, Docker images, cloud workflows, or API requests.", "", "## Package Results", "", "| Project | Structure | Modules | Lessons | Questions |", "|---|---:|---:|---:|---:|"]
    for slug, status, modules, lessons, questions, _ in audit_rows:
        summary.append(f"| {slug} | {status} | {modules} | {lessons} | {questions} |")
    summary.extend(["", "## Source Findings and Human Review", ""])
    for slug, _, _, _, _, notes in audit_rows:
        summary.append(f"### {slug}")
        summary.extend([f"- {note}" for note in notes] or ["- No source-specific finding was recorded."])
    summary.extend(["", "## Limits", "", "This validator does not run source builds, containers, cloud deployments, broker stacks, smart contracts, or external services. It checks mapped source files and excerpt cues but cannot certify technical accuracy, production behavior, or current provider/API behavior."])
    (REPORTS / "source-content-audit.md").write_text("\n".join(summary) + "\n", encoding="utf-8")
    module_audit = ["# Module-to-source audit", "", f"Modules audited: {sum(row[2] for row in audit_rows)}", "", "Every module is mapped to source files and a code focus. Validation checks source-file existence, excerpt citations, focus-cue presence, and plain-language-before-code progression. Human review remains necessary for semantic correctness.", ""]
    for project in projects:
        module_audit.extend([f"## {project.name}", ""])
        for module_file in sorted((project / "modules").glob("module-*/module.json")):
            data = json.loads(module_file.read_text(encoding="utf-8"))
            focus = data.get("source_code_focus", {})
            module_audit.append(f"- **{data.get('title')}** — `{focus.get('excerpt_file')}` → `{focus.get('symbol_or_search_term')}` (lines {focus.get('line_start')}–{focus.get('line_end')}); mapped: {', '.join('`'+x+'`' for x in data.get('source_files', []))}.")
        module_audit.append("")
    (REPORTS / "module-source-audit.md").write_text("\n".join(module_audit) + "\n", encoding="utf-8")
    return int(overall)


if __name__ == "__main__":
    sys.exit(main())
