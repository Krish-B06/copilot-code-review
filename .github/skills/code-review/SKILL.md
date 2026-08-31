---
name: code-review
description: Perform a structured code review focusing on correctness, security, maintainability, testing, and requirements.
---

# Code Review Skill

Review the proposed code changes systematically.

## Review areas

1. Correctness
   - Identify bugs, incorrect logic, and edge cases.
   - Verify that the implementation behaves as intended.

2. Security
   - Identify potential security vulnerabilities.
   - Check unsafe handling of inputs, data, and sensitive information.

3. Maintainability
   - Check code structure, readability, duplication, and complexity.

4. Testing
   - Check whether new or modified behavior is adequately tested.
   - Identify important missing test cases.

5. Requirements
   - When requirement or acceptance-criteria information is available,
     compare the implementation against it.
   - Report unmet or partially implemented requirements separately.

## Review principles

- Focus on actionable findings.
- Prioritize correctness and security issues.
- Explain why each finding matters.
- Avoid purely stylistic comments unless they affect maintainability.
- Do not report issues unrelated to the changed code.
