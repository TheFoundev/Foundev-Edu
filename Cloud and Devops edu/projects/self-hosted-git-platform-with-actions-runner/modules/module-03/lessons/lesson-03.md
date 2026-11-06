# Assess failure and operational limits of read history, branches, and diff

**Lesson ID:** lesson-03  
**Module ID:** module-03  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Read History, Branches, and Diff** in Self-Hosted Git Platform with Actions Runner. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Go, Git object hashing, custom workflow parser, os/exec. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

Log follows commit ancestry; Diff compares file maps between two commits.

## Move from the idea to the source

Move from the happy path to operational reasoning. For this project, Log, Head, Branches, CreateBranch, Checkout, and Diff provide repository navigation.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. Identify a failure, boundary, or unexpected input.
2. Use `repository.go` and the `CreateBranch` path to predict behavior: Log, Head, Branches, CreateBranch, Checkout, and Diff provide repository navigation.
3. Describe a safe local/test verification and what evidence to collect.
4. State what additional code or infrastructure would be needed before making a production claim.

## Source-code walkthrough

**Source file(s):** repository.go

**Source:** `repository.go:148–157`  
**Focus cue:** `CreateBranch`

````go
return branches
}

// CreateBranch points a new branch at a commit. A branch that is already
// there is not changed.
func (repository *Repository) CreateBranch(name, from string) error {
	repository.mu.Lock()
	defer repository.mu.Unlock()
	if name == "" {
		return fmt.Errorf("a branch needs a name")
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: Log, Head, Branches, CreateBranch, Checkout, and Diff provide repository navigation. The original application was not modified or deployed by this content package.

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
