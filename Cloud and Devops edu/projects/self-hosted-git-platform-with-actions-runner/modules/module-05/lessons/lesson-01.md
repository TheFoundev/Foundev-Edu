# Explain parse workflow definitions using a plain-language model

**Lesson ID:** lesson-01  
**Module ID:** module-05  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Parse Workflow Definitions** in Self-Hosted Git Platform with Actions Runner. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Go, Git object hashing, custom workflow parser, os/exec. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

The parser recognizes a small indentation-based subset of workflow syntax, not arbitrary YAML.

## Move from the idea to the source

Begin with this mental model: The parser recognizes a small indentation-based subset of workflow syntax, not arbitrary YAML. Identify the actual components in repository.go.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. State the idea in your own words before reading code.
2. Open `repository.go` at the cited lines and identify the input and output.
3. Compare the analogy with the implementation: ParseWorkflow supports list/key job shapes, run/uses/needs/env fields.
4. Write one question the analogy does not answer about real deployments.

## Source-code walkthrough

**Source file(s):** repository.go

**Source:** `repository.go:301–310`  
**Focus cue:** `ParseWorkflow`

````go
// It is a small YAML subset, read from the indentation: the keys of the
// workflow are at the left, a job is at two spaces, the keys of a job at
// four, a step at six and the keys of a step at eight. Both shapes of the
// actions files are understood: a job as a list entry ("- name: build") and
// as a key ("build:").
func ParseWorkflow(text string) (Workflow, error) {
	workflow := Workflow{}
	jobIndex := -1
	stepIndex := -1
	inEnv := false
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: ParseWorkflow supports list/key job shapes, run/uses/needs/env fields. The original application was not modified or deployed by this content package.

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
