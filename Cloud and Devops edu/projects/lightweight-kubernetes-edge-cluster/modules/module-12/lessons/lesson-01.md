# Explain uninstall and restore safely using a plain-language model

**Lesson ID:** lesson-01  
**Module ID:** module-12  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Uninstall and Restore Safely** in Lightweight Kubernetes Edge Cluster. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses K3s, Kubernetes, Helm, systemd, Linux, Raspberry Pi/VM. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

Teardown scripts can remove a cluster and data; backup restore is a separate recovery process.

## Move from the idea to the source

Begin with this mental model: Teardown scripts can remove a cluster and data; backup restore is a separate recovery process. Identify the actual components in bootstrap/99-uninstall.sh; README.md.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. State the idea in your own words before reading code.
2. Open `bootstrap/99-uninstall.sh` at the cited lines and identify the input and output.
3. Compare the analogy with the implementation: Uninstall is gated by --yes; runbook covers node replacement, token rotation, and snapshot restoration.
4. Write one question the analogy does not answer about real deployments.

## Source-code walkthrough

**Source file(s):** bootstrap/99-uninstall.sh; README.md

**Source:** `bootstrap/99-uninstall.sh:10–19`  
**Focus cue:** `snapshot`

````sh
#   sudo ./bootstrap/99-uninstall.sh --role server --yes
#   sudo ./bootstrap/99-uninstall.sh --role agent  --yes
#
# WARNING: uninstalling a SERVER node removes its etcd member. If this is the
# last server, or if too many servers are removed at once, the cluster loses
# quorum and data is unrecoverable. Take an etcd snapshot first
# (systemctl start k3s-backup.service) and confirm quorum afterwards.
#
set -euo pipefail
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: Uninstall is gated by --yes; runbook covers node replacement, token rotation, and snapshot restoration. The original application was not modified or deployed by this content package.

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
