# C mastery learning map

**100 original tasks · 10 modules · 5 increasing bands of challenge.** This is deliberately broader than an introductory operating-systems C crash course. The exercise source material calibrates the prerequisite competencies and concepts, **not** the individual assignment wording or implementation.

## Module progression

| Module | Tasks | Main competency |
|---|---:|---|
| 1 — C tooling and numerical foundations | 01–10 | Program structure, safe I/O, types, casting, branching, flags and overflow |
| 2 — Loops, arrays and search | 11–20 | Divisibility, numeric algorithms, histograms, arrays, sorting, searching and matrix locality |
| 3 — Strings and robust parsing | 21–30 | NUL termination, bytes vs characters, safe parsing, CSV/command grammars and IPv4 input |
| 4 — Pointers, structs and undefined behavior | 31–40 | Aliasing, lifetime, typed views, tagged unions, callbacks, byte order and debugging |
| 5 — Dynamic memory and containers | 41–50 | malloc/calloc/realloc/free, failure safety, ownership, lists, queues and amortized analysis |
| 6 — Modules, Make and generic components | 51–60 | Header interfaces, preprocessor, makefiles, errno, generic callbacks, hash maps and capstone |
| 7 — Streams, formats and persistence | 61–70 | Standard C/POSIX file I/O, long lines, binary serialization, durable saves, logs and journaling |
| 8 — POSIX files, processes and IPC | 71–80 | File descriptors, EINTR, directories, fork/exec/wait, pipes, signal lifecycles and CLOEXEC |
| 9 — Synchronization, atomics and network foundations | 81–90 | Signals, shared memory, semaphores, pthreads, locks, atomics and loopback TCP |
| 10 — Advanced systems engineering | 91–100 | poll, framed protocols, arenas, slab allocation, memory mapping, journaling, thread pools, benchmarking, fuzzing and final capstone |

## Why these topics

Source-derived calibration: the TU Braunschweig 2026 operating-systems **Warmup** highlights C11, POSIX/SUSv4, gcc warning discipline, Linux tooling and C program structure; **C-Extended** treats arrays, pointers, conversions, preprocessors, C library/errno and Make; **Zeiger und Speicher** covers allocation/lifetime, heap organization and debugging. The university **exercise sheets 1/2** concern linked lists and dynamic storage management. Their course AI policy forbids AI tools in graded homework. Study OS uses **new independent challenges and contracts** and never includes university solutions or copyrighted slide scans.

Broader practice added by Study OS: robust parsers, portable binary protocols, owned APIs, Make, checked arithmetic, file descriptors, processes, signals, pipes, shared memory, threading, C11 atomics, bounded local TCP networking, alignment, memory mapping, caches, fuzzing and systems integration. These additions are independent curriculum design, **not** a claim that all appear in the lecture or exams.

## Evidence and spaced study

Every exercise has a strict 100-point rubric and an initial retrieval prompt; create `reflection.md` with an unaided prediction, code and test records, then submit exact commit SHA. Review correctness separately from mastery; only after actual evidence update `state/assessments.csv`, `state/skills.csv`, `state/reviews.csv`. Provisional example intervals are 1, 3, 7, 14, 30 days, adapt based on errors and retention. After each 10 tasks, do an **unseen mini-exam** revisiting current and earlier skills; after task 50 and task 100, perform a larger integrative assessment. Avoid rote memorization of published examples.

## Environment

- Tasks 1–60: macOS or Linux with Clang/GCC, C11, Make; use a disposable working tree.
- Tasks 61–70: C11/stdio, then POSIX file APIs where explicitly indicated.
- Tasks 71–100: Linux VM/container is recommended. Network exercises bind loopback only. No root privileges, aggressive scanning or live systems.
- `tools/check_c.py` runs optional published cases where available; **absence of cases does not mean the exercise passed**. Unpublished checks and reviewer questioning should be newly authored after the learner submits evidence.
