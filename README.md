# HxMod v1.0

A fast, offline CLI tool for identifying hash types and finding corresponding Hashcat modes. No internet required!

**Created by:** MD.SHORIF MIA

## 🎯 Features

- **Offline Operation**: Works completely offline - no internet connection needed
- **Multiple Hash Types**: Identifies 100+ hash types including:
  - Raw hashes (MD5, SHA1, SHA256, SHA512, etc.)
  - Unix crypt hashes (bcrypt, sha256crypt, sha512crypt)
  - Windows hashes (NTLM, LM, Domain Cached Credentials)
  - Network protocols (NetNTLMv1/v2, Kerberos, WPA)
  - Modern KDF (Argon2, scrypt, PBKDF2)
  - Full-disk encryption (LUKS, BitLocker, FileVault2)
  - Archives (ZIP, RAR, 7-Zip)
  - Cryptocurrency wallets
  - And many more...

- **Hashcat Integration**: Returns Hashcat mode numbers for each identified hash
- **Multiple Output Formats**: Standard, Table, Detailed, JSON, CSV, Compact, Hashcat commands
- **Batch Processing**: Identify multiple hashes from a file
- **Feature Analysis**: Analyze hash characteristics
- **Database Search**: Search and browse Hashcat modes
- **Zero Dependencies**: Uses only Python standard library (optional dependencies available)

## 📋 Requirements

- Python 3.6 or later
- Linux/Unix/macOS or Windows with Python installed

## 🚀 Installation

### On Linux/Unix/macOS

```bash
# Clone or download the repository
cd hash-identifier

# Run the installation script
chmod +x setup.sh
./setup.sh

# Or manual installation
python3 hash_identifier.py -h
```

### On Windows

```bash
# Install Python 3.6+ from python.org
# Then navigate to the directory and run:
python hash_identifier.py -h
```

## 💻 Usage

### Basic Hash Identification

```bash
# Identify a single hash
python3 hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332"

# Get more detailed output
python3 hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332" --output detailed

# Show hash feature analysis
python3 hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332" --features
```

### Batch Processing

```bash
# Identify hashes from a file (one per line)
python3 hash_identifier.py -f hashes.txt

# Save results to file
python3 hash_identifier.py -f hashes.txt --save results.txt

# Export as JSON
python3 hash_identifier.py -f hashes.txt --output json
```

### Output Formats

```bash
# Standard format (default)
python3 hash_identifier.py <hash> --output standard

# Table format
python3 hash_identifier.py <hash> --output table

# Detailed format with full info
python3 hash_identifier.py <hash> --output detailed

# JSON format
python3 hash_identifier.py <hash> --output json

# Compact JSON
python3 hash_identifier.py <hash> --output json_compact

# CSV format
python3 hash_identifier.py <hash> --output csv

# Compact single line
python3 hash_identifier.py <hash> --output compact

# Hashcat command suggestions
python3 hash_identifier.py <hash> --output hashcat

# Brief format (hash type + mode only)
python3 hash_identifier.py <hash> --output brief
```

### Database Operations

```bash
# List all hash categories
python3 hash_identifier.py --categories

# List modes in a category
python3 hash_identifier.py --list "Operating System"

# Search for a hash type
python3 hash_identifier.py --search "bcrypt"

# Get details for a specific Hashcat mode
python3 hash_identifier.py --mode 3200

# Show database information
python3 hash_identifier.py --info
```

## 📊 Examples

### Example 1: Identify MD5 Hash

```bash
$ python3 hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332"

======================================================================
Hash Length: 32 characters
Overall Confidence: 100%
======================================================================

[1] MD5
    Hashcat Mode: 0
    Category: Raw Hash
    Description: MD5 hash
    Confidence: 100%
    Salt Type: none
    Example: 8846f7eaee8fb117ad06bdd810b7e332
```

### Example 2: Identify bcrypt Hash

```bash
$ python3 hash_identifier.py "$2a$12$R9h/cIPz0gi.URNNGHQ1be3DlH.PKZbv5H8KnzzVgXXbVxzy2K7E."

======================================================================
Hash Length: 60 characters
Overall Confidence: 95%
======================================================================

[1] bcrypt
    Hashcat Mode: 3200
    Category: Operating System
    Description: bcrypt $2*$, Blowfish (Unix)
    Confidence: 95%
    Salt Type: embedded
    Variants: $2a$, $2b$, $2y$
```

### Example 3: Get Hashcat Commands

```bash
$ python3 hash_identifier.py "$2a$12$..." --output hashcat

Hashcat Command Suggestions:
======================================================================

[1] bcrypt (Mode 3200)
    hashcat -m 3200 -a 0 <hash_file> <wordlist>
    hashcat -m 3200 -a 3 <hash_file> ?a?a?a?a
```

### Example 4: Batch Process with JSON Output

