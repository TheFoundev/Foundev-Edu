# A beginner's model of runtime configuration connected to code

**Lesson ID:** `owasp-crapi-module-06-lesson-1`

## Purpose and learning objectives

Inspect the declared manifests .github/workflows/ci.yml, Dockerfile, k8s/deployment.yaml and trace the relevant package or setting into implementation file src/main/java/io/foundev/crapi/CrapiApplication.java. Separate a declaration from an imported, configured, or executed behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `.github/workflows/ci.yml`, `Dockerfile`, `k8s/deployment.yaml`, `src/main/java/io/foundev/crapi/CrapiApplication.java`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- The excerpt from `.github/workflows/ci.yml` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `Dockerfile` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `k8s/deployment.yaml` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/main/java/io/foundev/crapi/CrapiApplication.java`, `package io.foundev.crapi;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/CrapiApplication.java`, `import org.springframework.boot.SpringApplication;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/CrapiApplication.java`, `import org.springframework.boot.autoconfigure.SpringBootApplication;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public class CrapiApplication {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public static void main(String[] args) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### .github/workflows/ci.yml

```text
name: CI

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'
      - name: Run the tests
        run: mvn -B test

```

### Dockerfile

```text
FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /workspace
COPY pom.xml .
COPY src ./src
RUN mvn -q -DskipTests package

FROM eclipse-temurin:17-jre
WORKDIR /app
COPY --from=build /workspace/target/crapi-0.1.0.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]

```

### k8s/deployment.yaml

```text
apiVersion: apps/v1
kind: Deployment
metadata:
  name: crapi
spec:
  replicas: 1
  selector:
    matchLabels:
      app: crapi
  template:
    metadata:
      labels:
        app: crapi
    spec:
      containers:
        - name: crapi
          image: foundev/crapi:0.1.0
          ports:
            - containerPort: 8080
          env:
            - name: SPRING_PROFILES_ACTIVE
              value: practice

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

This lesson ties its explanation to `.github/workflows/ci.yml`, `Dockerfile`, `k8s/deployment.yaml`, `src/main/java/io/foundev/crapi/CrapiApplication.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
