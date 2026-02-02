# HxMod v1.0 - Quick Start Guide

**Created by:** MD.SHORIF MIA

## 📍 What Was Created

Your complete hash identifier tool is now ready! Here's what was built:

### Project Structure
```
hash-identifier/
├── hash_identifier.py              ← Main CLI application
├── README.md                       ← Full documentation
├── setup.sh                        ← Linux installation script
├── requirements.txt                ← Python dependencies (optional)
├── .gitignore                      ← Git ignore file
├── database/
│   └── hashcat_modes.json         ← 450+ hash modes database
├── lib/
│   ├── hash_patterns.py           ← Hash pattern matching (100+ patterns)
│   ├── hash_analyzer.py           ← Core analysis engine
│   └── formatter.py               ← Output formatting (9 formats)
└── examples/
    └── sample_hashes.txt          ← Test hashes
```

## 🚀 Quick Start (Windows)

### 1. Test the Installation

```bash
cd hash-identifier
python hash_identifier.py -h
```

You should see the help menu.

### 2. Identify Your First Hash

```bash
python hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332"
```

Expected Output:
```
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

### 3. Try Different Output Formats

```bash
# JSON output
python hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332" -o json

# Hashcat commands
python hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332" -o hashcat

# Detailed information
python hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332" -o detailed

# With feature analysis
python hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332" --features
```

### 4. Test with Sample Hashes

```bash
python hash_identifier.py -f examples/sample_hashes.txt
```

### 5. Search the Database

```bash
# Find all bcrypt modes
python hash_identifier.py --search "bcrypt"

# Get details for mode 3200
python hash_identifier.py --mode 3200

# List all categories
python hash_identifier.py --categories

# List modes in a category
python hash_identifier.py --list "Operating System"
```

## 🚀 Quick Start (Linux/macOS)

### 1. Install

```bash
cd hash-identifier
chmod +x setup.sh
./setup.sh

# Follow the prompts
```

### 2. Use Anywhere

After installation, you can run from anywhere:

```bash
# If you created a symlink
hash-identifier "8846f7eaee8fb117ad06bdd810b7e332"

# Or using python directly
python3 hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332"
```

## 📚 Common Use Cases

### Case 1: Identify Unknown Hash

```bash
python hash_identifier.py "$2a$12$R9h/cIPz0gi.URNNGHQ1be3DlH.PKZbv5H8KnzzVgXXbVxzy2K7E."
# Result: bcrypt (Mode 3200)
```

### Case 2: Get Hashcat Command

```bash
python hash_identifier.py <hash> -o hashcat
# Shows: hashcat -m 3200 -a 0 <hash_file> <wordlist>
```

### Case 3: Batch Process File

```bash
# Create a file with multiple hashes (one per line)
echo "8846f7eaee8fb117ad06bdd810b7e332" > hashes.txt
echo "356a192b7913b04c54574d18c28d46e6395428ab" >> hashes.txt

# Process them
python hash_identifier.py -f hashes.txt --output json --save results.json
```

### Case 4: Export Results

```bash
# As CSV
python hash_identifier.py -f hashes.txt --output csv > results.csv

# As JSON
python hash_identifier.py -f hashes.txt --output json > results.json
```

### Case 5: Research Hashcat Modes

```bash
# What modes exist?
python hash_identifier.py --categories

# Modes in "Operating System" category?
python hash_identifier.py --list "Operating System"

# Details on mode 1800?
python hash_identifier.py --mode 1800
```

## 🔑 Key Features

✅ **Offline**: Works completely without internet
✅ **Fast**: Instant hash identification
✅ **Comprehensive**: 450+ hash modes supported
✅ **Accurate**: Confidence scoring for each match
✅ **Flexible**: 9 different output formats
✅ **Batch**: Process multiple hashes at once
✅ **Searchable**: Browse and search hash database
✅ **Zero Dependencies**: Works with standard Python

## 💡 Pro Tips

1. **Batch Processing**: Always use `-f` for multiple hashes - much faster
2. **JSON Output**: Great for scripting and data processing
3. **Feature Analysis**: Use `--features` to understand hash structure
4. **Confidence Scoring**: Higher confidence = more likely correct identification
5. **Variants**: Check "Variants" field for different algorithm versions (e.g., $2a$ vs $2b$ in bcrypt)

## 🔍 Hash Types Supported

The database includes identification for:

- **Raw Hashes**: MD5, SHA1, SHA224, SHA256, SHA384, SHA512, SHA3, BLAKE2b, RIPEMD160
- **Unix Crypt**: bcrypt, md5crypt ($1$), sha256crypt ($5$), sha512crypt ($6$), apr1
- **Windows**: NTLM, LM, Domain Cached Credentials
- **Network**: NetNTLMv1/v2, Kerberos, WPA, JWT, SIP
- **KDF**: Argon2, scrypt, PBKDF2 variants
- **FDE**: LUKS, BitLocker, FileVault2, VeraCrypt
- **Databases**: MySQL, PostgreSQL, Oracle, MSSQL
- **Archives**: 7-Zip, ZIP, RAR5
- **Crypto Wallets**: Bitcoin, Ethereum, Electrum
- **And 50+ more categories...**

## ❓ Troubleshooting

### "No matches found"

The hash might be:
- Corrupted
- In base64 instead of hex
- A new/uncommon format
- Not actually a hash

**Solution**: Try `--features` to see what pattern matching detected

### Hash is too short/long

```bash
# See what the tool detected
python hash_identifier.py <hash> --features

# Look at the length and characteristics
# Maybe it's a partial hash or includes extra data
```

### Want to understand a specific hash?

```bash
# Analyze its features
python hash_identifier.py "<hash>" --features

# Shows: length, hex/base64, delimiters, prefix, case-sensitivity
```

## 🎯 Next Steps

1. **Test with your own hashes**: Try the tool with real hashes you want to identify
2. **Batch process files**: Test with multiple hashes
3. **Explore the database**: Use `--search` and `--list` to learn about hash types
4. **Automate**: Use JSON output in scripts
5. **Share**: Add to your security toolkit

## 📖 For More Information

See `README.md` for:
- Detailed usage documentation
- All command-line options
- API usage for Python scripts
- Advanced examples
- FAQ and troubleshooting

## 🚀 You're Ready!

Your hash identifier is fully functional and ready to use. Start identifying hashes!

```bash
python hash_identifier.py <your-hash-here>
```

**Happy hash hunting! 🎯**

---

Built with ❤️ for the security community | Offline Hash Identification Tool
