# Architecture

## Implemented system

Topics/partitions, deterministic key partitioning, publish/fetch, consumer cursor/ack/pending, retention trim, HTTP handlers.

## Data and control flow

Publish(topic,key,payload) → partition/offset → fetch from offset → consumer poll → ack advances cursor → retention trims history.

## Module source map

- **Message, Topic, and Partition Models:** Message carries topic/key/payload/offset/partition; Topic stores partition slices and offsets.
- **Choose a Partition from the Key:** partitionOf(key) hashes key and maps it to the broker's partition count.
- **Publish and Assign Offsets:** Broker.Publish obtains/creates Topic, selects partition, increments per-partition offset.
- **Fetch from an Offset:** Broker.Fetch accepts topic, offset, limit and returns matching messages.
- **Consumer Poll, Ack, and Pending:** Consumer.Poll and Ack track a single offset for that consumer instance.
- **Retention and HTTP API:** NewBroker(retention); PublishHandler/FetchHandler serve JSON.
- **Durability and Delivery Limits:** Topic.Messages is an in-memory slice; the queue has no persistence, replication, durable consumer groups, or dead-letter queue.

## Boundaries and risks

- All topics/messages/offsets are in memory; restart loses them.
- There are no durable consumer groups, replication, dead-letter queues, or flow control.
- Acknowledgement semantics and retention boundaries are simple prototype behavior, not Kafka/NATS guarantees.
- README says NATS-like concept but implementation is its own Go HTTP API.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
