"""
Hash Pattern Recognition Module
Identifies hash types using regex patterns
Created by: MD.SHORIF MIA
"""

import re


class HashPatterns:
    """Collection of hash type patterns and detection methods"""
    
    # Pattern definitions for various hash types
    PATTERNS = {
        # MD5 and MD5-like
        'MD5': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 60  # Can be confused with other 32-char hashes
        },
        'MD4': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 50
        },
        'NTLM': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 100  # When confirmed via context
        },
        'LM': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 100  # When confirmed via context
        },
        
        # SHA1
        'SHA1': {
            'pattern': r'^[a-f0-9]{40}$',
            'length': 40,
            'confidence': 80
        },
        
        # SHA2-224 (SHA224)
        'SHA2-224': {
            'pattern': r'^[a-f0-9]{56}$',
            'length': 56,
            'confidence': 83
        },
        
        # SHA2-256 (SHA256)
        'SHA2-256': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 85
        },
        
        # SHA2-384 (SHA384)
        'SHA2-384': {
            'pattern': r'^[a-f0-9]{96}$',
            'length': 96,
            'confidence': 88
        },
        
        # SHA2-512 (SHA512)
        'SHA2-512': {
            'pattern': r'^[a-f0-9]{128}$',
            'length': 128,
            'confidence': 88
        },
        
        # Bcrypt
        'bcrypt': {
            'pattern': r'^\$2[aby]\$\d{2}\$[./A-Za-z0-9]{53}$',
            'length': None,
            'confidence': 100
        },
        
        # Scrypt
        'scrypt': {
            'pattern': r'^\$7\$.{,11}\$[./A-Za-z0-9]{0,32}\$[./A-Za-z0-9]{32}$',
            'length': None,
            'confidence': 100
        },
        
        # Argon2
        'Argon2': {
            'pattern': r'^\$argon2[id]{1}\$v=\d+\$m=\d+,t=\d+,p=\d+\$.{22}[.A-Za-z0-9]{31}$',
            'length': None,
            'confidence': 100
        },
        
        # PBKDF2 - using the exact names from database
        'PBKDF2-HMAC-SHA1': {
            'pattern': r'^\$pbkdf2-sha1\$[0-9]+\$[./A-Za-z0-9]+\$[./A-Za-z0-9]+$',
            'length': None,
            'confidence': 100
        },
        'PBKDF2-HMAC-SHA256': {
            'pattern': r'^\$pbkdf2-sha256\$[0-9]+\$[./A-Za-z0-9]+\$[./A-Za-z0-9]+$',
            'length': None,
            'confidence': 100
        },
        
        # md5crypt (MD5 crypt)
        'md5crypt': {
            'pattern': r'^\$1\$[./a-zA-Z0-9]{0,8}\$[./a-zA-Z0-9]{22}$',
            'length': None,
            'confidence': 100
        },
        
        # sha256crypt $5$
        'sha256crypt $5$': {
            'pattern': r'^\$5\$[./a-zA-Z0-9]{0,16}\$[./a-zA-Z0-9]{43}$',
            'length': None,
            'confidence': 100
        },
        
        # sha512crypt $6$
        'sha512crypt $6$': {
            'pattern': r'^\$6\$[./a-zA-Z0-9]{0,16}\$[./a-zA-Z0-9]{86}$',
            'length': None,
            'confidence': 100
        },
        
        # Unix/Linux crypt
        'Unix-DES': {
            'pattern': r'^[./A-Za-z0-9]{13}$',
            'length': 13,
            'confidence': 70
        },
        
        # MySQL - using exact database names
        'MySQL323': {
            'pattern': r'^[a-f0-9]{16}$',
            'length': 16,
            'confidence': 80
        },
        'MySQL4.1/MySQL5': {
            'pattern': r'^\*[A-F0-9]{40}$',
            'length': 41,
            'confidence': 100
        },
        
        # MSSQL
        'MSSQL-2000': {
            'pattern': r'^0x[a-f0-9]{80}$',
            'length': 82,
            'confidence': 100
        },
        'MSSQL-2005': {
            'pattern': r'^0x[a-f0-9]{80}$',
            'length': 82,
            'confidence': 100
        },
        'MSSQL-2012': {
            'pattern': r'^0x[a-f0-9]{128}$',
            'length': 130,
            'confidence': 100
        },
        
        # PostgreSQL
        'PostgreSQL': {
            'pattern': r'^\$2[aby]\$\d{2}\$[./A-Za-z0-9]{53}$',
            'length': None,
            'confidence': 100
        },
        
        # Oracle
        'Oracle7': {
            'pattern': r'^[a-f0-9]{16}$',
            'length': 16,
            'confidence': 70
        },
        'Oracle10': {
            'pattern': r'^S:[A-F0-9]{60}$',
            'length': 62,
            'confidence': 100
        },
        'Oracle11': {
            'pattern': r'^[A-F0-9]{30}$',
            'length': 30,
            'confidence': 85
        },
        
        # Cisco
        'Cisco-IOS': {
            'pattern': r'^\$1\$[A-Z0-9]{5}\$[A-Z0-9]{33}$',
            'length': None,
            'confidence': 100
        },
        'Cisco-PIX': {
            'pattern': r'^[a-z0-9]{16}$',
            'length': 16,
            'confidence': 70
        },
        'Cisco-ASA': {
            'pattern': r'^\$1\$[A-Z0-9]{5}\$[A-Z0-9]{33}$',
            'length': None,
            'confidence': 100
        },
        'Cisco-Type7': {
            'pattern': r'^[0-9]{2}[a-zA-Z0-9]{48}$',
            'length': 50,
            'confidence': 90
        },
        
        # LDAP
        'LDAP-MD5': {
            'pattern': r'^{MD5}[a-zA-Z0-9+/]{24}={0,2}$',
            'length': None,
            'confidence': 100
        },
        'LDAP-SHA': {
            'pattern': r'^{SHA}[a-zA-Z0-9+/]{28}={0,2}$',
            'length': None,
            'confidence': 100
        },
        'LDAP-SSHA': {
            'pattern': r'^{SSHA}[a-zA-Z0-9+/]{38,54}={0,2}$',
            'length': None,
            'confidence': 100
        },
        
        # RipeMD
        'RIPEMD-128': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 60
        },
        'RIPEMD-160': {
            'pattern': r'^[a-f0-9]{40}$',
            'length': 40,
            'confidence': 75
        },
        'RIPEMD-256': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 75
        },
        'RIPEMD-320': {
            'pattern': r'^[a-f0-9]{80}$',
            'length': 80,
            'confidence': 85
        },
        
        # HMAC - using exact names from database
        'HMAC-MD5 (key = $pass)': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 50
        },
        'HMAC-SHA1 (key = $pass)': {
            'pattern': r'^[a-f0-9]{40}$',
            'length': 40,
            'confidence': 65
        },
        'HMAC-SHA256 (key = $pass)': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 70
        },
        'HMAC-SHA512 (key = $pass)': {
            'pattern': r'^[a-f0-9]{128}$',
            'length': 128,
            'confidence': 75
        },
        
        # DES variants
        'DES-crypt': {
            'pattern': r'^[./A-Za-z0-9]{13}$',
            'length': 13,
            'confidence': 80
        },
        'Triple-DES-crypt': {
            'pattern': r'^[./A-Za-z0-9]{20}$',
            'length': 20,
            'confidence': 85
        },
        
        # Whirlpool
        'Whirlpool': {
            'pattern': r'^[a-f0-9]{128}$',
            'length': 128,
            'confidence': 80
        },
        
        # GOST
        'GOST': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 75
        },
        
        # Skein
        'Skein': {
            'pattern': r'^[a-f0-9]{128}$',
            'length': 128,
            'confidence': 75
        },
        
        # Blake2
        'Blake2': {
            'pattern': r'^[a-f0-9]{64,128}$',
            'length': None,
            'confidence': 80
        },
        
        # CRC variants
        'CRC32': {
            'pattern': r'^[a-f0-9]{8}$',
            'length': 8,
            'confidence': 60
        },
        
        # Adler32
        'Adler32': {
            'pattern': r'^[a-f0-9]{8}$',
            'length': 8,
            'confidence': 50
        },
        
        # MD2
        'MD2': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 50
        },
        
        # Tiger
        'Tiger128': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 55
        },
        'Tiger160': {
            'pattern': r'^[a-f0-9]{40}$',
            'length': 40,
            'confidence': 70
        },
        'Tiger192': {
            'pattern': r'^[a-f0-9]{48}$',
            'length': 48,
            'confidence': 75
        },
        
        # Snefru
        'Snefru128': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 50
        },
        'Snefru256': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 70
        },
        
        # Haval
        'Haval128': {
            'pattern': r'^[a-f0-9]{32}$',
            'length': 32,
            'confidence': 50
        },
        'Haval160': {
            'pattern': r'^[a-f0-9]{40}$',
            'length': 40,
            'confidence': 65
        },
        'Haval192': {
            'pattern': r'^[a-f0-9]{48}$',
            'length': 48,
            'confidence': 70
        },
        'Haval224': {
            'pattern': r'^[a-f0-9]{56}$',
            'length': 56,
            'confidence': 75
        },
        'Haval256': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 80
        },
        
        # SHA3 (Keccak)
        'SHA3-224': {
            'pattern': r'^[a-f0-9]{56}$',
            'length': 56,
            'confidence': 82
        },
        'SHA3-256': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 83
        },
        'SHA3-384': {
            'pattern': r'^[a-f0-9]{96}$',
            'length': 96,
            'confidence': 86
        },
        'SHA3-512': {
            'pattern': r'^[a-f0-9]{128}$',
            'length': 128,
            'confidence': 86
        },
        
        # BLAKE2 variants
        'BLAKE2b-512': {
            'pattern': r'^\$BLAKE2\$[a-f0-9]{128}$',
            'length': 136,
            'confidence': 95
        },
        'BLAKE2-256': {
            'pattern': r'^[a-f0-9]{64}$',
            'length': 64,
            'confidence': 78
        },
        
        # phpBB (WordPress-style hashing)
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
        
        hash_value = hash_value.strip().lower()
        matches = {}
        
        for hash_type, info in HashPatterns.PATTERNS.items():
            pattern = info['pattern']
            
            try:
                if re.match(pattern, hash_value):
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
        Identify hash type by pattern matching
        
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
                # For patterns with special prefixes ($), use original case
                # For hex patterns, use lowercase
                test_value = hash_value if '$' in pattern else hash_value_lower
                
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
        """Get hash category by length"""
        if length == 8:
            return ['CRC32', 'Adler32']
        elif length == 16:
            return ['MD5', 'MySQL323', 'Oracle7', 'Cisco-PIX']
        elif length == 32:
            return ['MD5', 'MD4', 'NTLM', 'LM', 'MD2', 'Tiger128']
        elif length == 40:
            return ['SHA1', 'RIPEMD-160', 'Tiger160']
        elif length == 48:
            return ['Tiger192', 'Haval192']
        elif length == 56:
            return ['Haval224']
        elif length == 64:
            return ['SHA256', 'RIPEMD-256', 'GOST', 'Skein']
        elif length == 80:
            return ['RIPEMD-320']
        elif length == 96:
            return ['SHA384']
        elif length == 128:
            return ['SHA512', 'Whirlpool', 'Blake2']
        else:
            return []
    
    @staticmethod
    def get_pattern_info(hash_type):
        """Get pattern information for a specific hash type"""
        return HashPatterns.PATTERNS.get(hash_type, None)
