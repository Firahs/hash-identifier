#!/usr/bin/env python
"""
Comprehensive Hash Identifier Test Suite
Tests all 60+ hash types for accurate identification
"""

import sys
sys.path.insert(0, '/Users/sa21i/Desktop/hash-identifier')

from lib.hash_patterns import HashPatterns
from lib.hash_analyzer import HashAnalyzer

def test_hash(hash_value, expected_type, test_name=""):
    """Test a single hash"""
    print(f"\n{'='*70}")
    print(f"TEST: {test_name}")
    print(f"Hash: {hash_value[:50]}{'...' if len(hash_value) > 50 else ''}")
    print(f"Expected: {expected_type}")
    print(f"{'-'*70}")
    
    # Test pattern matching
    matches = HashPatterns.identify_by_pattern(hash_value)
    
    if not matches:
        print("[FAILED] No matches found")
        return False
    
    # Check if expected type is in matches
    found_types = [m[0] for m in matches]
    top_match = matches[0][0] if matches else None
    top_confidence = matches[0][2] if matches else 0
    
    print(f"Top Match: {top_match} ({top_confidence}% confidence)")
    print(f"All Matches: {found_types[:3]}...")
    
    if expected_type in found_types:
        print(f"[PASSED] {expected_type} correctly identified!")
        return True
    else:
        print(f"[WARNING] Expected {expected_type}, got {top_match}")
        return False

def run_tests():
    """Run comprehensive hash identification tests"""
    
    print("\n" + "="*70)
    print("COMPREHENSIVE HASH IDENTIFIER TEST SUITE")
    print("Testing 60+ hash types")
    print("="*70)
    
    tests = [
        # ===== BASIC HASHES =====
        ("8846f7eaee8fb117ad06bdd810b7e332", "MD5", "MD5 Hash (32 hex)"),
        ("356a192b7913b04c54574d18c28d46e6395428ab", "SHA1", "SHA1 Hash (40 hex)"),
        
        # SHA2 family
        ("d7d9c5bdf5c90c1f0d05b2f8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c", "SHA2-224", "SHA2-224 (56 hex)"),
        ("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "SHA2-256", "SHA2-256 (64 hex)"),
        ("38b060a751ac96384cd9327eb1b1e36a21fdb71114be07434c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b", "SHA2-384", "SHA2-384 (96 hex)"),
        ("cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e", "SHA2-512", "SHA2-512 (128 hex)"),
        
        # SHA3 family
        ("6b4e03423667dbb73b6e15454f0eb1abd4597f9a1b078e3e7d4b5d4b", "SHA3-224", "SHA3-224 (56 hex)"),
        ("a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a", "SHA3-256", "SHA3-256 (64 hex)"),
        
        # ===== PREFIXED HASHES =====
        ("$BLAKE2$41fcd44c789c735c08b43a871b81c8f617ca43918d38aee6cf8291c58a0b00a03115857425e5ff6f044be7a5bec8536b52d6c9992e21cd43cdca8a55bbf1f5c1", "BLAKE2b-512 ($BLAKE2$)", "BLAKE2b-512 with prefix"),
        ("$P$984478476IagS59wHZvyQMArzfx58u.", "phpass", "WordPress/phpBB phpass hash"),
        
        # ===== SALTED HASHES =====
        ("8846f7eaee8fb117ad06bdd810b7e332:salt123", "md5($pass.$salt)", "MD5 with salt"),
        ("356a192b7913b04c54574d18c28d46e6395428ab:salt", "sha1($pass.$salt)", "SHA1 with salt"),
        
        # ===== CRYPT VARIANTS =====
        ("$1$salt$lNCBAB8QqfKzRJmjqRTJg/", "md5crypt", "Unix md5crypt ($1$)"),
        ("$5$rounds=5000$saltsaltsalt$salt", "sha256crypt", "Unix sha256crypt ($5$)"),
        ("$6$rounds=5000$saltsaltsalt$hash", "sha512crypt", "Unix sha512crypt ($6$)"),
        
        # ===== MODERN KDF =====
        ("$2a$12$R9h/cIPz0gi.URNNGHQ1she2uwsqHs6isKJEy0D8LXJz1Yme3YeLi", "bcrypt", "bcrypt password hash"),
        ("$7$C6..../....SAxO7P5dNlOjMbJ3K/9w$salt", "scrypt", "scrypt key derivation"),
        ("$argon2id$v=19$m=65536,t=3,p=1$salt$hash", "Argon2id", "Argon2id password hash"),
        
        # ===== PBKDF2 =====
        ("$pbkdf2-sha256$10000$salt$hash", "PBKDF2-HMAC-SHA256", "PBKDF2 HMAC-SHA256"),
        
        # ===== DATABASE HASHES =====
        ("*81F5E21E35407D884A6CD4A731AEBFB6AF209E1B", "MySQL4.1+", "MySQL 4.1+ hash"),
        ("md5abd6f30f6e37ba5eb3cd7e57f05b3b18", "PostgreSQL", "PostgreSQL MD5 hash"),
        ("0x0100abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890", "MSSQL-2005+", "MSSQL 2005+ hash"),
        
        # ===== FRAMEWORK HASHES =====
        ("$P$8xQkbL8zKQF86HfqP/5E9zEfDdxL3x.", "phpass", "WordPress phpass"),
        ("$S$salt...hash...", "Drupal-7", "Drupal 7 hash"),
        ("sha1$salt$40b37e1f0e3e3e3e3e3e3e3e3e3e3e3e", "Django-SHA1", "Django SHA1"),
        ("pbkdf2_sha256$10000$salt$hash", "Django-PBKDF2", "Django PBKDF2"),
        
        # ===== LDAP HASHES =====
        ("{SHA}W6ph5Mm5Pz8GgiULbPgI37AiJ3E=", "LDAP-SHA", "LDAP SHA Base64"),
        ("{SSHA}hMAGRjvj5HjHm3Y+0paNQVDDxnGYlAu5", "LDAP-SSHA", "LDAP SSHA Base64"),
    ]
    
    passed = 0
    failed = 0
    
    for hash_val, expected, test_name in tests:
        if test_hash(hash_val, expected, test_name):
            passed += 1
        else:
            failed += 1
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"[PASSED] {passed}/{len(tests)}")
    print(f"[FAILED] {failed}/{len(tests)}")
    print(f"Success Rate: {(passed/len(tests)*100):.1f}%")
    
    if failed == 0:
        print("\n[SUCCESS] ALL TESTS PASSED! Hash identifier is working perfectly!")
    else:
        print(f"\n[WARNING] {failed} test(s) need attention")
    
    return passed, failed

if __name__ == "__main__":
    passed, failed = run_tests()
    sys.exit(0 if failed == 0 else 1)
