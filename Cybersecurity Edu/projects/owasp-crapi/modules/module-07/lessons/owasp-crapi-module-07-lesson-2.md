# Read documented goals mapped to implementation in the source

**Lesson ID:** `owasp-crapi-module-07-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors src/main/java/io/foundev/crapi/CrapiApplication.java, src/main/java/io/foundev/crapi/model/User.java, src/main/java/io/foundev/crapi/repository/UserRepository.java. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `src/main/java/io/foundev/crapi/CrapiApplication.java`, `src/main/java/io/foundev/crapi/model/User.java`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/main/java/io/foundev/crapi/CrapiApplication.java`, `package io.foundev.crapi;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/CrapiApplication.java`, `import org.springframework.boot.SpringApplication;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/CrapiApplication.java`, `import org.springframework.boot.autoconfigure.SpringBootApplication;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public class CrapiApplication {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public static void main(String[] args) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/main/java/io/foundev/crapi/model/User.java`, `package io.foundev.crapi.model;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/model/User.java`, `import jakarta.persistence.Entity;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/model/User.java`, `import jakarta.persistence.GeneratedValue;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/model/User.java`, `import jakarta.persistence.GenerationType;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/model/User.java`, `import jakarta.persistence.Id;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public class User {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public Long getId() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public String getEmail() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public void setEmail(String email) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public String getPassword() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public void setPassword(String password) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
# OWASP crAPI

A vulnerable REST API for practising the OWASP API Top 10.

> A deliberately vulnerable API-first application for practising modern API security testing in an authorised lab.

## Overview

An original, self-contained implementation of the **OWASP crAPI** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- User and vehicle REST resources with insecure direct object references
- Tokens issued as unsigned JWTs and accepted without verification
- Mass assignment on the signup endpoint
- Seed data for the standard practice scenarios

## Stack

`JUnit; Java; Spring Boot`
The CSV stack is JUnit + Java + Spring Boot. javac is not installed here, so this is source-only: the Maven project, Spring controllers and Dockerfile are complete but were not compiled.

## Run

```bash
mvn spring-boot:run  # needs a JDK (javac is not installed here)
```

## Structure

```text
owasp-crapi/
├── pom.xml                 Maven project
├── src/main/java/          Spring Boot controllers and models
├── src/test/java/          the token test and the MockMvc scenario tests
├── Dockerfile
└── k8s/deployment.yaml
```

## Testing

```bash
mvn test        # 9 tests: the token service and the MockMvc scenarios
```

The suite has two parts:

- `TokenServiceTest`: the token service reads the subject it issued.
- `VulnerabilityScenarioTest`: the MockMvc tests that prove every practice
  scenario is reachable — the IDOR on `/identity/api/users/{id}`, the
  unsigned token, the mass assignment at signup (the client chooses its own
  role), the duplicate email and the vehicle endpoints that need no
  authentication. They assert that the vulnerable behaviour is still there, so
  a fix has to be a deliberate change.

The project is compiled with `-parameters` (set in `pom.xml`), without which
Spring cannot bind the `@PathVariable` names and every path endpoint fails
at runtime.

## Notes and limitations

- The application is deliberately vulnerable; do not deploy it publicly.
- Password hashing is intentionally absent for the practice scenarios.
- Only the main endpoints from the practice guide are implemented.

## License

Apache-2.0. See `LICENSE`.

## About the scope

This is a third-year student project. The listed toolchain was not available in this environment, so the repository is source-only and was checked by structural validation.

```

### src/main/java/io/foundev/crapi/CrapiApplication.java

```text
package io.foundev.crapi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class CrapiApplication {

    public static void main(String[] args) {
        SpringApplication.run(CrapiApplication.class, args);
    }
}

```

### src/main/java/io/foundev/crapi/model/User.java

```text
package io.foundev.crapi.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String email;
    private String password;
    private String name;
    private String role;

    public Long getId() {
        return id;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = [REDACTED];
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
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

This lesson ties its explanation to `README.md`, `src/main/java/io/foundev/crapi/CrapiApplication.java`, `src/main/java/io/foundev/crapi/model/User.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
