# EX-0092 — Streaming framed-message parser

**Time:** ~40 min · **Skill:** `PROG-C-SECURITY` · **Platform:** Linux/POSIX

**Task:** Read stdin: one ASCII digit `0`..`5` specifying payload byte count, then that many bytes; print the payload or `short` if truncated.

**Cases (stdin → stdout):** `"3cat"` → `"cat\n"` · `"4hi"` → `"short\n"` · `"0"` → `"\n"`

**Rules:** Do not assume one `fread` gets a full frame; cap at 5 bytes.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0092`.
