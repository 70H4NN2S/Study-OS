# Run a C exercise

1. Write the source in `exercises/c/EX-xxxx-.../src/main.c`.
2. From the repo root: `python3 tools/check_c.py EX-0001` (change the ID).
3. Commit and send the exact SHA/PR for review.

The checker compiles with C11 warnings and runs 1–3 **public exact stdin/stdout examples for all 100 exercises**, including exit status. Some tasks explicitly require additional sources, headers or a Makefile. Linux is recommended for POSIX, pthread and mmap tasks (#71–100).

**Passing public tests is not a grade.** Independent cases, cleanup, robustness and understanding are assessed on your submitted code. No mandatory test report or reflection file.
