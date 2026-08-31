---
name: code-review
description: "Use when reviewing pull requests or performing a manual local code review. Applies to changed source code and related tests, and requires findings to include severity, file and line, issue, impact, and recommended action."
---

# Code Review

Use this skill to perform code reviews in two modes.

## Repository/Server Reviewer

Use this mode for newly created or updated pull requests.

- Review only changed source code and related tests.
- Focus on actionable findings.
- Check for correctness and functional defects, security vulnerabilities, edge cases, performance issues, maintainability, test coverage, out-of-scope changes, and requirement or acceptance-criteria compliance when context is available.

## Local VS Code Reviewer

Use this mode when a developer manually invokes a review during implementation.

- Review source code and tests with full local context.
- Validate the implementation against requirements and acceptance criteria when they are available.
- Surface issues that would block merge or warrant follow-up, even if the change is still in progress.

## Finding Format

Every finding must include:

- Severity
- File and line reference
- Issue
- Impact
- Recommended action

## Review Rules

- Do not change source code as part of the review.
- Do not create correction commits.
- Do not push fixes.
- Prefer concrete, falsifiable findings over broad commentary.
- Do not report unrelated problems unless they are directly relevant to the review scope.
- If no issues are found, say so explicitly and mention any remaining risks or coverage gaps.
