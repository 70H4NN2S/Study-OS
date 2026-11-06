# EX-0052 — Make rebuild rules

- **Track:** C mastery · stage 3/10 manual memory, data structures, modular builds · 52/100
- **Target skills:** PROG-C-TOOLCHAIN
- **Difficulty / estimated time:** 6/10 · 75–150 minutes
- **Prerequisites:** functions, pointers, arrays, and at least one preceding heap/struct practice exercise.
- **Prior connections:** Reuse parsing from stage 2 and document any ownership model involved.

## Active recall before coding
Answer from memory, then verify from documentation: **Why are `.o` files useful and why do stale dependencies cause bugs?** Record first and revised explanations in `reflection.md`.

## Assignment
Create a `Makefile` with targets `all`, `clean`, `test`, object files and automatic header dependencies for the library from exercise 51.

**Contract / example:** Editing `queue.h` rebuilds affected `.o` files; running `make` twice without changes does no compilation; `make clean` removes generated objects.

**Adversarial focus:** Declare `.PHONY`; preserve C11/pedantic/warning flags.

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
