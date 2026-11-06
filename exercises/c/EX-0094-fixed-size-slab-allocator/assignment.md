# EX-0094 — Fixed-size slab allocator

- **Track:** C mastery · module 10/10 · 94/100
- **Target skills:** PROG-C-MEMORY-MODEL
- **Difficulty / estimated time:** 9/10 · 3–8 hours
- **Prerequisites:** stages 1–4; Linux VM strongly recommended (Debian/Ubuntu), C11, Make, POSIX APIs, debugger/sanitizers.
- **Prior connections:** Design and explain interactions among memory ownership, input handling, process/thread lifecycle and failure semantics.

## Independent retrieval and design
Before reading documentation: **Contrast fragmentation in slabs with variable-size allocation.** Draw a dataflow/ownership diagram and write a brief test-first outline. Capture your initial hypothesis and revisions in `reflection.md`.

## Assignment
Implement a pool of 128 same-sized records backed by one aligned block and an internal free-index stack. Allocate/free by pool handle with explicit validity checks.

**Observable contract:** All 128 slots allocate, 129th fails; freeing one slot makes it reusable; invalid slot and double-free are detected without UB.

**Reliability and security requirement:** Do not read arbitrary caller pointers before verifying they belong to the pool.

## Setup
Use a self-contained directory with `include/`, `src/`, `tests/` and a `Makefile`. Work **only on loopback/local disposable data**; no elevated privileges. Compiler baseline:

```sh
cc -std=c11 -pedantic -D_XOPEN_SOURCE=700 -Wall -Wextra -Werror -g -O1 -pthread -Iinclude -o app src/*.c
```

Use `-latomic` only if your particular toolchain requires it; record toolchain/platform in `README.md`. For networking tests use ephemeral/unprivileged local ports and hard connection timeouts. Explicitly document status codes and concurrency assumptions. Start with a minimal vertical slice, then incrementally add features with tests.

## Deliverables
Source, `Makefile` with `all/test/clean`, a design `README.md` (API, invariants, ownership, failures), executable or reproducible `tests/` scenarios, `reflection.md`, and test evidence at an exact commit. Minimum eight scenarios: normal, empty, invalid, boundary, failure, repeat/restart, stress and interleaving. For the capstone provide a protocol spec and a demonstration transcript.

## Allowed help
Independent first attempt; documentation and man pages permitted. AI tier 1 nudge or tier 2 concept after your design; tier 3 scaffolding only for a documented blocker; tier 4 worked solution only on explicit post-attempt request. Log help actually used. This curriculum is separate from the university assignments, whose AI-use restrictions must be respected.

## Acceptance criteria
- Behaviors and measurable cases above hold in a controlled Linux environment.
- Every allocation, descriptor, process, thread and synchronization primitive has documented lifecycle and cleanup.
- No unbounded memory growth, uncontrolled external interface, UB, data race or deadlock in designed normal cases.
- Negative/error paths have repeatable tests; no claims of determinism for nondeterministic scheduling.
- Warning-free C11 compile; sanitizer/runtime diagnostics where supported (ThreadSanitizer may not work in every environment).
- Explain performance, portability and reliability limitations without claiming formal proof.

## Rubric — 100 points
- Functional behavior and integration: **50**
- Edge conditions, safety, failure and concurrency invariants: **25**
- Architecture, reproducibility and test quality: **15**
- Independent oral explanation and reflection: **10**

## Verification
Review exact commit, compile/run in an isolated Linux environment, inspect static error paths, test independent invalid/concurrent requests and memory/FD/thread lifetimes, use sanitizers and stress scripts when supported. Record observed failures and limitations. Do **not** mark mastery or pass status before real submission.

## Delayed transfer
After assessment, revisit a smaller but structurally novel variant in 7–30 days; use evidence to schedule topics that were weak rather than mechanically repeating solved steps.
