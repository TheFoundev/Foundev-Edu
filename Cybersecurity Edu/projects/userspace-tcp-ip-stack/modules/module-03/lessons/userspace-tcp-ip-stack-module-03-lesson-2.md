# Read test code and implementation evidence in the source

**Lesson ID:** `userspace-tcp-ip-stack-module-03-lesson-2`

## Purpose and learning objectives

Read the test cases in tests/test_main.c beside the implementation in src/main.c. Explain the behavior asserted by the tests and trace each assertion to the implementation. A test file describes a check; it does not prove that check passed.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `tests/test_main.c`, `src/main.c`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `tests/test_main.c`, `#include <assert.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_main.c`, `#include <stdio.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_main.c`, `#include <string.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_main.c`, `#include "../src/packet.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main.c`, `#include "packet.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main.c`, `#include <stdio.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### tests/test_main.c

```text
#include <assert.h>
#include <stdio.h>
#include <string.h>

#include "../src/packet.h"

static void test_the_checksum(void) {
    uint8_t header[20];
    memset(header, 0, sizeof(header));
    header[0] = 0x45;
    header[3] = 20;

    uint16_t checksum = packet_checksum(header, sizeof(header));
    // The checksum of a header that has the checksum in it is zero.
    header[10] = (uint8_t)(checksum >> 8);
    header[11] = (uint8_t)(checksum & 0xff);
    assert(packet_checksum(header, sizeof(header)) == 0);
}

static void test_read_and_write(void) {
    uint8_t buffer[4] = {0x12, 0x34, 0x56, 0x78};
    assert(packet_read_u16(buffer) == 0x1234);
    assert(packet_read_u32(buffer) == 0x12345678u);

    uint8_t out[4];
    packet_write_u16(out, 0xabcd);
    assert(out[0] == 0xab && out[1] == 0xcd);
    packet_write_u32(out, 0x01020304u);
    assert(out[0] == 1 && out[3] == 4);
}

static void test_the_ipv4_header_is_parsed(void) {
    uint8_t packet[20];
    memset(packet, 0, sizeof(packet));
    packet[0] = 0x45;
    packet[9] = 6;

    ipv4_header_t header;
    // The length of the header is returned, and zero when the packet is
    // broken.
    assert(packet_parse_ipv4(packet, sizeof(packet), &header) == IPV4_HEADER);
    assert((header.version_ihl >> 4) == 4);
    assert(header.protocol == 6);
}

static void test_the_tcp_header_is_parsed(void) {
    uint8_t packet[20];
    memset(packet, 0, sizeof(packet));
    packet[0] = 0x50;
    packet_write_u16(packet, 1234);
    packet_write_u16(packet + 2, 443);

    tcp_header_t header;
    assert(packet_parse_tcp(packet, sizeof(packet), &header) == TCP_HEADER);
    assert(header.source_port == 1234);
    assert(header.destination_port == 443);
}

static void test_a_short_buffer_is_refused(void) {
    uint8_t packet[4] = {0x45, 0, 0, 0};
    ipv4_header_t header;
    // A packet that is too short is refused.
    assert(packet_parse_ipv4(packet, sizeof(packet), &header) == 0);
}

static void test_a_packet_is_built(void) {
    uint8_t buffer[64];
    uint8_t payload[4] = {1, 2, 3, 4};

    size_t length = packet_build_ipv4_tcp(buffer, sizeof(buffer), 0x0a000001, 0x0a000002,
                                        1234, 80, payload, sizeof(payload));
    assert(length >= IPV4_HEADER + TCP_HEADER + sizeof(payload));

    ipv4_header_t ip;
    assert(packet_parse_ipv4(buffer, length, &ip) == IPV4_HEADER);
    assert(ip.protocol == 6);
}

int main(void) {
    test_the_checksum();
    test_read_and_write();
    test_the_ipv4_header_is_parsed();
    test_the_tcp_header_is_parsed();
    test_a_short_buffer_is_refused();
    test_a_packet_is_built();
    printf("all packet tests passed\n");
    return 0;
}

```

### src/main.c

```text
#include "packet.h"

#include <stdio.h>

int main(void) {
    uint8_t buffer[256];
    ipv4_header_t ip;
    tcp_header_t tcp;
    size_t total;
    const char *payload = "hello";

    total = packet_build_ipv4_tcp(buffer, sizeof(buffer), 0x0a000001u, 0x0a000002u,
                                  12345, 80, (const uint8_t *)payload, 5);
    printf("built %zu bytes\n", total);
    if (packet_parse_ipv4(buffer, total, &ip) == 0) {
        fprintf(stderr, "bad ip header\n");
        return 1;
    }
    if (packet_parse_tcp(buffer + IPV4_HEADER, total - IPV4_HEADER, &tcp) == 0) {
        fprintf(stderr, "bad tcp header\n");
        return 1;
    }
    printf("ip ttl=%u protocol=%u checksum=0x%04x\n", ip.ttl, ip.protocol, ip.checksum);
    printf("tcp %u -> %u flags=0x%02x\n", tcp.source_port, tcp.destination_port, tcp.flags);
    printf("ipv4 checksum valid: %s\n", packet_checksum(buffer, IPV4_HEADER) == 0 ? "yes" : "no");
    return 0;
}

```

The excerpt comes from this project’s source tree and may omit context. It is not evidence that the source was executed. Never treat a listed function name alone as proof that a user-facing path reaches it.

## Expected behavior and known limits

Only behavior visible in the cited implementation or assertions can be explained as implemented. External calls, deployment settings, successful installation, performance, and test outcomes remain unverified here.

## Practical exercise

Use the module exercise to create a call/data/configuration trace for these exact files. Include a source location for every claim.

## Common mistakes and debugging

- Reading only function names: follow bodies, callers, and return paths.
- Assuming imports prove an integration ran: inspect the call site and configuration.
- Assuming tests pass because they exist: record execution separately.
- If the path is unclear, search all references to the symbol and trace from the actual entry point.

## Best practices and security

Use synthetic fixtures and isolated environments. Redact credentials and personal data. Review validation at input boundaries, dependency declarations, and error handling before suggesting a change. These security projects are dual-use: scan, intercept, phish, or operate honeypots only on systems you own or have explicit authorization to test. Keep intentionally vulnerable apps and security labs isolated, and use synthetic targets and credentials.

## Summary

This lesson ties its explanation to `tests/test_main.c`, `src/main.c`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
