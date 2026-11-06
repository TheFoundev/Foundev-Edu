# Lightweight Event Messaging and Queue System

## Overview and purpose

A Go in-memory broker partitions topics by key, appends messages, fetches by offset, and tracks one consumer offset.

## Real-world context

Understand ordering, partitions, offsets, acknowledgements, retention, and the limitations of a memory-only queue.

## Implemented features

Topics/partitions, deterministic key partitioning, publish/fetch, consumer cursor/ack/pending, retention trim, HTTP handlers.

## Source findings and limitations

- All topics/messages/offsets are in memory; restart loses them.
- There are no durable consumer groups, replication, dead-letter queues, or flow control.
- Acknowledgement semantics and retention boundaries are simple prototype behavior, not Kafka/NATS guarantees.
- README says NATS-like concept but implementation is its own Go HTTP API.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Go, HTTP JSON API, in-memory queue. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Publish(topic,key,payload) → partition/offset → fetch from offset → consumer poll → ack advances cursor → retention trims history.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 7. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
