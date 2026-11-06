# Read documented goals mapped to implementation in the source

**Lesson ID:** `container-runtime-from-scratch-module-06-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors main.py, runtime.py, src/pipeline.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `main.py`, `runtime.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `runtime.py`, `from src.pipeline import ContainerSpec, namespace_flags, plan_container` brings a module or package name into this file; follow later references before claiming it is used on a running path.

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
# Container Runtime from Scratch

Plan and record Linux namespace and cgroup isolation steps.

> A workshop that rebuilds Docker from scratch to teach Linux namespaces and cgroups used by containers.

## Overview

An original, self-contained implementation of the **Container Runtime from Scratch** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Container spec with root filesystem, network, memory and cpu limits
- An ordered plan of namespace, mount and cgroup operations, where every step
  is a dataclass with the arguments it needs, so the plan is a program
- The namespace mask of the container, the way the kernel takes it
- A generated rootfs with the layout of an image and a shell entry point
- The cgroup limits really written into cgroup v2 when the rights are there
- The command really started inside the namespaces when the rights are there
- A dry run, so the project always shows what it would do

## Stack

`Python; Linux namespaces; cgroups`

The CSV stack is Python + Linux namespaces + cgroups. Both need rights, so
the runtime checks them: with the rights it writes the cgroup limits and
starts the command inside the namespaces, without them it writes the plan
down and says why nothing ran.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
container-runtime-from-scratch/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
├── runtime.py              container planner library
```

## Testing

```bash
pytest -q
```

13 tests: the namespaces and the mask, the plan and the steps it has to
have, the cgroup limits, the rootfs layout, the command, the cgroup writes
and the run.

## Notes and limitations

- The namespaces need root or user namespaces. Without them the runtime
  writes the plan down and says what it would have done.
- The rootfs holds a script, not a real distribution: there is no dynamic
  loader and no libc, so a real binary cannot be started inside it.
- There is no network setup: a container without a network namespace has no
  interface at all, and there is no veth or bridge.
- The cgroup limits are written when cgroup v2 is mounted and the directory
  can be written; otherwise the answer says which limit was refused.

## License

MIT. See `LICENSE`.

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
    parser = argparse.ArgumentParser(description='Plan a container runtime from first principles.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Plan a container runtime from first principles.')
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

### runtime.py

```text
"""Library entry point for the container planner."""
from src.pipeline import ContainerSpec, namespace_flags, plan_container

__all__ = ["ContainerSpec", "namespace_flags", "plan_container"]

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

This lesson ties its explanation to `README.md`, `main.py`, `runtime.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
