# EX-0061 — File line counter

- **Track:** C mastery · module 7/10 · 61/100
- **Target skills:** PROG-C-FILES
- **Difficulty / estimated time:** 7/10 · 90–180 minutes
- **Prerequisites:** stage 3 memory ownership + error handling; familiarity with Linux command line recommended.
- **Environment:** C11 and standard/POSIX file I/O; macOS or Linux, Linux recommended for parity.
- **Connections:** Combine input parsing, owned buffers, errno handling and data structures from previous stages.

## Retrieval challenge
Before coding: **Explain `fgetc` return type and why it is `int`.** In `reflection.md`, write an independent prediction, identify assumptions, and correct it after experimenting.

## Assignment
Create `linecount FILE` using standard C streams; report physical newline count and logical line count (last unterminated line still counts). Read in bounded chunks.

**Expected behavior:** For bytes `a\nb\n`, print `newlines=2 lines=2`; for `a\nb`, print `newlines=1 lines=2`; empty file reports both 0.

**Failure model / pitfall:** Differentiate EOF from `ferror`; include binary data with NUL.

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
