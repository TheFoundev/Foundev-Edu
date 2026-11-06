# A beginner's model of test code and implementation evidence

**Lesson ID:** `owasp-crapi-module-05-lesson-1`

## Purpose and learning objectives

Read the test cases in src/test/java/io/foundev/crapi/TokenServiceTest.java, src/test/java/io/foundev/crapi/VulnerabilityScenarioTest.java beside the implementation in src/main/java/io/foundev/crapi/security/TokenService.java. Explain the behavior asserted by the tests and trace each assertion to the implementation. A test file describes a check; it does not prove that check passed.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/test/java/io/foundev/crapi/TokenServiceTest.java`, `src/test/java/io/foundev/crapi/VulnerabilityScenarioTest.java`, `src/main/java/io/foundev/crapi/security/TokenService.java`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/test/java/io/foundev/crapi/TokenServiceTest.java`, `package io.foundev.crapi;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/io/foundev/crapi/TokenServiceTest.java`, `import static org.junit.jupiter.api.Assertions.assertEquals;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/io/foundev/crapi/TokenServiceTest.java`, `import io.foundev.crapi.security.TokenService;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/io/foundev/crapi/TokenServiceTest.java`, `import org.junit.jupiter.api.Test;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class TokenServiceTest {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/test/java/io/foundev/crapi/VulnerabilityScenarioTest.java`, `package io.foundev.crapi;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/io/foundev/crapi/VulnerabilityScenarioTest.java`, `import static org.junit.jupiter.api.Assertions.assertThrows;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/io/foundev/crapi/VulnerabilityScenarioTest.java`, `import static org.junit.jupiter.api.Assertions.assertTrue;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/io/foundev/crapi/VulnerabilityScenarioTest.java`, `import static org.mockito.ArgumentMatchers.any;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/test/java/io/foundev/crapi/VulnerabilityScenarioTest.java`, `import static org.mockito.Mockito.when;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class VulnerabilityScenarioTest {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/main/java/io/foundev/crapi/security/TokenService.java`, `package io.foundev.crapi.security;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/security/TokenService.java`, `import java.nio.charset.StandardCharsets;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/main/java/io/foundev/crapi/security/TokenService.java`, `import java.util.Base64;` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `public class TokenService {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public String issue(long userId, String role) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `public long readUserId(String token) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/test/java/io/foundev/crapi/TokenServiceTest.java

```text
package io.foundev.crapi;

import static org.junit.jupiter.api.Assertions.assertEquals;

import io.foundev.crapi.security.TokenService;
import org.junit.jupiter.api.Test;

class TokenServiceTest {

    @Test
    void readsTheSubjectItIssued() {
        TokenService tokens = new TokenService();
        String token = [REDACTED], "user");
        assertEquals(42L, tokens.readUserId(token));
    }
}

```

### src/test/java/io/foundev/crapi/VulnerabilityScenarioTest.java

```text
package io.foundev.crapi;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import io.foundev.crapi.model.User;
import io.foundev.crapi.repository.UserRepository;
import io.foundev.crapi.web.UserController;
import io.foundev.crapi.web.VehicleController;
import jakarta.servlet.ServletException;
import java.util.Optional;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.util.ReflectionTestUtils;
import org.springframework.test.web.servlet.MockMvc;

/**
 * The vulnerabilities of the practice application are reachable, and that is
 * the point of the exercise: every test below asserts that a broken
 * behaviour is still broken, so a "fix" has to be a deliberate change.
 */
@WebMvcTest(controllers = {UserController.class, VehicleController.class})
class VulnerabilityScenarioTest {

    @Autowired
    private MockMvc mvc;

    @MockBean
    private UserRepository users;

    private User victim;

    @BeforeEach
    void setUp() {
        victim = new User();
        ReflectionTestUtils.setField(victim, "id", 1L);
        victim.setEmail("victim@example.com");
        victim.setPassword("hunter2");
        victim.setName("Victim");
        victim.setRole("user");
    }

    @Test
    void anyCallerCanReadAnyUser() throws Exception {
        when(users.findById(1L)).thenReturn(Optional.of(victim));

        // There is no token and no ownership check: the read succeeds.
        mvc.perform(get("/identity/api/users/1"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.email").value("victim@example.com"));
    }

    @Test
    void anUnknownUserIsNotFound() throws Exception {
        when(users.findById(404L)).thenReturn(Optional.empty());

        mvc.perform(get("/identity/api/users/404"))
                .andExpect(status().isNotFound());
    }

    @Test
    void theClientCanChooseItsOwnRoleAtSignup() throws Exception {
        when(users.findByEmail(any())).thenReturn(Optional.empty());
        when(users.save(any(User.class))).thenAnswer(call -> {
            User saved = call.getArgument(0);
            ReflectionTestUtils.setField(saved, "id", 2L);
            return saved;
        });

        // Mass assignment: the role of the body is kept as it is.
        mvc.perform(post("/identity/api/auth/signup")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"email\":\"new@example.com\",\"password\":\"x\",\"name\":\"New\","
                                + "\"role\":\"admin\"}"))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.id").value(2));
    }

    @Test
    void aDuplicateEmailIsRefused() throws Exception {
        when(users.findByEmail("victim@example.com")).thenReturn(Optional.of(victim));

        // The controller throws from inside a lambda, so the request fails
        // with a 500 instead of a 409.
        ServletException failure = assertThrows(ServletException.class,
                () -> mvc.perform(post("/identity/api/auth/signup")
                        .contentType(MediaType.APPLICATION_JSON)
         
```

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

This lesson ties its explanation to `src/test/java/io/foundev/crapi/TokenServiceTest.java`, `src/test/java/io/foundev/crapi/VulnerabilityScenarioTest.java`, `src/main/java/io/foundev/crapi/security/TokenService.java`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
