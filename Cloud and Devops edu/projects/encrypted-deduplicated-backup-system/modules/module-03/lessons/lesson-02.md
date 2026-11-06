# Trace the source implementation for content-defined chunk boundaries

**Lesson ID:** lesson-02  
**Module ID:** module-03  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Content-Defined Chunk Boundaries** in Encrypted Deduplicated Backup System. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Go, SHA-256, PBKDF2-style key derivation, AES-GCM, Filesystem. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

Content-defined chunking chooses boundaries from data content so edits can preserve later chunks better than fixed-size blocks.

## Move from the idea to the source

Now trace the implementation for Content-Defined Chunk Boundaries. The source evidence is: ContentDefined uses rolling hash with min/average/max boundaries.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. Open `repository.go` and locate `ContentDefined`.
2. Trace values from input to state changes and result.
3. Compare the actual code excerpt with the authored source finding: ContentDefined uses rolling hash with min/average/max boundaries.
4. Separate source behavior from external infrastructure.

## Source-code walkthrough

**Source file(s):** repository.go

**Source:** `repository.go:101–110`  
**Focus cue:** `ContentDefined`

````go
// The hash is a polynomial hash over the last bytes of the chunk, so the
// boundary of a chunk only depends on the bytes around it and not on the
// place of the chunk in the file. That is what makes the deduplication work:
// a byte that is inserted at the front only moves the boundaries near the
// front.
func ContentDefined(data []byte, min, average, max int) [][]byte {
	var chunks [][]byte
	const prime = uint64(1099511628211)

	// prime^(window-1), the weight of the byte that leaves the window.
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: ContentDefined uses rolling hash with min/average/max boundaries. The original application was not modified or deployed by this content package.

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
