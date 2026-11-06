# Explain test deduplication and restore drills using a plain-language model

**Lesson ID:** lesson-01  
**Module ID:** module-08  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Test Deduplication and Restore Drills** in Encrypted Deduplicated Backup System. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Go, SHA-256, PBKDF2-style key derivation, AES-GCM, Filesystem. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

Tests verify chunk boundaries, repeated content deduplication, restoration, and key derivation properties.

## Move from the idea to the source

Begin with this mental model: Tests verify chunk boundaries, repeated content deduplication, restoration, and key derivation properties. Identify the actual components in repository_test.go.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. State the idea in your own words before reading code.
2. Open `repository_test.go` at the cited lines and identify the input and output.
3. Compare the analogy with the implementation: TestBackupDedupAndRestore; TestContentDefinedChunking; TestTheKeyIsDerivedWithASalt.
4. Write one question the analogy does not answer about real deployments.

## Source-code walkthrough

**Source file(s):** repository_test.go

**Source:** `repository_test.go:6–15`  
**Focus cue:** `TestContentDefinedChunking`

````go
"os"
	"path/filepath"
	"testing"
)

func TestContentDefinedChunking(t *testing.T) {
	data := bytes.Repeat([]byte("abcdefgh"), 64)
	chunks := ContentDefined(data, 32, 96, 192)
	if len(chunks) == 0 {
		t.Fatal("expected chunks")
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: TestBackupDedupAndRestore; TestContentDefinedChunking; TestTheKeyIsDerivedWithASalt. The original application was not modified or deployed by this content package.

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
