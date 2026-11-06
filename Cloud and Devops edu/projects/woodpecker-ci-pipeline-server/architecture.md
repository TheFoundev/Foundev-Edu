# Architecture

## Implemented system

Pipeline/Step/Build types, indentation parser, trigger/run/status handlers, HostRunner, in-memory build registry.

## Data and control flow

HTTP trigger/config → parse pipeline → create build record → run steps → capture outputs/status → list/query build.

## Module source map

- **Pipeline and Build Models:** Step/Pipeline/Build types store command, repo/commit, status, and logs.
- **Parse the Pipeline Subset:** ParsePipeline reads lines and recognizes its supported step shape.
- **Trigger and Record a Build:** Server.Trigger stores Build; main exposes HTTP routes and CLI demo.
- **Execute Steps with HostRunner:** Runner interface can be replaced in tests; HostRunner uses os/exec.
- **Stop on Failure and Inspect Status:** Server.Run updates Build and stops subsequent steps after failure.
- **Serve the HTTP API and Console:** ListHandler and TriggerHandler expose API functionality; frontend/server files are separate.
- **Review Security and Product Scope:** HostRunner.Run invokes os/exec on the local machine; source has no OAuth/account model, queue, retries, cancellation, or container sandbox.

## Boundaries and risks

- No OAuth/user accounts, queue worker, retries, cancellation, or container isolation.
- HostRunner executes commands on the server machine; do not run untrusted pipelines.
- README says logs are recorded commands but HostRunner captures actual output; reconcile documentation with the selected runner.
- Pipeline syntax is a tiny custom subset, not full Woodpecker YAML.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
