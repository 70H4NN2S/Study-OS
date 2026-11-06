# EX-0008 — Checked addition

- **Track:** Progressive C mastery · stage 1/10 (fundamentals) · exercise 8/100
- **Target skills:** PROG-C-TYPES
- **Difficulty / estimated time:** 2/10 · 20–45 minutes
- **Prerequisites:** EX-0007 recommended; do not require perfect completion
- **Prior connections:** Reuse input validation, control flow and correct numerical reasoning from earlier exercises.

## Retrieval before coding (3–5 minutes)
Without opening notes, answer: **Describe why a cast after an overflowing addition cannot repair UB.** Save your prediction in `reflection.md`; revise it after testing.

## Assignment
Read two signed 32-bit integers and print their sum if representable, otherwise print `overflow` and exit 1. Do not invoke signed-overflow UB.

**Observable contract:** Input `2147483647 1` -> `overflow`; `-5 2` -> `-3`. Malformed input -> exit 2.

**Pitfall to address:** Check bounds before computing or widen to a safely larger type.

## Setup and starter files
Create `src/main.c` yourself under this exercise directory. No implementation or solution is supplied. Compile with:

```sh
gcc -std=c11 -pedantic -D_XOPEN_SOURCE=700 -Wall -Wextra -Werror -g -o app src/main.c
```

Use standard input and standard output unless specified above; no interactive prompts. Extra trailing non-whitespace input is invalid unless the task explicitly defines a command stream. On malformed input print a short explanation to stderr, exit 2, and do not print a misleading success result. A valid run exits 0 unless stated otherwise.

## Deliverables
Commit `src/main.c`, `tests.md` (at least 4 manually run cases with expected and actual output), and `reflection.md` (pre-code prediction, failures, assumptions, and explanation). Submit a Study OS PR or exact commit SHA; **never** put your solution into the university GitLab exercise repository.

## Allowed help
Personal notes and public C/POSIX documentation: **yes**. Internet: **yes, for documentation**. AI: tiers 1–2 allowed after a genuine independent attempt; tier 3 only after recording the blocker; tier 4 only after you request a post-attempt walkthrough. Record the highest tier used; do not paste generated code without understanding it. This is a **separate original practice exercise**, not a TU Braunschweig graded task.

## Acceptance criteria
- The behavioral contract and the named example/edge cases hold exactly.
- Reject malformed input; prevent out-of-bounds accesses, integer overflow and undefined behavior.
- Clean C11 compilation with the flags above and no unnecessary global state.
- Explain your algorithm and give its time/space complexity when relevant.
- `tests.md` covers ordinary, boundary, invalid and adversarial input.

## Rubric (100 points)
- Correct output and specification: **50**
- Boundary cases, safety, and explanation of check bounds before computing or widen to a safely larger type: **25**
- Readability, compilation, reproducible tests: **15**
- Independent oral/written explanation and reflection: **10**

## Verification
Reviewer compiles the exact submitted commit, runs user tests and independent boundary/invalid cases, inspects source for UB, and asks one transfer question. No automatic passing status is implied by this assignment. Use sanitizers where available. Record score and mastery separately **after** evidence review.

## Delayed transfer
Within 3–7 days, solve one related problem with different inputs/constraints without re-reading this implementation; schedule only after assessment.
