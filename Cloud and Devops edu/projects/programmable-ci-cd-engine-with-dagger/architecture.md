# Architecture

## Implemented system

Pipeline/Step model, DAG ordering/cycle checks, digest cache, host/recording executors, retries/timeouts, environment/secret handling, report.

## Data and control flow

Pipeline definitions → dependency order → content/dependency digests → cache or executor → results/logs.

## Module source map

- **Model Pipeline Steps and Dependencies:** Step contains dependencies, environment, retries, timeout, and secrets; Pipeline contains Steps.
- **Resolve the Dependency Graph:** Order rejects unknown dependencies, duplicate names, and cycles.
- **Build Correct Cache Digests:** digestOf hashes step content together with dependency digests.
- **Use Memory and File Caches:** MemoryCache and FileCache implement Has/Put.
- **Compare Host and Recording Executors:** HostExecutor uses os/exec; RecordingExecutor records calls without running them.
- **Run Steps with Retries and Timeouts:** Engine.runStep uses context cancellation and retries, then captures exit code/output.
- **Handle Environment and Secrets:** Tests verify environment delivery and secret redaction.
- **Read Pipeline Files and Reports:** LoadPipeline/SavePipeline read and write definitions; PrintResults renders results.
- **Distinguish Dagger from This Engine:** HostExecutor.Run invokes the host command executor; the source does not create Dagger containers.

## Boundaries and risks

- Despite project name and listed stack, this implementation does not import or invoke the Dagger SDK/engine; it simulates container steps with host command execution.
- HostExecutor commands run on the machine and are not isolated containers.
- FileCache is local; no remote artifact/cache service exists.
- Secrets are redacted in output by tests but still require careful environment and process handling.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
