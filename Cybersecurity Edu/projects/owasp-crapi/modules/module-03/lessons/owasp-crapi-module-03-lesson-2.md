# Read tokenservice and usercontroller in the source

**Lesson ID:** `owasp-crapi-module-03-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/main/java/io/foundev/crapi/security/TokenService.java] and [src/main/java/io/foundev/crapi/web/UserController.java]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include TokenService, issue, readUserId, UserController; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/main/java/io/foundev/crapi/security/TokenService.java`, `src/main/java/io/foundev/crapi/web/UserController.java`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/main/java/io/foundev/crapi/security/TokenService.java`, `package io.foundev.crapi.security;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/security/TokenService.java`, `import java.nio.charset.StandardCharsets;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/security/TokenService.java`, `import java.util.Base64;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public class TokenService {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public String issue(long userId, String role) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public long readUserId(String token) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/main/java/io/foundev/crapi/web/UserController.java`, `package io.foundev.crapi.web;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/web/UserController.java`, `import io.foundev.crapi.model.User;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/web/UserController.java`, `import io.foundev.crapi.repository.UserRepository;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/web/UserController.java`, `import io.foundev.crapi.security.TokenService;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/web/UserController.java`, `import java.util.Map;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public class UserController {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/main/java/io/foundev/crapi/security/TokenService.java

```text
package io.foundev.crapi.security;

import java.nio.charset.StandardCharsets;
import java.util.Base64;

// Deliberately unsigned tokens. Any payload the client sends back is trusted,
// which is the point of the practice scenario.
public class TokenService {

    public String issue(long userId, String role) {
        String header = encode("{\"alg\":\"none\",\"typ\":\"JWT\"}");
        String payload = encode("{\"sub\":\"" + userId + "\",\"role\":\"" + role + "\"}");
        return header + "." + payload + ".";
    }

    public long readUserId(String token) {
        String[] parts = token.split("\\.");
        String payload = new String(Base64.getUrlDecoder().decode(parts[1]), StandardCharsets.UTF_8);
        String marker = "\"sub\":\"";
        int start = payload.indexOf(marker) + marker.length();
        int end = payload.indexOf('"', start);
        return Long.parseLong(payload.substring(start, end));
    }

    private String encode(String json) {
        return Base64.getUrlEncoder().withoutPadding().encodeToString(json.getBytes(StandardCharsets.UTF_8));
    }
}

```

### src/main/java/io/foundev/crapi/web/UserController.java

```text
package io.foundev.crapi.web;

import io.foundev.crapi.model.User;
import io.foundev.crapi.repository.UserRepository;
import io.foundev.crapi.security.TokenService;
import java.util.Map;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/identity/api")
public class UserController {

    private final UserRepository users;
    private final TokenService tokens = new TokenService();

    public UserController(UserRepository users) {
        this.users = users;
    }

    @PostMapping("/auth/signup")
    public ResponseEntity<?> signup(@RequestBody User request) {
        // Mass assignment: the client can set any field, including role.
        users.findByEmail(request.getEmail()).ifPresent(existing -> {
            throw new IllegalStateException("email already registered");
        });
        User saved = users.save(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(Map.of("id", saved.getId()));
    }

    @PostMapping("/auth/login")
    public ResponseEntity<?> login(@RequestBody Map<String, String> body) {
        return users.findByEmail(body.get("email"))
                .filter(user -> user.getPassword().equals(body.get("password")))
                .map(user -> ResponseEntity.ok(Map.of("token", tokens.issue(user.getId(), user.getRole()))))
                .orElseGet(() -> ResponseEntity.status(HttpStatus.UNAUTHORIZED).build());
    }

    @GetMapping("/users/{id}")
    public ResponseEntity<?> findById(@PathVariable long id) {
        // No ownership check: any authenticated caller can read any user.
        return users.findById(id)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
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

This lesson ties its explanation to `src/main/java/io/foundev/crapi/security/TokenService.java`, `src/main/java/io/foundev/crapi/web/UserController.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
