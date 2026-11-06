# EX-0090 — Single-client TCP echo server

**Time:** ~55 min · **Skill:** `PROG-C-NETWORK` · **Platform:** Linux/POSIX

**Task:** Bind/listen on loopback ephemeral TCP port, fork a client that sends `hi`, accept it, echo two bytes, and print received echo from client.

**Cases (stdin → stdout):** `""` → `"hi\n"`

**Rules:** Use `getsockname` to discover chosen port; close sockets and reap child.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0090`.
