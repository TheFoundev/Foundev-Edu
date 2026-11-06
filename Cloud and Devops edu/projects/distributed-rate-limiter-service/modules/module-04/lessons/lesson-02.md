# Trace the source implementation for choose a request identity key

**Lesson ID:** lesson-02  
**Module ID:** module-04  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Choose a Request Identity Key** in Distributed Rate Limiter Service. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Go, HTTP middleware, Redis RESP subset, Prometheus text. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

A limiter needs a key to decide which requests share a bucket; trusting proxy headers changes who can choose that key.

## Move from the idea to the source

Now trace the implementation for Choose a Request Identity Key. The source evidence is: KeyFor prefers X-API-Key, then RemoteAddr; first X-Forwarded-For is used only when TrustedProxies is true.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. Open `limiter.go` and locate `RemoteAddr`.
2. Trace values from input to state changes and result.
3. Compare the actual code excerpt with the authored source finding: KeyFor prefers X-API-Key, then RemoteAddr; first X-Forwarded-For is used only when TrustedProxies is true.
4. Separate source behavior from external infrastructure.

## Source-code walkthrough

**Source file(s):** limiter.go

**Source:** `limiter.go:96–105`  
**Focus cue:** `RemoteAddr`

````go
func (limiter *Limiter) KeyFor(request *http.Request) string {
	if key := request.Header.Get("X-API-Key"); key != "" {
		return key
	}

	host := request.RemoteAddr
	if forwarded, _, err := net.SplitHostPort(host); err == nil {
		host = forwarded
	}
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: KeyFor prefers X-API-Key, then RemoteAddr; first X-Forwarded-For is used only when TrustedProxies is true. The original application was not modified or deployed by this content package.

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
