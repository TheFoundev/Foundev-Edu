# Architecture

## Implemented system

Validation, dry-run/local executors, static metric reader, pre/post checks, event timeline, rollback, memory/file stores.

## Data and control flow

Validate → baseline check → apply → wait/recover → verify → persist or abort.

## Module source map

- **Experiment and Action Models:** Experiment contains namespace/hypothesis/actions; Action has kind, target, duration, magnitude.
- **Validate Actions and Hypotheses:** Validate allows delay/kill/stress and nonempty targets; hypothesis operators are lt/gt/eq.
- **Executor Interface and Dry Run:** FaultExecutor requires Apply, Recover, Name; nil executor defaults to DryRunExecutor.
- **Local Fault Effects and Safety:** Local delay sleeps, stress starts busy goroutines, and kill sends SIGTERM to a parsed PID; Recover is empty.
- **Check Steady-State Hypotheses:** Runner reads MetricReader before actions and after recovery, records checks, and aborts when a check fails.
- **Runner Timeline and Rollback:** Run validates, checks baseline, applies actions, waits, recovers, records events, and rolls back actions still marked applied.
- **Store Experiment Results:** MemoryStore keeps results in process; FileStore serializes results to JSON.
- **Tests and Deterministic Time:** Tests use fakeClock/recordingExecutor and exercise rollback, failed hypothesis, dry run, and local wait.
- **Audit Local Executor Semantics:** Local delay waits once in Apply and again in Runner; stress magnitude is ignored; kill has no recovery action.
- **Plan Safe Fault Experiments:** Dry run is default; local executor is a host-side demo; scheduler and real infrastructure executor are absent.

## Boundaries and risks

- Local executor may SIGTERM a host process and consume CPU; only use a disposable target.
- Local delay sleeps in Apply and Runner, doubling configured delay.
- Recover is a no-op; killed processes are not restarted.
- Stress magnitude does not scale worker count; static metrics are not Prometheus.
- No Kubernetes/Chaos Mesh API or scheduler is present.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
