# EX-0029 — IPv4 text validator

- **Track:** C mastery · module 3/10 · 29/100
- **Target skills:** PROG-C-STRINGS
- **Difficulty / estimated time:** 4/10 · 40–85 minutes
- **Prerequisites:** C arrays, functions, basic input validation; earlier stages recommended. 
- **Prior connections:** Reuse earlier input handling and safety rules; explain how this task generalizes one earlier exercise.

## Independent retrieval
Before coding answer without assistance: **Explain why an IPv4 address is not four C strings.** Put the initial answer and final corrected explanation in `reflection.md`.

## Assignment
Implement `int parse_ipv4(const char *text, unsigned char bytes[4])` for four base-10 decimal octets with dots and no leading zeros except the digit `0`. CLI prints normalized dotted decimal.

**Observable contract:** `192.168.1.10` is valid; `256.1.2.3`, `01.2.3.4`, and `1.2.3` are invalid.

**Safety constraint:** Reject empty components and avoid overflow while accumulating digits.

## Setup
Create `src/main.c` and, if appropriate, `src/module.c` / `src/module.h` under this exercise directory. Keep interfaces described in the specification. Compilation for ordinary implementations:

```sh
gcc -std=c11 -pedantic -D_XOPEN_SOURCE=700 -Wall -Wextra -Werror -g -o app src/*.c
```

Use stdin/stdout with no prompts, exit 0 on success, exit 2 on malformed input, and stderr for diagnostics (unless a different exit status is prescribed). Any numeric length or token limit is a hard bound.

## Deliverables
Commit source, `tests.md` (at least 5 cases: nominal, boundary, malformed, adversarial, reuse of a previous concept), and `reflection.md`. Include diagrams or debugger notes when useful. Submit an exact commit SHA or Study OS PR; keep solutions away from the course GitLab submissions.

## Allowed help
Personal notes and standard C/POSIX documentation allowed. AI hints: tier 1 nudge after an independent attempt; tier 2 conceptual help; tier 3 pseudocode only after documenting a blocker; tier 4 full solution only after an attempt and explicit request. Disclose assistance actually used. This task is original independent practice, not a university graded homework answer.

## Acceptance criteria
- Meet the precise example and edge cases; reject malformed inputs without corrupting memory or lying about success.
- Avoid undefined behavior, unbounded string processing and unjustified ownership transfers.
- Compile warning-free under the command above; run address/undefined-behavior sanitizers when relevant and available.
- Prove or explain interface semantics, ownership/lifetime, complexity and security implications where applicable.
- Document at least five reproducible tests with expected and observed outcomes.

## Rubric (100 points)
- Specification and output: **50**
- Robustness, memory safety and reasoning: **25**
- Design, source quality and repeatable tests: **15**
- Independent explanation and self-review: **10**

## Verification
Reviewer compiles the submitted revision, compares observed output with contract and new adversarial cases, inspects unsafe paths and checks submitted reasoning. Sanitizers are diagnostic aids, not proof of correctness. No tests have been claimed to pass before learner submission.

## Spaced transfer
After grading, revisit a variant 3–7 days later without consulting this code. Focus on whichever bug class or concept the review identifies.
