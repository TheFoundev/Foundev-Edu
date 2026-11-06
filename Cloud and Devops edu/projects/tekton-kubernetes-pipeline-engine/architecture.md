# Architecture

## Implemented system

Task/Pipeline structs, DAG resolver, parameter substitution, workspace/results, runner, retry/timeout/finally logic, directory loader.

## Data and control flow

Definitions → Resolve DAG → substitute params → host-run steps → workspace/results → statuses.

## Module source map

- **Task, Step, and Pipeline Models:** TaskStep, Task, PipelineTask, Pipeline, TaskStatus are plain Go types.
- **Resolve DAG Dependencies:** Resolve detects duplicate tasks, cycles, and unresolved runAfter references.
- **Substitute Task Parameters:** Substitute replaces $(params.name) and returns an error for absent parameters.
- **Execute Steps and Capture Results:** runStep invokes command executor and reads output/result files.
- **Share a Workspace and Read Results:** runTask creates/uses workspace; readResults collects declared result files.
- **Handle Retries and Timeouts:** Runner/runStep use retry counts, context deadlines, and durations.
- **Run Finally Tasks:** Runner schedules finally tasks after normal task completion/failure.
- **Load Definitions from Directories:** LoadDefinitionSet reads files and returns pipeline plus task map.
- **Compare the Local Runner with Tekton:** No Kubernetes client, CRDs, or cluster resources are in source; Runner.Execute delegates to the local command executor.
- **Test Execution and Security Limits:** Host command execution uses exec.CommandContext with the caller's OS permissions; tests use a recording executor for safe cases.

## Boundaries and risks

- No Kubernetes API server, Tekton CRDs, Pods, service accounts, or cluster execution are used.
- Commands run on the host; untrusted pipeline definitions can execute arbitrary commands.
- Definitions are Go structs/custom YAML reader rather than Tekton YAML CRDs.
- README's Notes says no retry/timeout/workspace despite earlier features/tests claiming they are implemented; inspect code, which does implement them in the local runner.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
