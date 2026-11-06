# Read user and userrepository in the source

**Lesson ID:** `owasp-crapi-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/main/java/io/foundev/crapi/model/User.java] and [src/main/java/io/foundev/crapi/repository/UserRepository.java]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include User, getId, getEmail, setEmail, getPassword, setPassword, getName, setName, UserRepository; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/main/java/io/foundev/crapi/model/User.java`, `src/main/java/io/foundev/crapi/repository/UserRepository.java`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

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
- In `src/main/java/io/foundev/crapi/repository/UserRepository.java`, `package io.foundev.crapi.repository;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/repository/UserRepository.java`, `import io.foundev.crapi.model.User;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/repository/UserRepository.java`, `import java.util.Optional;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/repository/UserRepository.java`, `import org.springframework.data.jpa.repository.JpaRepository;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public interface UserRepository extends JpaRepository<User, Long> {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### src/main/java/io/foundev/crapi/repository/UserRepository.java

```text
package io.foundev.crapi.repository;

import io.foundev.crapi.model.User;
import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> findByEmail(String email);
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

This lesson ties its explanation to `src/main/java/io/foundev/crapi/model/User.java`, `src/main/java/io/foundev/crapi/repository/UserRepository.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
