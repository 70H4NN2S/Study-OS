# EX-0134 — AES-GCM authenticated encryption

**Time:** ~40 min · **Skill:** `SEC-CRYPTO-AEAD`

**Task:** Using PyCryptodome, implement `gcm_encrypt_hex(key_hex: str, nonce_hex: str, plaintext_hex: str, aad_hex: str = "") -> str` returning `ciphertext_hex:tag_hex`, and `gcm_decrypt_hex(key_hex: str, nonce_hex: str, ciphertext_hex: str, tag_hex: str, aad_hex: str = "") -> str`.

**Cases:** For all-zero AES-128 key and 12-byte nonce, 16 zero plaintext bytes produce ciphertext `0388dace60b6a392f328c2b971b2fe78` and tag `ab6e47d42cec13bdf53a67b21257bddf`.

**Rules:** Use library verification (`decrypt_and_verify`); tampering must raise `ValueError`. Fixed nonces occur only in test vectors; never reuse a nonce with the same key in real applications.

**Submit:** `exercises/security/EX-0134-aes-gcm-integrity/src/main.py` (one file). Check: `python3 tools/check_crypto.py EX-0134`.
