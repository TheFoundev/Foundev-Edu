# Container Runtime From Scratch

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

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
├── src/p

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Container spec with root filesystem, network, memory and cpu limits
- An ordered plan of namespace, mount and cgroup operations, where every step
- The namespace mask of the container, the way the kernel takes it
- A generated rootfs with the layout of an image and a shell entry point
- The cgroup limits really written into cgroup v2 when the rights are there
- The command really started inside the namespaces when the rights are there
- A dry run, so the project always shows what it would do
- The namespaces need root or user namespaces. Without them the runtime
- The rootfs holds a script, not a real distribution: there is no dynamic
- There is no network setup: a container without a network namespace has no
- The cgroup limits are written when cgroup v2 is mounted and the directory

The implementation inventory includes 25 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `requirements.txt`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `README.md`
- `main.py`
- `requirements.txt`
- `runtime.py`
- `src/__init__.py`
- `src/pipeline.py`
- `tests/test_pipeline.py`
- `web/api_impl.py`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: tests/test_pipeline.py. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
