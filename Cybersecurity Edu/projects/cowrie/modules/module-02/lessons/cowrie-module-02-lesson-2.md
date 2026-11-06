# Read pipeline and api impl in the source

**Lesson ID:** `cowrie-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/pipeline.py] and [web/api_impl.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include HoneypotHandler, handle, _log, answer, HoneypotServer, __init__, record, events_snapshot, state, sessions, commands_per_session, summary, handle; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/pipeline.py`, `web/api_impl.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

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
- In `web/api_impl.py`, `from __future__ import annotations` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from src.pipeline import run  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def state() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def sessions() -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def commands_per_session() -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def handle(method, path, payload, user):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### web/api_impl.py

```text
"""The API of the project: the log of the honeypot.

The numbers come from the real honeypot: the server is started, a few clients
log in and ask for things, and the events of every session are read back from
the log of the run.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import run  # noqa: E402

#: Where the honeypot writes the log of the run.
BASE_DIR = ROOT / "artifacts"
LOG = BASE_DIR / "events.jsonl"

#: The summary of the last run, kept for the life of the process.
_STATE: dict = {}


def state() -> dict:
    """Let the clients in and keep the events of the run."""
    if "run" not in _STATE:
        result = run(quick=False, base_dir=str(BASE_DIR))
        events = []
        if LOG.exists():
            for line in LOG.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    events.append(json.loads(line))
        _STATE["run"] = result
        _STATE["events"] = events
    return _STATE


def sessions() -> list:
    """The logins that were tried, with the password and the address."""
    return [
        {
            "user": event.get("user", ""),
            "password": [REDACTED]"password", ""),
            "from": event.get("source", ""),
        }
        for event in state()["events"] if event.get("kind") == "login"
    ]


def commands_per_session() -> list:
    """How many commands every session asked for."""
    counts: dict = {}
    for event in state()["events"]:
        if event.get("kind") == "command":
            user = event.get("user", "")
            counts[user] = counts.get(user, 0) + 1
    return [{"label": user, "value": count} for user, count in counts.items()]


def summary() -> dict:
    """The state of the last run: the sessions, the commands and the users."""
    current = state()
    result = current["run"]
    return {
        "stats": {
            "sessions": result["sessions"],
            "commands": result["commands"],
            "unique_users": result["unique_users"],
            "port": result["port"],
        },
        "series": commands_per_session(),
        "lists": {
            "events": [
                {
                    "kind": event.get("kind", ""),
                    "user": event.get("user", ""),
                    "command": event.get("command", ""),
                    "from": event.get("source", ""),
                }
                for event in current["events"]
            ],
            "sessions": sessions(),
        },
    }


def handle(method, path, payload, user):
    """The read and the write endpoints of the project."""
    if method == "GET" and path == "/api/events":
        return 200, {"events": summary()["lists"]["events"]}
    if method == "GET" and path == "/api/sessions":
        return 200, {"sessions": sessions()}
    if method == "POST" and path == "/api/run":
        _STATE.pop("run", None)
        _STATE.pop("events", None)
        state()
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

This lesson ties its explanation to `src/pipeline.py`, `web/api_impl.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
