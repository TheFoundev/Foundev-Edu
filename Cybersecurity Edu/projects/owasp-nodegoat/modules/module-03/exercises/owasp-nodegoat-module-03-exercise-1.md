# Exercise: Trace test code and implementation evidence

**Exercise ID:** `owasp-nodegoat-module-03-exercise-1`

- **Objective:** Explain a concrete code/configuration path in `test/app.test.js`, `test/hardened.test.js`, `src/app.js`.
- **Problem:** Starting from one declaration or setting in the listed files, trace its caller, input, output, or test evidence through the repository.
- **Requirements:** Cite at least two exact paths; describe the code operation in your own words; identify one boundary or failure case; state what remains unverified; propose one targeted test or review step.
- **Constraints:** Do not claim tests ran; do not use private data or credentials; do not edit the upstream source for this exercise.
- **Expected behavior:** A concise, source-linked trace and a reproducible verification plan.
- **Acceptance criteria:** Each claim has a source location; at least one caller/test/config link is traced; no inferred behavior is stated as fact; the proposed check addresses the named boundary.
- **Hints:** Search for imports, calls, and references to names declared in the anchor files. Check fixtures and mocks for their limits.
- **Difficulty:** Intermediate
- **Estimated time:** 45–60 minutes
