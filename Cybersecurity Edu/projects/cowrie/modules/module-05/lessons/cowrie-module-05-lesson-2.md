# Read documented goals mapped to implementation in the source

**Lesson ID:** `cowrie-module-05-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors main.py, src/pipeline.py, web/api_impl.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `main.py`, `src/pipeline.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
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

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### README.md

```text
# Cowrie

A tiny SSH-style honeypot that records login attempts and commands.

> A medium-interaction SSH and Telnet honeypot that records attacker behaviour for defensive research.

## Overview

An original, self-contained implementation of the **Cowrie** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- A honeypot that answers a line-based shell: the files of a small fake
  system can be read and the directories listed
- The events of every session are collected by the server with a lock, so two
  sessions never write into the same list
- A session that says nothing is closed instead of being kept open
- The log of every session: the user, the password and every command

## Stack

`Python`
The CSV stack is Python. Twisted is not installed, so the server uses the standard library socket server and the project runs directly on the host.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
cowrie/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
```bash
pytest -q
```

8 tests: the answers of the honeypot, the files and the directories of the
fake system, that the events of two sessions do not mix, that the log holds
the logins, the passwords and the commands, and that a session ends when the
client stops talking.
```

## Notes and limitations

- The protocol is a fake line-based shell, not real SSH, so it cannot be logged into with an SSH client.
- Only localhost is used in the demo; there is no container sandbox.
- The log is plain JSONL with no rotation or alerting.

## License

BSD-3-Clause. See `LICENSE`.

## About the scope

This is a third-year student project, not a production data platform. It uses local files and SQLite so the pipeline can run on one machine. The notes above list the production pieces that were replaced or skipped.

```

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

This lesson ties its explanation to `README.md`, `main.py`, `src/pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
