# EX-0046 — Deep-copy directory

- **Track:** C mastery · module 5/10 · 46/100
- **Target skills:** PROG-C-HEAP
- **Difficulty / estimated time:** 6/10 · 75–150 minutes
- **Prerequisites:** functions, pointers, arrays, and at least one preceding heap/struct practice exercise.
- **Prior connections:** Reuse parsing from stage 2 and document any ownership model involved.

## Active recall before coding
Answer from memory, then verify from documentation: **Contrast shallow copies of structs with deep ownership copies.** Record first and revised explanations in `reflection.md`.

## Assignment
Implement `struct contact` with heap-owned name and dynamically allocated tags; support `clone_contact`, `free_contact`, and failure-safe initialization.

**Contract / example:** Modifying a clone's name or tag must not modify the original; cloning an empty tag array succeeds; no leaks after failure injection.

**Adversarial focus:** On partial clone failure, free only objects actually initialized.

## Setup
Create the library/CLI files demanded by this exercise in its own folder. Use `src/main.c`, `src/*.c`, and `include/*.h` for multi-file work (adjust from this convention only where the task explicitly prescribes another layout). Provide a build command or `Makefile` that compiles under C11:

```sh
cc -std=c11 -pedantic -D_XOPEN_SOURCE=700 -Wall -Wextra -Werror -g -Iinclude -o app src/*.c
```

The command assumes `src/*.c` exists; for tasks with a different structure, write down the exact equivalent. On bad CLI input return exit 2 with stderr diagnostics; library APIs must use documented status codes and leave outputs in a defined state. Prefer no global mutable state. Tests may call the functions directly; do not rely solely on output inspection.

## Deliverables
Source and public headers; `tests.md` containing 6 independent cases (including allocation failure/empty/full where applicable), `reflection.md`, and a reproducible build recipe. For heap-managing tasks include an **ownership table** identifying who allocates/frees each object. Submit a commit SHA or PR for review.

## Allowed help
Notes/manuals/public references: yes. AI: tier 1 nudge, tier 2 concept, tier 3 pseudocode after documented struggle, tier 4 solution only upon explicit post-attempt request. Disclose assistance. This is independent, original practice, not an authorized use of AI in university-graded submissions.

## Acceptance criteria
- Functions and CLI follow the contract including the given example, invalid input, and boundary cases.
- Every dynamic object has clear ownership; allocation failure preserves invariants and never loses an allocation.
- Warning-free C11 build, defined failure behavior, deterministic cleanup and no detected sanitizer violations when tested.
- Direct API tests cover operations in unusual orders, not just the happy path.
- Explain complexity, pointer lifetime, and one alternative design with a tradeoff.

## Rubric — 100 points
- Correct feature contract: **50**
- Edge cases, failures, ownership and safety: **25**
- Modular design, tests and reproducibility: **15**
- Independent retrieval, explanation and reflection: **10**

## Verification
Compile exact submission revision, run manual/API cases, inspect ownership and error paths; when supported run AddressSanitizer, UndefinedBehaviorSanitizer and a leak checker. A clean sanitizer run does not establish full correctness. Mastery is updated **only after assessment**, not by this PR.

## Delayed interleaving
At review time schedule a variant that combines this technique with an earlier topic (arrays, parsing or pointer ownership) 3, 7 or 14 days later, depending on actual evidence.
