# EX-0073 — Directory snapshot

- **Track:** C mastery · stage 4/10 files, process API and POSIX systems programming · 73/100
- **Target skills:** PROG-C-POSIX-FS
- **Difficulty / estimated time:** 8/10 · 120–240 minutes
- **Prerequisites:** stage 3 memory ownership + error handling; familiarity with Linux command line recommended.
- **Environment:** Linux (Debian VM recommended); SUSv4/POSIX.1-2008 APIs; some tests may behave differently on macOS.
- **Connections:** Combine input parsing, owned buffers, errno handling and data structures from previous stages.

## Retrieval challenge
Before coding: **Why distinguish `lstat` from `stat`?** In `reflection.md`, write an independent prediction, identify assumptions, and correct it after experimenting.

## Assignment
Implement `listdir PATH` using `opendir`, `readdir`, and `lstat`; print each entry type, name and size, sorted by raw byte name.

**Expected behavior:** A directory with two files and one symlink shows all entries excluding `.` and `..`; dangling symlink is listed as link, not dereferenced.

**Failure model / pitfall:** Do not assume `readdir` returns sorted order; avoid arbitrary path-length assumptions.

## Setup
Create `src/*.c` and any `include/*.h` needed. Add a `Makefile` with `all`, `test`, `clean`; build with `-std=c11 -pedantic -D_XOPEN_SOURCE=700 -Wall -Wextra -Werror`. Do not use GNU-only extensions unless the task explicitly marks them as optional; only use binaries/paths under your own temporary test directory. Include a `FORMAT.md` for binary protocols or files when indicated. No solution is supplied.

## Deliverables
Commit sources, tests or reproducible `tests.md` (>=6 scenarios), `reflection.md` (predictions, findings, help level), a working `Makefile`, and any format/API documentation. Submit exact commit SHA/PR to Study OS. Do **not** reuse code as a university-graded submission where AI use is prohibited.

## Allowed help
Notes, local man pages and internet documentation are allowed. AI hint tier 1 after independent attempt; tier 2 conceptual; tier 3 scaffold/pseudocode after recording blocker; tier 4 full solution only upon explicit post-attempt request. Disclose actual assistance. For process/file experiments use only your own disposable test files and programs.

## Acceptance criteria
- Meet the behavior in the contract, including empty/truncated/invalid inputs.
- Check error returns and preserve meaningful `errno` at failure sites.
- No descriptor leaks, invalid heap accesses or unreaped children (as relevant).
- Preserve binary content exactly and document format, encoding, ordering and exit statuses.
- Show >=6 reproducible tests, including failure injection or concurrency scheduling where relevant.
- Explain correctness, complexity and one tradeoff or race condition relevant to the interface.

## Rubric (100 points)
- Contract and observable results: **50**
- Edge cases, safety and precise error handling: **25**
- Build quality, tests and reproducibility: **15**
- Independent conceptual explanation: **10**

## Verification
Reviewer inspects the exact commit, builds on a POSIX-compatible environment, runs supplied and novel cases, looks for leaks, missing EINTR loops and lifecycle errors. External command behavior must be checked in a controlled test folder. Never claim CI or sanitizer success until it has run.

## Follow-up
After assessment, interleave a related parser/heap challenge and schedule delayed transfer based on actual weak skills, not automatic completion counts.
