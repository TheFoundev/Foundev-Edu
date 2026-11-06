# A beginner's model of pipeline and api impl

**Lesson ID:** `container-runtime-from-scratch-module-02-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/pipeline.py] and [web/api_impl.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include ContainerSpec, Step, to_dict, namespace_flags, namespace_mask, plan_container, state, plan_steps, namespace_rows, summary, plan_container_of; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/pipeline.py`, `web/api_impl.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import shutil` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import subprocess` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from dataclasses import asdict, dataclass, field` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class ContainerSpec:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class Step:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def to_dict(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def namespace_flags(spec):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def namespace_mask(spec):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def plan_container(spec, base):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `web/api_impl.py`, `from __future__ import annotations` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def state(force: bool = False) -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def plan_steps(plan: dict) -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def namespace_rows(plan: dict) -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def plan_container_of(payload: dict) -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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
"""A small container runtime built from namespace and cgroup ideas.

The runtime has two halves that never touch each other:

  the planner  turns a `ContainerSpec` into a list of steps, each step a
               dataclass with the arguments it needs, so the plan can be
               checked and shown before anything runs
  the runner   walks the steps and does them: it creates the rootfs, writes
               the cgroup limits, runs the command inside the namespaces and
               mounts what is missing

The runner needs the rights to create the namespaces. When it does not have
them it says so and the plan is written down instead, so the project always
shows what it would do.
"""
import json
import os
import shutil
import subprocess
from dataclasses import asdict, dataclass, field
from pathlib import Path

#: The namespaces of a container, with the flag of each.
NAMESPACE_FLAGS = {
    "CLONE_NEWNS": 0x00020000,
    "CLONE_NEWUTS": 0x04000000,
    "CLONE_NEWIPC": 0x08000000,
    "CLONE_NEWUSER": 0x10000000,
    "CLONE_NEWPID": 0x20000000,
    "CLONE_NEWNET": 0x40000000,
}

#: The name of the cgroup the container is put in.
CGROUP_ROOT = "/sys/fs/cgroup"


@dataclass
class ContainerSpec:
    name: str = "demo"
    rootfs: str = "rootfs"
    hostname: str = "student-container"
    memory_mb: int = 128
    cpu_percent: int = 25
    command: list = field(default_factory=lambda: ["/bin/hello"])
    network: bool = False
    # Read only means the rootfs is mounted read only.
    read_only: bool = False
    # The user the command runs as inside the container.
    user: str = "root"


@dataclass
class Step:
    """One step of the plan.

    The step says what has to happen and with which arguments, so the plan
    is a program and not a text.
    """

    kind: str
    detail: str
    args: dict = field(default_factory=dict)

    def to_dict(self):
        return {"kind": self.kind, "detail": self.detail, "args": self.args}


def namespace_flags(spec):
    """The namespaces the container gets."""
    flags = ["CLONE_NEWPID", "CLONE_NEWUTS", "CLONE_NEWNS", "CLONE_NEWIPC"]
    if not spec.network:
        flags.append("CLONE_NEWNET")
    return flags


def namespace_mask(spec):
    """The mask of the namespace flags, the way the kernel takes them."""
    mask = 0
    for name in namespace_flags(spec):
        mask |= NAMESPACE_FLAGS[name]
    return mask


def plan_container(spec, base):
    """The steps that turn the spec into a running container."""
    rootfs = Path(base) / spec.rootfs
    steps = [
        Step("validate", f"check {rootfs} and the limits of the container", {
            "rootfs": str(rootfs),
            "memory_mb": spec.memory_mb,
            "cpu_percent": spec.cpu_percent,
        }),
        Step("namespaces", "clone with " + ", ".join(namespace_flags(spec)), {
            "flags": namespace_flags(spec),
            "mask": namespace_mask(spec),
        }),
        Step("rootfs", f"pivot_root into {rootfs}", {
            "rootfs": str(rootfs),
            "read_only": spec.read_only,
        }),
```

### web/api_impl.py

```text
"""The API of the project: the plan of a container and what the runner did.

The plan comes from the real planner of the project: a `ContainerSpec` is
turned into the steps of the plan, the namespace mask is built from the flags
of the kernel, the root filesystem is generated and the runner writes the
cgroup limits and starts the command when the machine gives it the rights.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime import ContainerSpec, namespace_flags, plan_container  # noqa: E402
from src.pipeline import (  # noqa: E402
    NAMESPACE_FLAGS,
    effective_uid,
    execute,
    make_rootfs,
    namespace_mask,
    run,
)

#: Where the plan and the root filesystem of the container are written.
BASE_DIR = ROOT / "artifacts"

#: The plan and the result of the last run.
_STATE: dict = {}


def state(force: bool = False) -> dict:
    """Plan the container of the project and keep the result of the run."""
    if force or "run" not in _STATE or "plan" not in _STATE:
        if (BASE_DIR / "plan.json").exists():
            try:
                result = _STATE.get("run") or run(quick=False, base_dir=str(BASE_DIR))
                plan = json.loads((BASE_DIR / "plan.json").read_text(encoding="utf-8"))
                _STATE["run"] = result
                _STATE["plan"] = plan
            except Exception:
                result = run(quick=False, base_dir=str(BASE_DIR))
                plan = json.loads((BASE_DIR / "plan.json").read_text(encoding="utf-8"))
                _STATE["run"] = result
                _STATE["plan"] = plan
        else:
            result = run(quick=False, base_dir=str(BASE_DIR))
            plan = json.loads((BASE_DIR / "plan.json").read_text(encoding="utf-8"))
            _STATE["run"] = result
            _STATE["plan"] = plan
    return _STATE


def plan_steps(plan: dict) -> list:
    """The steps of the plan, in the order the runner walks them."""
    result = []
    for step in plan["steps"]:
        detail = step["detail"]
        # Remove local project paths for cleaner display
        detail = detail.replace(str(ROOT), ".")
        detail = detail.replace(str(BASE_DIR), "artifacts")
        result.append({"step": step["kind"], "what": detail})
    return result


def namespace_rows(plan: dict) -> list:
    """The namespaces of the container and the bit each of them adds."""
    return [
        {"namespace": name, "flag": hex(NAMESPACE_FLAGS[name])}
        for name in plan["namespaces"]
    ]


def summary() -> dict:
    """The state of the last plan: the steps, the namespaces and the limits."""
    current = state(force=True)
    result = current["run"]
    plan = current["plan"]
    return {
        "stats": {
            "steps": result["steps"],
            "namespaces": result["namespaces"],
            "memory_mb": result["memory_mb"],
            "mode": "dry run" if result["dry_run"] else "executed",
        },
        "series": [
            {"label": name, "value": NAMESPACE_FLAGS[name]} for name in plan["namespaces"]
        ],
        "lists": {
            "plan": plan_steps(plan),
            "namespaces": namespace_rows(plan),
        },
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

Use synthetic fixtures and isolated environments. Redact credentials and personal data. Review validation at input boundaries, dependency declarations, and error handling before suggesting a change. These security projects are dual-use: scan, intercept, phish, or operate honeypots only on systems you own or have explicit authorization to test. Keep intentionally vulnerable apps and security labs isolated, and use synthetic targets and credentials.

## Summary

This lesson ties its explanation to `src/pipeline.py`, `web/api_impl.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
