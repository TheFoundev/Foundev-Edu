# A beginner's model of documented goals mapped to implementation

**Lesson ID:** `userspace-tcp-ip-stack-module-05-lesson-1`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors src/main.c, src/packet.c, src/packet.h. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `README.md`, `src/main.c`, `src/packet.c`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/main.c`, `#include "packet.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main.c`, `#include <stdio.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/packet.c`, `#include "packet.h"` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/packet.c`, `#include <string.h>` brings a module or package name into this file; follow later references before claiming it is used on a running path.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### README.md

```text
# Userspace TCP/IP Stack

Parse and build Ethernet, IPv4 and TCP headers in userspace.

> A small userspace TCP/IP stack written for learning how protocols are implemented end to end.

## Overview

An original, self-contained implementation of the **Userspace TCP/IP Stack** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Header parsing with length checks
- Internet checksum computation and verification
- Packet builder for IPv4 and TCP
- Loopback stack that maps ports to handlers

## Stack

`C; POSIX`
The CSV stack is C + POSIX. This build works on raw byte buffers and an in-process loopback; the TUN/TAP device is documented but not opened in tests.

## Run

```bash
make
./build/app
make test
```

## Structure

```text
userspace-tcp-ip-stack/
├── src/packet.c            header parsing and building
├── src/packet.h            structs and API
├── src/main.c              demo program
├── tests/test_main.c       unit tests
└── Makefile
```

## Testing

```bash
make test
```

6 tests (`make test`), up from 2: the checksum, the byte order helpers, the headers and a packet that is built.


## Notes and limitations

- There is no congestion control, retransmission or TCP state machine.
- The TUN device code is optional and needs root to run.
- Only IPv4 is supported.

## License

MIT. See `LICENSE`.

## About the scope

This is a third-year student project. The build and tests run locally with GCC; there is no portability work beyond the platforms named in the notes.

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

### src/packet.c

```text
#include "packet.h"

#include <string.h>

uint16_t packet_read_u16(const uint8_t *data) {
    return (uint16_t)((data[0] << 8) | data[1]);
}

uint32_t packet_read_u32(const uint8_t *data) {
    return ((uint32_t)data[0] << 24) | ((uint32_t)data[1] << 16) |
           ((uint32_t)data[2] << 8) | (uint32_t)data[3];
}

void packet_write_u16(uint8_t *data, uint16_t value) {
    data[0] = (uint8_t)(value >> 8);
    data[1] = (uint8_t)(value & 0xff);
}

void packet_write_u32(uint8_t *data, uint32_t value) {
    data[0] = (uint8_t)(value >> 24);
    data[1] = (uint8_t)(value >> 16);
    data[2] = (uint8_t)(value >> 8);
    data[3] = (uint8_t)(value & 0xff);
}

uint16_t packet_checksum(const uint8_t *data, size_t length) {
    uint32_t sum = 0;
    size_t index;
    for (index = 0; index + 1 < length; index += 2) {
        sum += packet_read_u16(data + index);
    }
    if (index < length) {
        sum += (uint16_t)(data[index] << 8);
    }
    while (sum >> 16) {
        sum = (sum & 0xffff) + (sum >> 16);
    }
    return (uint16_t)(~sum);
}

int packet_parse_ethernet(const uint8_t *data, size_t length, ethernet_header_t *header) {
    if (length < ETHERNET_HEADER) {
        return 0;
    }
    memcpy(header->destination, data, 6);
    memcpy(header->source, data + 6, 6);
    header->ethertype = packet_read_u16(data + 12);
    return ETHERNET_HEADER;
}

int packet_parse_ipv4(const uint8_t *data, size_t length, ipv4_header_t *header) {
    size_t header_length;
    if (length < IPV4_HEADER) {
        return 0;
    }
    header->version_ihl = data[0];
    if ((header->version_ihl >> 4) != 4) {
        return 0;
    }
    header_length = (size_t)(header->version_ihl & 0x0f) * 4u;
    if (header_length < IPV4_HEADER || length < header_length) {
        return 0;
    }
    header->total_length = packet_read_u16(data + 2);
    header->identification = packet_read_u16(data + 4);
    header->flags_fragment = packet_read_u16(data + 6);
    header->ttl = data[8];
    header->protocol = data[9];
    header->checksum = packet_read_u16(data + 10);
    header->source = packet_read_u32(data + 12);
    header->destination = packet_read_u32(data + 16);
    return (int)header_length;
}

int packet_parse_tcp(const uint8_t *data, size_t length, tcp_header_t *header) {
    if (length < TCP_HEADER) {
        return 0;
    }
    header->source_port = packet_read_u16(data);
    header->destination_port = packet_read_u16(data + 2);
    header->sequence = packet_read_u32(data + 4);
    header->acknowledgement = packet_read_u32(data + 8);
    header->data_offset = data[12];
    header->flags = data[13];
    header->window = packet_read_u16(data + 14);
    header->checksum = packet_read_u16(data + 16);
    header->urgent = packet_read_u16(data + 18);
    return TCP_HEADER;
}

size_t packet_build_ipv4_tcp(uint8_t *buffer, size_t capacity, uint32_t source, uint32_t destination,
                             uint16_t source_port, uint16_t destination_port,
                             const uint8_t *payload, size_t payload_length) {
    size_t total = IPV4_HEADER + TCP_HEADER + payload_length;
    uint8_t *ip = buffer;
    uint8_t *tcp = buffer + IPV4_HEADER;
    if (capacity < total) {
        return 0;
    }
    memset(buffer, 0, total);
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

This lesson ties its explanation to `README.md`, `src/main.c`, `src/packet.c`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
