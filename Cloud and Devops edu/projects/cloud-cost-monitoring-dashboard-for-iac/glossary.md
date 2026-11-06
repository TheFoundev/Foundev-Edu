# Glossary

- **Control plane:** Components that store desired configuration and coordinate changes to managed resources.
- **Data plane:** Components that carry application requests, messages, or user data.
- **Reconciliation:** Repeatedly compare desired and observed state and apply changes to reduce the difference.
- **Idempotency:** Repeating an operation with the same identity should not create unintended duplicate effects.
- **Quorum:** A majority threshold used to make decisions despite some unavailable members.
- **Retry/backoff:** Reattempt a failed operation, often after increasing delays.
- **Dead-letter queue:** A separate destination for messages that cannot be processed normally.
- **Content address:** Identifier derived from data bytes and encoding parameters.
- **KDF:** Key-derivation function that turns a password/secret and salt into key material.
- **Authenticated encryption:** Encryption that also detects modification of ciphertext.
- **Threat model:** A description of assets, attackers, trust boundaries, and failure consequences.
- **SLO/steady-state hypothesis:** A measurable statement about acceptable service behavior.
- **Artifact:** A file or build output passed between workflow steps or stored for later use.
- **Simulation:** A local model that demonstrates logic without contacting the real external service.
- **Least privilege:** Granting only the permissions required for a task.
