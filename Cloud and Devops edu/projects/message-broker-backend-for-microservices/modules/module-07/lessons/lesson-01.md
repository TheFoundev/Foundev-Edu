# Explain retry ladder and dead-letter queue using a plain-language model

**Lesson ID:** lesson-01  
**Module ID:** module-07  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Retry Ladder and Dead-Letter Queue** in Message Broker Backend for Microservices. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Erlang/OTP, RabbitMQ, AMQP, Docker Compose, Prometheus. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

A retry queue delays a message before routing it back; a dead-letter queue holds exhausted or terminal failures.

## Move from the idea to the source

Begin with this mental model: A retry queue delays a message before routing it back; a dead-letter queue holds exhausted or terminal failures. Identify the actual components in src/mbb_topology.erl; src/mbb_consumer.erl; rabbitmq/definitions.json.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. State the idea in your own words before reading code.
2. Open `src/mbb_consumer.erl` at the cited lines and identify the input and output.
3. Compare the analogy with the implementation: Retry TTL grows as base × 4^(N-1); x-retry-count and max_retries govern exhaustion.
4. Write one question the analogy does not answer about real deployments.

## Source-code walkthrough

**Source file(s):** src/mbb_topology.erl; src/mbb_consumer.erl; rabbitmq/definitions.json

**Source:** `src/mbb_consumer.erl:11–20`  
**Focus cue:** `max_retries`

````erl
%%%   <li>`ok' -> ack; `{retry, R}' -> republish into the next
%%%       `orders.retry.N' queue with `x-retry-count' incremented and
%%%       ack (the queue's `x-message-ttl' + dead-letter-back provides
%%%       the delay); `{dead_letter, R}' -> republish to `orders.dlq'
%%%       with `x-dlq-reason' and ack;</li>
%%%   <li>a retry whose `x-retry-count' has reached `max_retries' is
%%%       dead-lettered with `retries_exhausted' instead of looping.</li>
%%% </ol>
%%%
%%% Backpressure: the channel prefetch (set by mbb_connection) bounds how
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: Retry TTL grows as base × 4^(N-1); x-retry-count and max_retries govern exhaustion. The original application was not modified or deployed by this content package.

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
