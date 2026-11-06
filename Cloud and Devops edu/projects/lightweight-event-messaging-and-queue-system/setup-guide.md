# Setup Guide

## Source scope

Run as a local teaching prototype. Do not use it as a durable production message broker.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- All topics/messages/offsets are in memory; restart loses them.
- There are no durable consumer groups, replication, dead-letter queues, or flow control.
- Acknowledgement semantics and retention boundaries are simple prototype behavior, not Kafka/NATS guarantees.
- README says NATS-like concept but implementation is its own Go HTTP API.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
