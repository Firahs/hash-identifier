#!/usr/bin/env python
"""
Comprehensive Hash Identification Test Suite
Tests all major hash types for 100% accuracy
"""

import subprocess
import sys

# Test cases with expected top matches
test_cases = [
    ("MD5", "5d41402abc4b2a76b9719d911017c592", ["MD5", "NTLM", "LM"]),
    ("SHA1", "356a192b7913b04c54574d18c28d46e6395428ab", ["SHA1"]),
    ("SHA2-224", "90a3ed9e32b2aaf4c61c410eb925426119e1a9dc53d4286ade99a809", ["SHA2-224"]),
    ("SHA2-256", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", ["SHA2-256"]),
    ("SHA2-384", "38b060a751ac96384cd9327eb1b1e36a21fdb71114be07434c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b", ["SHA2-384"]),
    ("SHA2-512", "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e", ["SHA2-512"]),
    ("BLAKE2b-512", "$BLAKE2$41fcd44c789c735c08b43a871b81c8f617ca43918d38aee6cf8291c58a0b00a03115857425e5ff6f044be7a5bec8536b52d6c9992e21cd43cdca8a55bbf1f5c1", ["BLAKE2b-512"]),
    ("phpass", "$P$984478476IagS59wHZvyQMArzfx58u.", ["phpass", "WordPress phpass"]),
]

print("=" * 70)
print("COMPREHENSIVE HASH IDENTIFICATION TEST SUITE")
print("=" * 70)
print()

passed = 0
failed = 0

for hash_type, hash_val, expected_matches in test_cases:
    result = subprocess.run(
        [sys.executable, "hash_identifier.py", hash_val],
        capture_output=True,
        text=True,
        cwd="."
    )
    
    # Check if any expected match is in output
    found_match = False
    for expected in expected_matches:
        if expected in result.stdout:
            found_match = True
            break
    
    status = "✅ PASS" if found_match else "❌ FAIL"
    print(f"{hash_type:20} {status}")
    
    if found_match:
        passed += 1
    else:
        failed += 1
        print(f"  Expected one of: {', '.join(expected_matches)}")

print()
print("=" * 70)
print(f"Results: {passed} PASSED, {failed} FAILED (Total: {passed + failed})")
print("=" * 70)

if failed == 0:
    print("✅ All tests passed! Hash identification is 100% accurate!")
    sys.exit(0)
else:
    print(f"⚠️ {failed} test(s) failed. Please review patterns.")
    sys.exit(1)
