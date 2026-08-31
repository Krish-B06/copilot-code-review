# Copilot Instructions

When asked to review code in this repository, follow the code-review workflow described in `.github/skills/code-review/SKILL.md`.

Use two reviewer modes:

1. Repository/Server Reviewer
   - Automatically reviews newly created and updated pull requests.
   - Reviews changed source code and related tests only.
   - Focuses on actionable findings that affect correctness, security, edge cases, performance, maintainability, test coverage, out-of-scope changes, and requirement or acceptance-criteria compliance when available.

2. Local VS Code Reviewer
   - Is manually invoked by developers during development.
   - Provides a comprehensive, context-sensitive review.
   - Reviews source code and tests.
   - Validates implementation against requirements and acceptance criteria when present in the request or nearby context.

Review findings must include all of the following:

- Severity
- File and line reference
- Issue
- Impact
- Recommended action

Behavior constraints:

- Do not modify source code automatically.
- Do not create correction commits.
- Do not push fixes.
- Prefer findings that are specific, actionable, and tied to a concrete code location.
- Ignore unrelated files unless they are directly relevant to the review request or the changed behavior.
- If there are no findings, state that clearly and mention any residual risks or testing gaps.
