# Public C checks

Use `python3 tools/check_c.py EX-0001` after writing a learner solution in `exercises/c/EX-0001-.../src/*.c`. The checker compiles under strict C11 flags and runs published examples from `tests/public_cases.json` where present. The rest require manual test plans and later independent review. **Public examples are a smoke test, never a grade, a proof of memory safety, or evidence of mastery.**

Add new executable public cases to each task only when the CLI/API contract is unambiguous; do not commit answer keys. Reviewer-created independent cases should be developed after a real submission, with the student's permission if hidden materials are involved. Advanced POSIX/threading tasks require Linux and potentially a task-specific harness.
