# Assess failure and operational limits of tests and real-ipfs limits

**Lesson ID:** lesson-03  
**Module ID:** module-08  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Tests and Real-IPFS Limits** in Decentralized Storage dApp on IPFS. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Node.js, CIDv1, Multihash, Local filesystem, HTTP. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

Tests cover the local client and content APIs, not integration with an IPFS peer network.

## Move from the idea to the source

Move from the happy path to operational reasoning. For this project, The client only calls a configured node URL; the included app does not provide an IPFS daemon, pinning service, replication, or garbage collection.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. Identify a failure, boundary, or unexpected input.
2. Use `src/ipfs.js` and the `DEFAULT_API` path to predict behavior: The client only calls a configured node URL; the included app does not provide an IPFS daemon, pinning service, replication, or garbage collection.
3. Describe a safe local/test verification and what evidence to collect.
4. State what additional code or infrastructure would be needed before making a production claim.

## Source-code walkthrough

**Source file(s):** test/ipfs.test.js; src/ipfs.js; README.md

**Source:** `src/ipfs.js:5–14`  
**Focus cue:** `DEFAULT_API`

````js
*
 * The API of a node is reached over a URL, so the client works against a
 * node on the machine and against one behind a gateway.
 */

const DEFAULT_API = "http://127.0.0.1:5001";

/**
 * The client of an IPFS node.
 */
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: The client only calls a configured node URL; the included app does not provide an IPFS daemon, pinning service, replication, or garbage collection. The original application was not modified or deployed by this content package.

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
