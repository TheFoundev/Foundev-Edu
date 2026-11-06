# Mentor Solution Guide

## Source findings

The project implements: Keccak implementation, address helper, decimal-unit conversion, transfer ABI encoder, static page, browser wallet connection and eth_sendTransaction call.

Review known limitations:
- No contract deployment, on-chain state reader, event listener, or transaction history is implemented.
- The UI checks address shape but does not call EIP-55 checksum validation before encoding.
- No EIP-55 checksum checking is implemented according to README; custom Keccak code needs independent validation before financial use.
- Wallet connection and sending requests require an injected provider; a transaction hash does not mean confirmation/success.
- Only ERC20 transfer calldata is encoded; token contract semantics are not verified.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
