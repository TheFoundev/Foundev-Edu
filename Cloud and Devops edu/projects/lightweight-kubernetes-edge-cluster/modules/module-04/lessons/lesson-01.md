# Explain join additional servers and agents using a plain-language model

**Lesson ID:** lesson-01  
**Module ID:** module-04  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Join Additional Servers and Agents** in Lightweight Kubernetes Edge Cluster. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses K3s, Kubernetes, Helm, systemd, Linux, Raspberry Pi/VM. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

Join tokens authorize nodes; control-plane peers and workers use different roles and commands.

## Move from the idea to the source

Begin with this mental model: Join tokens authorize nodes; control-plane peers and workers use different roles and commands. Identify the actual components in bootstrap/11-install-server-join.sh; bootstrap/20-install-agent.sh.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. State the idea in your own words before reading code.
2. Open `bootstrap/20-install-agent.sh` at the cited lines and identify the input and output.
3. Compare the analogy with the implementation: Server join and agent join consume a token file; agent gets node-class label.
4. Write one question the analogy does not answer about real deployments.

## Source-code walkthrough

**Source file(s):** bootstrap/11-install-server-join.sh; bootstrap/20-install-agent.sh

**Source:** `bootstrap/20-install-agent.sh:84–93`  
**Focus cue:** `agent`

````sh
done

log "planned labels: ${LABEL_ARGS[*]}"

if [ "${DRY_RUN}" -eq 1 ]; then
  log "dry-run: would join ${SERVER_URL} as agent with node-class=${NODE_CLASS}"
  exit 0
fi

CONFIG_FILE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/k3s/config-agent.yaml"
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: Server join and agent join consume a token file; agent gets node-class label. The original application was not modified or deployed by this content package.

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
