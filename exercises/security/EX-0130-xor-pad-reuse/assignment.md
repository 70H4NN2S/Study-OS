# EX-0130 — XOR and the reused-pad failure

**Time:** ~20 min · **Skill:** `SEC-CRYPTO-XOR`

**Task:** Implement `xor_hex(message_hex: str, key_hex: str) -> str` and `recover_second_hex(c1_hex: str, c2_hex: str, known_m1_hex: str) -> str`. Inputs and results are lowercase hexadecimal byte strings.

**Cases:** `xor_hex("4142","0102")` → `"4040"`; `recover_second_hex("4040","4246","4142")` → `"4344"`.

**Rules:** Require equal byte lengths; raise `ValueError` otherwise. This demonstrates an insecure reused pad; do not use it to protect data.

**Submit:** `exercises/security/EX-0130-xor-pad-reuse/src/main.py` (one file). Check: `python3 tools/check_crypto.py EX-0130`.
