# A beginner's model of test code and implementation evidence

**Lesson ID:** `container-runtime-from-scratch-module-04-lesson-1`

## Purpose and learning objectives

Read the test cases in tests/test_pipeline.py beside the implementation in src/pipeline.py. Explain the behavior asserted by the tests and trace each assertion to the implementation. A test file describes a check; it does not prove that check passed.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `tests/test_pipeline.py`, `src/pipeline.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `tests/test_pipeline.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `import shutil` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_namespaces_are_the_ones_a_container_needs():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_container_with_a_network_has_no_new_network_namespace():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_namespace_mask_is_the_flags_together():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_plan_is_a_list_of_steps(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_plan_has_the_steps_a_container_needs(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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
"""Tests for the container runtime."""
import os
import shutil
from pathlib import Path

from src.pipeline import (
    CGROUP_ROOT,
    NAMESPACE_FLAGS,
    ContainerSpec,
    Step,
    execute,
    make_rootfs,
    namespace_flags,
    namespace_mask,
    plan_container,
    run,
    unshare_command,
    write_cgroup_limits,
    demo,
)


def test_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


def test_the_namespaces_are_the_ones_a_container_needs():
    spec = ContainerSpec(network=False)
    flags = namespace_flags(spec)
    assert "CLONE_NEWNS" in flags
    assert "CLONE_NEWPID" in flags
    assert "CLONE_NEWNET" in flags


def test_a_container_with_a_network_has_no_new_network_namespace():
    spec = ContainerSpec(network=True)
    assert "CLONE_NEWNET" not in namespace_flags(spec)


def test_the_namespace_mask_is_the_flags_together():
    spec = ContainerSpec(network=False)
    mask = namespace_mask(spec)
    for name in namespace_flags(spec):
        assert mask & NAMESPACE_FLAGS[name]


def test_the_plan_is_a_list_of_steps(tmp_path):
    spec = ContainerSpec()
    steps = plan_container(spec, tmp_path)
    assert steps
    for step in steps:
        assert isinstance(step, Step)
        assert step.kind
        assert step.detail


def test_the_plan_has_the_steps_a_container_needs(tmp_path):
    steps = plan_container(ContainerSpec(), tmp_path)
    kinds = [step.kind for step in steps]
    for wanted in ("validate", "namespaces", "rootfs", "mounts", "cgroup", "hostname", "exec"):
        assert wanted in kinds


def test_the_cgroup_step_carries_the_limits(tmp_path):
    spec = ContainerSpec(memory_mb=256, cpu_percent=30)
    steps = plan_container(spec, tmp_path)
    cgroup = next(step for step in steps if step.kind == "cgroup")
    assert cgroup.args["memory_max"] == "256M"
    assert cgroup.args["cpu_max"] == "30000 100000"


def test_the_rootfs_has_the_layout_of_an_image(tmp_path):
    spec = ContainerSpec()
    rootfs = make_rootfs(tmp_path, spec)
    for directory in ("bin", "etc", "proc", "sys", "tmp"):
        assert (rootfs / directory).is_dir()
    assert (rootfs / "bin" / "hello").exists()
    assert (rootfs / "etc" / "hostname").read_text().strip() == spec.hostname


def test_the_command_names_the_namespaces(tmp_path):
    spec = ContainerSpec()
    command = unshare_command(spec)
    assert command[0] == "unshare"
    assert "--pid" in command
    assert "--mount-proc" in command


def test_the_cgroup_limits_are_written_when_they_can_be(tmp_path):
    spec = ContainerSpec(name="test-container", memory_mb=64, cpu_percent=10)
    result = write_cgroup_limits(spec, root=str(tmp_path))

    if result["written"]:
        assert "memory.max" in result["written"]
```

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

This lesson ties its explanation to `tests/test_pipeline.py`, `src/pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
