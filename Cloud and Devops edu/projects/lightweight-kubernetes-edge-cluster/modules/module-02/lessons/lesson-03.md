# Assess failure and operational limits of preflight host requirements

**Lesson ID:** lesson-03  
**Module ID:** module-02  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Preflight Host Requirements** in Lightweight Kubernetes Edge Cluster. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses K3s, Kubernetes, Helm, systemd, Linux, Raspberry Pi/VM. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

Preflight is a checklist before installation: architecture, memory, cgroups, ports, hostname, and swap constraints.

## Move from the idea to the source

Move from the happy path to operational reasoning. For this project, Preflight script checks host conditions before server/agent actions.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. Identify a failure, boundary, or unexpected input.
2. Use `bootstrap/00-preflight.sh` and the `agent` path to predict behavior: Preflight script checks host conditions before server/agent actions.
3. Describe a safe local/test verification and what evidence to collect.
4. State what additional code or infrastructure would be needed before making a production claim.

## Source-code walkthrough

**Source file(s):** bootstrap/00-preflight.sh

**Source:** `bootstrap/00-preflight.sh:18–27`  
**Focus cue:** `agent`

````sh
ROLE="agent"
for arg in "$@"; do
  case "${arg}" in
    --role=*) ROLE="${arg#*=}" ;;
    --role) shift; ROLE="${1:-agent}" ;;
    --help|-h)
      sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: Preflight script checks host conditions before server/agent actions. The original application was not modified or deployed by this content package.

## Practical exercise

Trace one input through the named source. Record the input, validation, state/data change, result, and one failure path. Then design a safe verification plan with the expected result and evidence.

## Common mistakes and debugging

- Treating a README feature list as proof of a real integration.
- Assuming an interface-shaped model is compatible with a provider protocol.
- Confusing passing unit tests with a production guarantee or independent security audit.
- Running destructive host, cluster, contract, or cloud operations against real resources.
- Logging secrets or relying on hard-coded sample credentials.

## Best practices and security

Use disposable environments, least privilege, explicit credential handling, and bounded inputs. For contracts, secrets, infrastructure, and host command runners, inspect the target before execution and separate test from production resources.

## Summary

You moved from a beginner explanation to the actual source behavior and its operational limits. You can cite the file and explain one verification path.

## Knowledge check

1. Which file/function implements the behavior?
2. What data or state changes?
3. What does the source not prove or provide?

## References

Use the official links in references.json.