```bash
$ python3 hash_identifier.py -f hashes.txt --output json

[
  {
    "input_hash": "8846f7eaee8fb117ad06bdd810b7e3...",
    "hash_length": 32,
    "matches": [
      {
        "hash_type": "MD5",
        "hashcat_mode": 0,
        "category": "Raw Hash",
        "confidence": 100,
        "salt_type": "none"
      }
    ]
  }
]
```


## 🎓 How It Works

### Hash Identification Process

1. **Pattern Matching**: Input is matched against 100+ regex patterns organized by category
2. **Confidence Scoring**: Each match receives a confidence score based on:
   - Pattern specificity
   - Hash format characteristics
   - Known delimiters and prefixes
3. **Database Lookup**: Matched hash types are looked up in the hashcat modes database
4. **Result Compilation**: All matches are compiled with Hashcat modes and metadata

### Why Offline?

- **Database Embedded**: Complete hashcat modes database is included (JSON format)
- **No Network Calls**: All pattern matching and lookups are local
- **Privacy**: No hash data is sent anywhere
- **Speed**: Instant results without network latency
- **Reliability**: Works anywhere, anytime

## 🔍 Supported Hash Categories

- Raw Hash (MD5, SHA1, SHA256, SHA512, SHA3, BLAKE2b, etc.)
- Raw Hash salted and/or iterated
- Raw Hash authenticated (HMAC variants)
- Unix-style (bcrypt, md5crypt, sha256crypt, sha512crypt, apr1)
- Operating System (NTLM, LM, DCC, macOS, BSD)
- Network Protocol (NetNTLMv1/v2, Kerberos, WPA, JWT, SIP)
- Database Server (MySQL, PostgreSQL, Oracle, MSSQL)
- FTP, HTTP, SMTP, LDAP
- Enterprise Applications (SAP, PeopleSoft, etc.)
- Generic KDF (PBKDF2, scrypt, Argon2)
- Full-Disk Encryption (LUKS, BitLocker, FileVault2, VeraCrypt)
- Password Manager (KeePass, LastPass, 1Password)
- Archive (7-Zip, ZIP, RAR5)
- Document (Office, PDF)
- Cryptocurrency Wallet (Bitcoin, Ethereum, Electrum)
- Framework (Django, Werkzeug, Passlib)
- And more...

## 💾 Sample Hashes

Common hashes to test with:

```
MD5:         8846f7eaee8fb117ad06bdd810b7e332
SHA1:        356a192b7913b04c54574d18c28d46e6395428ab
SHA256:      e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
SHA512:      cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e
bcrypt:      $2a$12$R9h/cIPz0gi.URNNGHQ1be3DlH.PKZbv5H8KnzzVgXXbVxzy2K7E.
NTLM:        8846f7eaee8fb117ad06bdd810b7e332
Argon2:      $argon2id$v=19$m=65536,t=3,p=1$salt$hash
PBKDF2:      pbkdf2_sha256$260000$salt$hash
JWT:         eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.dozjgNryP4J3jVmNHl0w5N_XgL0n3I9PlFUP0THsR8U
```

## 🔧 Advanced Usage

### Programmatic Usage (Python)

```python
from lib.hash_analyzer import HashAnalyzer

analyzer = HashAnalyzer()

# Identify a single hash
result = analyzer.identify_hash("8846f7eaee8fb117ad06bdd810b7e332")
print(result)

# Search database
modes = analyzer.search_by_name("bcrypt")
for mode in modes:
    print(f"Mode {mode['mode']}: {mode['name']}")

# Get mode details
mode_info = analyzer.get_mode_details(3200)
print(mode_info)

# List categories
categories = analyzer.list_categories()
for cat in categories:
    print(cat)
```

### Using in Scripts

```bash
#!/bin/bash

# Process all hashes in a directory
for hashfile in hashes/*.txt; do
    echo "Processing $hashfile..."
    python3 hash_identifier.py -f "$hashfile" \
        --output json \
        --save "results/$(basename $hashfile .txt).json"
done
```

## 🚨 Troubleshooting

### "Database not found" error

```bash
# Verify the database exists in the correct location
ls -la database/hashcat_modes.json

# If missing, the file should be at:
# <installation_directory>/database/hashcat_modes.json
```

### "No matches found"

- Hash may be corrupted or in an unsupported format
- Try the `--features` flag to see what pattern matching found
- Check if the hash is actually a hash (should be hex/base64 encoded)

### Python version issues

```bash
# Check Python version
python3 --version

# Should be 3.6 or later
# If not, install a newer Python version
```

## 📄 License

This tool is open source and available for public use. See LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional hash type patterns
- Performance optimizations
- Enhanced output formats
- Better documentation

## 🔗 References

- [Hashcat Official Wiki](https://hashcat.net/wiki/)
- [Hash Format Examples](https://hashcat.net/wiki/#example_hashes)
- [Hashcat Modes Documentation](https://hashcat.net/wiki/#hashcat)



## 📞 Support

For issues, questions, or suggestions, please create an issue on GitHub or contact the maintainer.

---

**Made with ❤️ for the security community** | Offline Hash Identification for Everyone
