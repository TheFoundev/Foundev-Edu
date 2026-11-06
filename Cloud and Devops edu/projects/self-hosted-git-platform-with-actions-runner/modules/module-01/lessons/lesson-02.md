# Trace the source implementation for git object types and hashing

**Lesson ID:** lesson-02  
**Module ID:** module-01  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Git Object Types and Hashing** in Self-Hosted Git Platform with Actions Runner. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Go, Git object hashing, custom workflow parser, os/exec. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

Git identifies objects by hashing a header containing object type and content length plus the content bytes.

## Move from the idea to the source

Now trace the implementation for Git Object Types and Hashing. The source evidence is: gitObjectHash/hashOf build object hash input; tests compare Git-compatible hashes.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. Open `repository.go` and locate `hashOf`.
2. Trace values from input to state changes and result.
3. Compare the actual code excerpt with the authored source finding: gitObjectHash/hashOf build object hash input; tests compare Git-compatible hashes.
4. Separate source behavior from external infrastructure.

## Source-code walkthrough

**Source file(s):** repository.go

**Source:** `repository.go:60–69`  
**Focus cue:** `hashOf`

````go
func hashOf(kind, content string) string {
	return gitObjectHash(kind, content)
}

func (repository *Repository) store(kind, content string) string {
	hash := hashOf(kind, content)
	repository.objects[hash] = Object{Hash: hash, Type: kind, Content: content}
	return hash
}
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: gitObjectHash/hashOf build object hash input; tests compare Git-compatible hashes. The original application was not modified or deployed by this content package.

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
