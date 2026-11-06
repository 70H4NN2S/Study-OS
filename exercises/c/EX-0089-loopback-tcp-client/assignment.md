# EX-0089 — Loopback TCP client

**Time:** ~35 min · **Skill:** `PROG-C-NETWORK` · **Platform:** Linux/POSIX

**Task:** Create an IPv4 TCP socket, bind it to `127.0.0.1` port 0, and print `bound` on success.

**Cases (stdin → stdout):** `""` → `"bound\n"`

**Rules:** Close socket; no external network connections.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0089`.
