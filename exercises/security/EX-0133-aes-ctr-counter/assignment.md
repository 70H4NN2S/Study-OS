# EX-0133 — AES-CTR counter-mode experiment

**Time:** ~30 min · **Skill:** `SEC-CRYPTO-BLOCK`

**Task:** Using PyCryptodome, implement `encrypt_ctr_hex(key_hex: str, nonce_hex: str, plaintext_hex: str) -> str`. Use an 8-byte nonce, a big-endian counter initialized to zero, and AES-128.

**Cases:** With all-zero key, all-zero nonce and an all-zero 16-byte plaintext, ciphertext is `66e94bd4ef8a2c3b884cfa59ca342b2e`.

**Rules:** Arbitrary plaintext lengths are allowed. Never reuse a key/nonce pair. Explain why CTR acts like a stream cipher.

**Submit:** `exercises/security/EX-0133-aes-ctr-counter/src/main.py` (one file). Check: `python3 tools/check_crypto.py EX-0133`.
