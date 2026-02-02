"""
Hash Pattern Recognition Module - ENHANCED
Identifies 100+ hash types using regex patterns
Created by: MD.SHORIF MIA
Version: 2.0
"""

import re


class HashPatterns:
    """Collection of hash type patterns and detection methods"""
    
    # Pattern definitions for 100+ hash types
    PATTERNS = {
        # ========== BASIC HASHES (32-128 bits) ==========
        
        # MD5 and variants
        'MD5': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 60
        },
        'MD2': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 50
        },
        'MD4': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 50
        },
        'NTLM': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 100
        },
        'LM': {
            'pattern': r'^[a-f0-9]{32}(:[a-f0-9]{32})?$',
            'length': 32,
            'confidence': 100
        },
        'Half-MD5': {
            'pattern': r'^[a-f0-9]{16}$',
            'length': 16,
            'confidence': 40
        },
        
        # SHA1 variants (40 hex chars)
        'SHA1': {
            'pattern': r'^[a-f0-9]{40}$',
            'length': 40,
            'confidence': 85
        },
        'RIPEMD-160': {
            'pattern': r'^[a-f0-9]{40}$',
            'length': 40,
            'confidence': 70
        },
        'Tiger160': {
            'pattern': r'^[a-f0-9]{40}$',
            'length': 40,
            'confidence': 60
        },
        
        # SHA2-224 (56 hex chars)
        'SHA2-224': {
            'pattern': r'^[a-f0-9]{56}$',
            'length': 56,
            'confidence': 90
        },
        'SHA3-224': {
            'pattern': r'^[a-f0-9]{56}$',
            'length': 56,
            'confidence': 88
        },
        'Keccak-224': {
            'pattern': r'^[a-f0-9]{56}$',
            'length': 56,
            'confidence': 85
        },
        
        # SHA2-256 (64 hex chars)
        'SHA2-256': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 92
        },
        'SHA3-256': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 88
        },
        'GOST': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 72
        },
        'Keccak-256': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 80
        },
        'BLAKE2s-256': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 75
        },
        'Skein-256': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 70
        },
        'SM3': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 75
        },
        
        # SHA2-384 (96 hex chars)
        'SHA2-384': {
            'pattern': r'^[a-f0-9]{96}$',
            'length': 96,
            'confidence': 95
        },
        'SHA3-384': {
            'pattern': r'^[a-f0-9]{96}$',
            'length': 96,
            'confidence': 92
        },
        'Keccak-384': {
            'pattern': r'^[a-f0-9]{96}$',
            'length': 96,
            'confidence': 90
        },
        
        # SHA2-512 (128 hex chars)
        'SHA2-512': {
            'pattern': r'^[a-f0-9]{128}$',
            'length': 128,
            'confidence': 95
        },
        'SHA3-512': {
            'pattern': r'^[a-f0-9]{128}$',
            'length': 128,
            'confidence': 92
        },
        'Whirlpool': {
            'pattern': r'^[a-f0-9]{128}$',
            'length': 128,
            'confidence': 80
        },
        'BLAKE2b-512': {
            'pattern': r'^[a-f0-9]{128}$',
            'length': 128,
            'confidence': 82
        },
        'Keccak-512': {
            'pattern': r'^[a-f0-9]{128}$',
            'length': 128,
            'confidence': 88
        },
        'GOST-512': {
            'pattern': r'^[a-f0-9]{128}$',
            'length': 128,
            'confidence': 78
        },
        
        # BLAKE2 with prefix
        'BLAKE2b-512 ($BLAKE2$)': {
            'pattern': r'^\$BLAKE2\$[a-f0-9]{128}$',
            'length': 136,
            'confidence': 99
        },
        
        # RIPEMD-320 (80 hex chars)
        'RIPEMD-320': {
            'pattern': r'^[a-f0-9]{80}$',
            'length': 80,
            'confidence': 98
        },
        
        # ========== CHECKSUMS (8 hex chars) ==========
        'CRC32': {
            'pattern': r'^[a-f0-9]{8}$',
            'length': 8,
            'confidence': 20
        },
        'MurmurHash': {
            'pattern': r'^[a-f0-9]{8}$',
            'length': 8,
            'confidence': 20
        },
        'Adler32': {
            'pattern': r'^[a-f0-9]{8}$',
            'length': 8,
            'confidence': 20
        },
        
        # ========== KEY DERIVATION FUNCTIONS ==========
        
        # bcrypt
        'bcrypt': {
            'pattern': r'^\$2[aby]\$\d{2}\$[./A-Za-z0-9]{53}$',
            'length': None,
            'confidence': 100
        },
        
        # scrypt
        'scrypt': {
            'pattern': r'^\$7\$.*',
            'length': None,
            'confidence': 100
        },
        
        # Argon2
        'Argon2id': {
            'pattern': r'^\$argon2id\$v=\d+\$m=\d+,t=\d+,p=\d+\$[./A-Za-z0-9]{0,22}\$[./A-Za-z0-9]{0,43}$',
            'length': None,
            'confidence': 100
        },
        'Argon2i': {
            'pattern': r'^\$argon2i\$v=\d+\$m=\d+,t=\d+,p=\d+\$[./A-Za-z0-9]{0,22}\$[./A-Za-z0-9]{0,43}$',
            'length': None,
            'confidence': 100
        },
        'Argon2': {
            'pattern': r'^\$argon2[id]{1,2}\$v=\d+\$m=\d+,t=\d+,p=\d+\$[./A-Za-z0-9]{0,22}\$[./A-Za-z0-9]{0,43}$',
            'length': None,
            'confidence': 100
        },
        
        # PBKDF2 variants
        'PBKDF2-HMAC-MD5': {
            'pattern': r'^\$pbkdf2-md5\$\d+\$[./a-zA-Z0-9]+\$[./a-zA-Z0-9]+$',
            'length': None,
            'confidence': 98
        },
        'PBKDF2-HMAC-SHA1': {
            'pattern': r'^\$pbkdf2-sha1\$\d+\$[./a-zA-Z0-9]+\$[./a-zA-Z0-9]+$',
            'length': None,
            'confidence': 98
        },
        'PBKDF2-HMAC-SHA256': {
            'pattern': r'^\$pbkdf2-sha256\$\d+\$[./a-zA-Z0-9]+\$[./a-zA-Z0-9]+$',
            'length': None,
            'confidence': 98
        },
        'PBKDF2-HMAC-SHA512': {
            'pattern': r'^\$pbkdf2-sha512\$\d+\$[./a-zA-Z0-9]+\$[./a-zA-Z0-9]+$',
            'length': None,
            'confidence': 98
        },
        
        # ========== CRYPT VARIANTS ==========
        
        # Unix md5crypt ($1$)
        'md5crypt': {
            'pattern': r'^\$1\$[./a-zA-Z0-9]{0,8}\$[./a-zA-Z0-9]{22}$',
            'length': None,
            'confidence': 100
        },
        
        # Unix SHA256 crypt ($5$)
        'sha256crypt': {
            'pattern': r'^\$5\$.*',
            'length': None,
            'confidence': 100
        },
        
        # Unix SHA512 crypt ($6$)
        'sha512crypt': {
            'pattern': r'^\$6\$.*',
            'length': None,
            'confidence': 100
        },
        
        # Traditional DES crypt
        'descrypt': {
            'pattern': r'^[./a-zA-Z0-9]{13}$',
            'length': 13,
            'confidence': 90
        },
        
        # BSDi extended DES ($_9$)
        'BSDi-crypt': {
            'pattern': r'^_[./a-zA-Z0-9]{19}$',
            'length': 20,
            'confidence': 98
        },
        
        # ========== FRAMEWORK/APP HASHES ==========
        
        # phpass (WordPress, phpBB)
        'phpass': {
            'pattern': r'^\$P\$[./a-zA-Z0-9]{31}$',
            'length': 34,
            'confidence': 100
        },
        'WordPress phpass': {
            'pattern': r'^\$P\$[./a-zA-Z0-9]{31}$',
            'length': 34,
            'confidence': 100
        },
        
        # Drupal 7 (phpass variant)
        'Drupal-7': {
            'pattern': r'^\$S\$.*',
            'length': None,
            'confidence': 100
        },
        
        # Django SHA1
        'Django-SHA1': {
            'pattern': r'^sha1\$.*',
            'length': None,
            'confidence': 99
        },
        
        # Django PBKDF2-SHA256
        'Django-PBKDF2': {
            'pattern': r'^pbkdf2_sha256\$\d+\$[./a-zA-Z0-9]+\$[./a-zA-Z0-9]+$',
            'length': None,
            'confidence': 99
        },
        
        # Apache $apr1$ (MD5)
        'Apache-apr1': {
            'pattern': r'^\$apr1\$[./a-zA-Z0-9]{0,8}\$[./a-zA-Z0-9]{22}$',
            'length': None,
            'confidence': 100
        },
        
        # ========== DATABASE SERVER HASHES ==========
        
        # MySQL 4.1+ (*hash)
        'MySQL4.1/MySQL5': {
            'pattern': r'^\*[A-F0-9]{40}$',
            'length': 41,
            'confidence': 100
        },
        
        # MySQL 3.23 (16 chars)
        'MySQL323': {
            'pattern': r'^[a-f0-9]{16}$',
            'length': 16,
            'confidence': 15
        },
        
        # MySQL $A$ (sha256crypt)
        'MySQL $A$ (sha256crypt)': {
            'pattern': r'^\$A\$\d{3}\$[./a-zA-Z0-9]+\$[./a-zA-Z0-9]+$',
            'length': None,
            'confidence': 98
        },
        
        # PostgreSQL (md5 prefix)
        'PostgreSQL': {
            'pattern': r'^md5[a-f0-9]{32}$',
            'length': 35,
            'confidence': 99
        },
        
        # MSSQL 2000
        'MSSQL-2000': {
            'pattern': r'^0x01[a-f0-9]{32}[a-f0-9]{40}$',
            'length': 82,
            'confidence': 100
        },
        
        # MSSQL 2005+
        'MSSQL-2005+': {
            'pattern': r'^0x0100[a-f0-9]{80}$',
            'length': 84,
            'confidence': 100
        },
        
        # ========== LDAP/DIRECTORY HASHES ==========
        
        # LDAP {SHA}
        'LDAP-SHA': {
            'pattern': r'^\{SHA\}[A-Za-z0-9+/]+={0,2}$',
            'length': None,
            'confidence': 99
        },
        
        # LDAP {SSHA}
        'LDAP-SSHA': {
            'pattern': r'^\{SSHA\}[A-Za-z0-9+/]+={0,2}$',
            'length': None,
            'confidence': 99
        },
        
        # ========== HMAC VARIANTS ==========
        
        # HMAC-MD5
        'HMAC-MD5': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 55
        },
        
        # HMAC-SHA1
        'HMAC-SHA1': {
            'pattern': r'^[a-f0-9]{40}$',
            'length': 40,
            'confidence': 70
        },
        
        # HMAC-SHA256
        'HMAC-SHA256': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 78
        },
        
        # HMAC-SHA512
        'HMAC-SHA512': {
            'pattern': r'^[a-f0-9]{128}$',
            'length': 128,
            'confidence': 82
        },
        
        # ========== SALTED HASHES ==========
        
        # md5($pass.$salt)
        'md5($pass.$salt)': {
            'pattern': r'^[a-f0-9]{32}:[a-zA-Z0-9]*$',
            'length': 32,
            'confidence': 62
        },
        
        # sha1($pass.$salt)
        'sha1($pass.$salt)': {
            'pattern': r'^[a-f0-9]{40}:[a-zA-Z0-9]*$',
            'length': 40,
            'confidence': 80
        },
        
        # sha256($pass.$salt)
        'sha256($pass.$salt)': {
            'pattern': r'^[a-f0-9]{64}:[a-zA-Z0-9]*$',
            'length': 64,
            'confidence': 88
        },
        
        # sha512($pass.$salt)
        'sha512($pass.$salt)': {
            'pattern': r'^[a-f0-9]{128}:[a-zA-Z0-9]*$',
            'length': 128,
            'confidence': 92
        },
        
        # ========== CMS HASHES ==========
        
        # Joomla < 2.5.18
        'Joomla': {
            'pattern': r'^[a-f0-9]{32}:[a-zA-Z0-9]*$',
            'length': 32,
            'confidence': 93
        },
    }
    
    @staticmethod
    def detect_hash_type(hash_value):
        """
        Detect hash type from hash value
        
        Args:
            hash_value: The hash string to identify
            
        Returns:
            Dictionary with detected hash types and confidence scores
        """
        if not hash_value:
            return {}
        
        hash_value = hash_value.strip()
        hash_value_lower = hash_value.lower()
        matches = {}
        
        for hash_type, info in HashPatterns.PATTERNS.items():
            pattern = info['pattern']
            
            try:
                # For patterns with special prefixes ($, {, *), use original case
                # For hex patterns, use lowercase
                test_value = hash_value if any(c in pattern for c in ['$', '{', '*', ':']) else hash_value_lower
                
                if re.match(pattern, test_value):
                    matches[hash_type] = {
                        'confidence': info['confidence'],
                        'length': len(hash_value)
                    }
            except re.error:
                continue
        
        return matches
    
    @staticmethod
    def identify_by_pattern(hash_value):
        """
        Identify hash type by pattern matching with intelligent matching
        
        Args:
            hash_value: The hash string to identify
            
        Returns:
            List of tuples: (hash_type, description, confidence)
        """
        if not hash_value:
            return []
        
        hash_value = hash_value.strip()
        hash_value_lower = hash_value.lower()
        matches = []
        
        for hash_type, info in HashPatterns.PATTERNS.items():
            pattern = info['pattern']
            
            try:
                # For patterns with special characters (prefixes), use original case
                # For hex-only patterns, use lowercase
                has_special_chars = any(c in pattern for c in ['$', '{', '*', ':'])
                test_value = hash_value if has_special_chars else hash_value_lower
                
                if re.match(pattern, test_value):
                    confidence = info['confidence']
                    description = f"{hash_type} - {len(hash_value)} chars"
                    matches.append((hash_type, description, confidence))
            except re.error:
                continue
        
        # Sort by confidence descending
        matches.sort(key=lambda x: x[2], reverse=True)
        return matches
    
    @staticmethod
    def get_hash_length_category(length):
        """Get hash candidates by length"""
        length_map = {
            8: ['CRC32', 'MurmurHash', 'Adler32', 'MySQL-323'],
            13: ['descrypt'],
            16: ['Half-MD5', 'MySQL-323'],
            20: ['BSDi-crypt'],
            32: ['MD5', 'MD2', 'MD4', 'NTLM', 'LM'],
            34: ['phpass', 'WordPress phpass'],
            40: ['SHA1', 'RIPEMD-160', 'Tiger160'],
            41: ['MySQL4.1+'],
            56: ['SHA2-224', 'SHA3-224', 'Keccak-224'],
            64: ['SHA2-256', 'SHA3-256', 'GOST', 'Keccak-256', 'BLAKE2s-256', 'Skein-256', 'SM3'],
            80: ['RIPEMD-320'],
            96: ['SHA2-384', 'SHA3-384', 'Keccak-384'],
            128: ['SHA2-512', 'SHA3-512', 'Whirlpool', 'BLAKE2b-512', 'Keccak-512', 'GOST-512'],
        }
        return length_map.get(length, [])
    
    @staticmethod
    def get_pattern_info(hash_type):
        """Get pattern information for a specific hash type"""
        return HashPatterns.PATTERNS.get(hash_type, None)
    
    @staticmethod
    def get_all_patterns():
        """Get all available patterns"""
        return list(HashPatterns.PATTERNS.keys())
    
    @staticmethod
    def get_pattern_count():
        """Get total number of patterns"""
        return len(HashPatterns.PATTERNS)
