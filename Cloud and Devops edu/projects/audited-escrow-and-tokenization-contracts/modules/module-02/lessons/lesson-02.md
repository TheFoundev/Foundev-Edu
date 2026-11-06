# Trace the source implementation for escrow state machine

**Lesson ID:** lesson-02  
**Module ID:** module-02  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Escrow State Machine** in Audited Escrow and Tokenization Contracts. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Solidity 0.8.24, Hardhat, TypeScript, ethers.js, OpenZeppelin Contracts. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

A state machine is a set of checkpoints; each operation is allowed only at particular checkpoints.

## Move from the idea to the source

Now trace the implementation for Escrow State Machine. The source evidence is: States: Created, Funded, Disputed, ArbiterDecided, Released, Refunded; invalid transitions revert with custom errors.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. Open `contracts/Escrow.sol` and locate `ArbiterDecided`.
2. Trace values from input to state changes and result.
3. Compare the actual code excerpt with the authored source finding: States: Created, Funded, Disputed, ArbiterDecided, Released, Refunded; invalid transitions revert with custom errors.
4. Separate source behavior from external infrastructure.

## Source-code walkthrough

**Source file(s):** contracts/Escrow.sol

**Source:** `contracts/Escrow.sol:345–354`  
**Focus cue:** `ArbiterDecided`

````sol
emit RulingRecorded(msg.sender, releaseToSeller);
    }

    /// @notice Anyone may execute a recorded ruling and book the credit.
    function executeRuling() external {
        if (state != State.ArbiterDecided) revert InvalidState(State.ArbiterDecided, state);

        if (rulingForSeller) {
            _settle(State.Released, seller, msg.sender);
        } else {
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: States: Created, Funded, Disputed, ArbiterDecided, Released, Refunded; invalid transitions revert with custom errors. The original application was not modified or deployed by this content package.

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
