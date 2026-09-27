---
name: commit-msg
description: Generate a conventional-commit message from staged changes and commit them. Use when the user says "write a commit message", "generate a commit", "commit my changes", or runs /commit-msg.
---

# commit-msg

Generate a Conventional Commits message from the staged diff and create the commit.

## Workflow

1. **Check for staged changes.** Run `git diff --staged --stat` (or `git diff --staged`). If there is no staged output, **stop** and tell the user: "Nothing is staged. Stage your changes first (e.g. `git add <files>`), then ask again." Do not stage anything yourself and do not commit.

2. **Read the staged diff.** Run `git diff --staged` and read it in full to understand what changed and why.

3. **Generate a commit message** in exactly this format:

   ```
   type(scope): short subject

   - bullet of what changed
   - bullet of why
   ```

   Rules:
   - `type` is one of: `feat`, `fix`, `refactor`, `chore`, `docs`, `style`, `test`.
   - `scope` is a short area name (a module, file, or feature). If no meaningful scope applies, omit it and the parentheses: `type: short subject`.
   - Subject line **under 60 characters**, imperative mood, no trailing period.
   - Body bullets are optional but encouraged: describe *what* changed and *why*. Skip the blank line and body if a single-line message is clearly sufficient.
   - **Never** include a `Co-Authored-By` trailer or any other attribution trailer.

4. **Commit.** Run `git commit` with the generated message. On Windows PowerShell, pass a multi-line message with a single-quoted here-string so `$` and backticks stay literal:

   ```
   git commit -m @'
   type(scope): short subject

   - bullet of what changed
   - bullet of why
   '@
   ```

   After committing, show the resulting commit (`git log -1 --stat`) so the user can confirm.

## Type selection guide

- `feat` — a new feature or capability
- `fix` — a bug fix
- `refactor` — code change that neither fixes a bug nor adds a feature
- `chore` — tooling, config, deps, or housekeeping
- `docs` — documentation only
- `style` — formatting, whitespace, no logic change
- `test` — adding or updating tests
