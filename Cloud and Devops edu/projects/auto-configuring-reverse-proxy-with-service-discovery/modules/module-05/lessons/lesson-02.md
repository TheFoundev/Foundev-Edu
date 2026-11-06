# Trace the source implementation for docker label discovery

**Lesson ID:** lesson-02  
**Module ID:** module-05  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Docker Label Discovery** in Auto-Configuring Reverse Proxy with Service Discovery. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Go, net/http, httputil, Docker Engine API. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

The Docker daemon is a host-level control API; discovery asks for containers and uses agreed labels.

## Move from the idea to the source

Now trace the implementation for Docker Label Discovery. The source evidence is: ListContainers calls /containers/json over a Unix socket; discovery reads foundev.service/port/host and filters non-running containers.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. Open `proxy.go` and locate `ListContainers`.
2. Trace values from input to state changes and result.
3. Compare the actual code excerpt with the authored source finding: ListContainers calls /containers/json over a Unix socket; discovery reads foundev.service/port/host and filters non-running containers.
4. Separate source behavior from external infrastructure.

## Source-code walkthrough

**Source file(s):** proxy.go

**Source:** `proxy.go:212–221`  
**Focus cue:** `ListContainers`

````go
// DiscoverFromDocker builds the registry from the containers of the daemon.
//
// Every container with the label "foundev.service" is a service, and the
// label "foundev.port" says which port of the container the traffic goes to.
func DiscoverFromDocker(client *DockerClient) (*Registry, error) {
	containers, err := client.ListContainers()
	if err != nil {
		return nil, err
	}
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: ListContainers calls /containers/json over a Unix socket; discovery reads foundev.service/port/host and filters non-running containers. The original application was not modified or deployed by this content package.

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
