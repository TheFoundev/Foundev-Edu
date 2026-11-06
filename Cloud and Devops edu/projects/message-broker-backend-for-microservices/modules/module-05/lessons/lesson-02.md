# Trace the source implementation for consume with prefetch and settlement

**Lesson ID:** lesson-02  
**Module ID:** module-05  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Consume with Prefetch and Settlement** in Message Broker Backend for Microservices. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Erlang/OTP, RabbitMQ, AMQP, Docker Compose, Prometheus. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

Prefetch limits unacknowledged messages; ack says done, retry/requeue or dead-letter handles failures.

## Move from the idea to the source

Now trace the implementation for Consume with Prefetch and Settlement. The source evidence is: Consumer classifies outcomes and settles deliveries; pipeline returns ok/retry/dead_letter.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. Open `src/mbb_consumer.erl` and locate `dead_letter`.
2. Trace values from input to state changes and result.
3. Compare the actual code excerpt with the authored source finding: Consumer classifies outcomes and settles deliveries; pipeline returns ok/retry/dead_letter.
4. Separate source behavior from external infrastructure.

## Source-code walkthrough

**Source file(s):** src/mbb_consumer.erl

**Source:** `src/mbb_consumer.erl:231–240`  
**Focus cue:** `dead_letter`

````erl
-spec decode_and_process(binary()) -> mbb_order:outcome().
decode_and_process(Payload) ->
    case mbb_order:from_json(Payload) of
        {ok, Order} -> mbb_order:process(Order);
        {error, Reason} -> {dead_letter, {malformed_json, Reason}}
    end.

-spec settle(mbb_order:outcome(), binary(), term(), list() | undefined,
             binary(), map()) -> map().
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: Consumer classifies outcomes and settles deliveries; pipeline returns ok/retry/dead_letter. The original application was not modified or deployed by this content package.

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
