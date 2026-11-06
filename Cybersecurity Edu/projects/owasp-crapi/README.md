# Owasp Crapi

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

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
  unsigned token

## Actual features and limits

README feature statements (verify each against code before relying on it):
- User and vehicle REST resources with insecure direct object references
- Tokens issued as unsigned JWTs and accepted without verification
- Mass assignment on the signup endpoint
- Seed data for the standard practice scenarios
- `TokenServiceTest`: the token service reads the subject it issued.
- `VulnerabilityScenarioTest`: the MockMvc tests that prove every practice
- The application is deliberately vulnerable; do not deploy it publicly.
- Password hashing is intentionally absent for the practice scenarios.
- Only the main endpoints from the practice guide are implemented.

The implementation inventory includes 21 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `the repository dependency/configuration files`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `Dockerfile`
- `README.extra.md`
- `README.md`
- `k8s/deployment.yaml`
- `pom.xml`
- `src/main/java/io/foundev/crapi/CrapiApplication.java`
- `src/main/java/io/foundev/crapi/model/User.java`
- `src/main/java/io/foundev/crapi/repository/UserRepository.java`
- `src/main/java/io/foundev/crapi/security/TokenService.java`
- `src/main/java/io/foundev/crapi/web/UserController.java`
- `src/main/java/io/foundev/crapi/web/VehicleController.java`
- `src/test/java/io/foundev/crapi/TokenServiceTest.java`
- `src/test/java/io/foundev/crapi/VulnerabilityScenarioTest.java`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: src/test/java/io/foundev/crapi/TokenServiceTest.java, src/test/java/io/foundev/crapi/VulnerabilityScenarioTest.java. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
