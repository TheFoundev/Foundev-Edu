# Explain tests and deterministic time using a plain-language model

**Lesson ID:** lesson-01  
**Module ID:** module-08  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Tests and Deterministic Time** in Chaos Engineering Experiment Platform. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Go, context, FaultExecutor, MetricReader. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

A fake clock lets tests advance time without waiting in real time.

## Move from the idea to the source

Begin with this mental model: A fake clock lets tests advance time without waiting in real time. Identify the actual components in chaos_test.go; chaos.go.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. State the idea in your own words before reading code.
2. Open `chaos_test.go` at the cited lines and identify the input and output.
3. Compare the analogy with the implementation: Tests use fakeClock/recordingExecutor and exercise rollback, failed hypothesis, dry run, and local wait.
4. Write one question the analogy does not answer about real deployments.

## Source-code walkthrough

**Source file(s):** chaos_test.go; chaos.go

**Source:** `chaos_test.go:143–152`  
**Focus cue:** `recordingExecutor`

````go
}
}

func TestDurationIsTheTotalNotTheLongest(t *testing.T) {
	clock := &fakeClock{now: time.Date(2026, 4, 23, 8, 0, 0, 0, time.UTC)}
	runner := Runner{Executor: &recordingExecutor{}, Now: clock.Now, Sleep: clock.Sleep}

	experiment := Experiment{Name: "x", Actions: []Action{
		{Kind: "delay", Target: "api", Duration: 2 * time.Second},
		{Kind: "delay", Target: "api", Duration: 3 * time.Second},
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: Tests use fakeClock/recordingExecutor and exercise rollback, failed hypothesis, dry run, and local wait. The original application was not modified or deployed by this content package.

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
