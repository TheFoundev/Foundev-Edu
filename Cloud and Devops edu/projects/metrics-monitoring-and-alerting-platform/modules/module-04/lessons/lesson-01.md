# Explain calculate sum and average using a plain-language model

**Lesson ID:** lesson-01  
**Module ID:** module-04  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Calculate Sum and Average** in Metrics Monitoring and Alerting Platform. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Go, HTTP JSON, Prometheus text exposition. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

Sum totals values; average divides total by sample count, with empty-window behavior handled explicitly.

## Move from the idea to the source

Begin with this mental model: Sum totals values; average divides total by sample count, with empty-window behavior handled explicitly. Identify the actual components in metrics.go.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. State the idea in your own words before reading code.
2. Open `metrics.go` at the cited lines and identify the input and output.
3. Compare the analogy with the implementation: Store.Sum and Store.Average use windowLocked.
4. Write one question the analogy does not answer about real deployments.

## Source-code walkthrough

**Source file(s):** metrics.go

**Source:** `metrics.go:38–47`  
**Focus cue:** `windowLocked`

````go
store.samples = append(store.samples, sample)
	}
}

// windowLocked is the window of a metric, with the lock already held.
func (store *Store) windowLocked(metric string, window time.Duration, now time.Time) []Sample {
	matches := []Sample{}
	for _, sample := range store.samples {
		if sample.Metric != metric {
			continue
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: Store.Sum and Store.Average use windowLocked. The original application was not modified or deployed by this content package.

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
