# A beginner's model of vehiclecontroller

**Lesson ID:** `owasp-crapi-module-04-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/main/java/io/foundev/crapi/web/VehicleController.java]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include VehicleController; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/main/java/io/foundev/crapi/web/VehicleController.java`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/main/java/io/foundev/crapi/web/VehicleController.java`, `package io.foundev.crapi.web;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/web/VehicleController.java`, `import java.util.ArrayList;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/web/VehicleController.java`, `import java.util.List;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/web/VehicleController.java`, `import java.util.Map;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/web/VehicleController.java`, `import org.springframework.web.bind.annotation.GetMapping;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public class VehicleController {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/main/java/io/foundev/crapi/web/VehicleController.java

```text
package io.foundev.crapi.web;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/identity/api/v2")
public class VehicleController {

    @GetMapping("/vehicles")
    public Map<String, Object> list(
            @RequestParam(name = "limit", defaultValue = "20") int limit,
            @RequestParam(name = "offset", defaultValue = "0") String offset,
            @RequestParam(name = "order", defaultValue = "id") String order) {
        // The offset is used as a raw query fragment in the original application;
        // here it is echoed back so the injection point is visible in the response.
        List<Map<String, Object>> vehicles = new ArrayList<>();
        for (int index = 0; index < limit; index++) {
            vehicles.add(Map.of("id", index, "model", "model-" + index));
        }
        return Map.of("vehicles", vehicles, "queryOffset", offset, "order", order);
    }

    @GetMapping("/vehicles/{id}/location")
    public Map<String, String> location(@PathVariable String id) {
        // No authentication at all on this endpoint.
        return Map.of("vehicleId", id, "latitude", "52.3702", "longitude", "4.8952");
    }
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

This lesson ties its explanation to `src/main/java/io/foundev/crapi/web/VehicleController.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
