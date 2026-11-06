# EX-0081 — Async-signal-safe shutdown

**Time:** ~20 min · **Skill:** `PROG-C-SIGNALS` · **Platform:** Linux/POSIX

**Task:** Install a `sigaction` handler for SIGUSR1 that only sets a `volatile sig_atomic_t` flag; call `raise(SIGUSR1)` and print `stopped` if flag set.

**Cases (stdin → stdout):** `""` → `"stopped\n"`

**Rules:** Do not print or allocate in handler.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0081`.
