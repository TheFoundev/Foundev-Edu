# Assess failure and operational limits of resolve the dependency graph

**Lesson ID:** lesson-03  
**Module ID:** module-02  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Resolve the Dependency Graph** in Programmable CI/CD Engine with Dagger. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Go, context, host process execution, memory/file cache. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

Topological ordering means a prerequisite runs before the step that depends on it.

## Move from the idea to the source

Move from the happy path to operational reasoning. For this project, Order rejects unknown dependencies, duplicate names, and cycles.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. Identify a failure, boundary, or unexpected input.
2. Use `engine.go` and the `Order` path to predict behavior: Order rejects unknown dependencies, duplicate names, and cycles.
3. Describe a safe local/test verification and what evidence to collect.
4. State what additional code or infrastructure would be needed before making a production claim.

## Source-code walkthrough

**Source file(s):** engine.go

**Source:** `engine.go:312–321`  
**Focus cue:** `Order`

````go
//
// A step is skipped when the cache has its digest, and the digest of a step
// is built from the digests of the steps it needs, so a change upstream
// invalidates everything downstream.
func (engine *Engine) Run(ctx context.Context, pipeline Pipeline) ([]Result, error) {
	order, err := Order(pipeline)
	if err != nil {
		return nil, err
	}
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: Order rejects unknown dependencies, duplicate names, and cycles. The original application was not modified or deployed by this content package.

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
