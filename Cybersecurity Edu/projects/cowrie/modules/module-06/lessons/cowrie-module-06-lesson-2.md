# Read code review and safe change 6 in the source

**Lesson ID:** `cowrie-module-06-lesson-2`

## Purpose and learning objectives

Use main.py to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import socket` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import socketserver` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import threading` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import time` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class HoneypotHandler(socketserver.StreamRequestHandler):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def handle(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _log(self, events, kind, **fields):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def answer(self, line):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class HoneypotServer(socketserver.ThreadingTCPServer):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, *args, **kwargs):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `tests/test_pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `import socket` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `import threading` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `import time` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_answers_of_the_known_commands():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_files_of_the_fake_system_can_be_read():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_directories_can_be_listed():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_events_of_two_sessions_do_not_mix():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def talk(name):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
    parser = argparse.ArgumentParser(description='Run a small honeypot and analyse captured sessions.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Run a small honeypot and analyse captured sessions.')
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
"""A line-based honeypot server and a small session analysis."""
import json
import socket
import socketserver
import threading
import time
from pathlib import Path

BANNER = "SSH-2.0-OpenSSH_7.4 honeypot\r\n"
PROMPT = b"$ "

#: The commands the honeypot answers, with the files of the fake system.
FILES = {
    "/etc/passwd": [REDACTED],
    "/etc/hostname": "honeypot\n",
    "/proc/version": "Linux version 4.15.0\n",
}

DIRECTORIES = {
    "/": ["bin", "etc", "home", "root", "tmp", "var"],
    "/etc": ["passwd", "hostname", "shadow"],
    "/root": [".bash_history", ".ssh"],
}


class HoneypotHandler(socketserver.StreamRequestHandler):
    """One connection of the honeypot."""

    # The session is closed after this many seconds without a command.
    idle_timeout = 5.0
    # The session is closed after this many commands.
    max_commands = 25

    def handle(self):
        # The events of every session are collected by the server, so two
        # sessions never write into the same list.
        events = self.server.events
        username = ""
        try:
            self.request.settimeout(self.idle_timeout)
            self.wfile.write(BANNER.encode())
            self.wfile.write(b"login as: ")
            username = self.rfile.readline(128).decode(errors="replace").strip()
            self.wfile.write(b"password: ")
            password = [REDACTED]"replace").strip()
            self._log(events, "login", user=username, password=[REDACTED]
            self.wfile.write(b"Welcome to Ubuntu 16.04\r\n")

            for _ in range(self.max_commands):
                self.wfile.write(PROMPT)
                line = self.rfile.readline(256).decode(errors="replace").strip()
                if not line:
                    break
                self._log(events, "command", user=username, command=line)
                if line in ("exit", "logout"):
                    break
                self.wfile.write(self.answer(line).encode())
        except (socket.timeout, OSError):
            self._log(events, "timeout", user=username, command="")

    def _log(self, events, kind, **fields):
        events.append({"kind": kind, "source": self.client_address[0], **fields})

    def answer(self, line):
        """The answer of the honeypot to a command."""
        if line == "whoami":
            return "root\n"
        if line == "pwd":
            return "/root\n"
        if line == "uname -a":
            return "Linux honeypot 4.15.0 x86_64 GNU/Linux\n"
        if line == "ls":
            return " ".join(DIRECTORIES["/root"]) + "\n"
        if line.startswith("ls "):
            directory = line[3:].strip() or "/"
            entries = DIRECTORIES.get(directory)
            if entries is None:
                return f"ls: cannot access '{directory}': No such file or directory\n"
            return " ".join(entries) + "\n"
        if line.startswith("cat "):
            path = line[4:].strip()
            content = FILES.get(path)
            if content is None:
                return f"cat: {path}: No such file or directory\n"
            return content
        return f"{line.split()[0]}: command not found\n"


class HoneypotServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # The events of every session, with the lock that keeps the sessions
        # from writing into the list at the same time.
        self.events = []
        self.events_lock = threading.Lock()

    def record(self, event):
```

### tests/test_pipeline.py

```text
"""Tests for the honeypot."""
import json
import socket
import threading
import time
from pathlib import Path

from src.pipeline import (
    DIRECTORIES,
    FILES,
    HoneypotHandler,
    HoneypotServer,
    run,
    demo,
)


def test_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


# ---------------------------------------------------------------------------
# The answers
# ---------------------------------------------------------------------------

def test_the_answers_of_the_known_commands():
    handler = HoneypotHandler.__new__(HoneypotHandler)
    assert handler.answer("whoami") == "root\n"
    assert handler.answer("pwd") == "/root\n"
    assert "Linux" in handler.answer("uname -a")
    assert handler.answer("nope").endswith("command not found\n")


def test_the_files_of_the_fake_system_can_be_read():
    handler = HoneypotHandler.__new__(HoneypotHandler)
    assert handler.answer("cat /etc/passwd") == FILES["/etc/passwd"]
    assert "No such file" in handler.answer("cat /etc/nope")


def test_the_directories_can_be_listed():
    handler = HoneypotHandler.__new__(HoneypotHandler)
    assert "bin" in handler.answer("ls /")
    assert "passwd" in handler.answer("ls /etc")
    assert "No such file" in handler.answer("ls /nope")


# ---------------------------------------------------------------------------
# The server
# ---------------------------------------------------------------------------

def test_the_events_of_two_sessions_do_not_mix():
    """The events are collected by the server, not by the class, so two
    sessions never write into the same list."""
    server = HoneypotServer(("127.0.0.1", 0), HoneypotHandler)
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    def talk(name):
        with socket.create_connection(("127.0.0.1", port), timeout=3) as client:
            client.settimeout(3)
            client.recv(256)
            client.sendall((name + "\n").encode())
            client.recv(64)
            client.sendall(b"secret\n")
            client.recv(128)
            client.sendall(b"whoami\n")
            client.recv(256)
            client.sendall(b"exit\n")

    workers = [threading.Thread(target=talk, args=(f"user{index}",)) for index in range(4)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join(timeout=5)

    server.shutdown()
    server.server_close()
    thread.join(timeout=2)

    events = server.events_snapshot()
    logins = [event for event in events if event["kind"] == "login"]
    assert len(logins) == 4
    assert len({event["user"] for event in logins}) == 4


def test_the_log_holds_the_logins_and_the_commands(tmp_path):
    summary = run(quick=True, base_dir=str(tmp_path))

    lines = (tmp_path / "events.jsonl").read_text().splitlines()
    events = [json.loads(line) for line in lines if line]

    assert summary["sessions"] == len([e for e in events if e["kind"] == "login"])
    assert summary["commands"] == len([e for e in events if e["kind"] == "command"])
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

Use synthetic fixtures and isolated environments. Redact credentials and personal data. Review validation at input boundaries, dependency declarations, and error handling before suggesting a change. These security projects are dual-use: scan, intercept, phish, or operate honeypots only on systems you own or have explicit authorization to test. Keep intentionally vulnerable apps and security labs isolated, and use synthetic targets and credentials.

## Summary

This lesson ties its explanation to `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
