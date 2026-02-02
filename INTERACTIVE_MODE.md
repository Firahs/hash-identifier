# HxMod v1.0 - Executive Mode & Hacker Banner

## 🎯 What's New

### 1. ✅ Hacker-Style Banner
Professional ASCII art banner with green color theme (like in your reference image)

```
    ================================================================
    #                                                              #
    #       /\  /\          /\/\/\    /\  /\   /\/\/\   /\  /\     #
    #      /  \/  \        /        \ /  \/  \ /        /  \/  \    #
    #     /          \    /  /\/\/\  /          \  /\/\/  /          #
    #    /  \    /  \   /  /    /  / \    /  \ /      / \    /  \   #
    #   /      \/      \ \__/    /__/  \__/    \\___/     \__/      #
    #                                                              #
    #         v1.0 - Hash Identification Tool                     #
    #         By MD.SHORIF MIA                                    #
    #         www.blackploit.com                                  #
    #         Root@blackploit.com                                 #
    #                                                              #
    ================================================================
```

### 2. ✅ Interactive Mode with HASH: Prompt
When you run HxMod without arguments, you get an interactive prompt:

```
HASH: [user types hash here]
```

### 3. ✅ Executable Scripts
- `hxmod` - Linux/macOS executable
- `hxmod.bat` - Windows batch wrapper
- Just type `hxmod` or run the script directly

---

## 🚀 Usage Examples

### Interactive Mode (No Arguments)

```bash
$ python hash_identifier.py
[Banner displays]

========================================
Interactive Mode - Type 'help' for commands, 'quit' to exit
========================================

HASH: 8846f7eaee8fb117ad06bdd810b7e332

Hash Length: 32 characters
[Results...]

HASH: help

Commands:
  help                 - Show this help
  quit/exit            - Exit HxMod
  clear                - Clear screen
  info                 - Show database info
  categories           - List all categories
  search <name>        - Search hash modes
  
Just type a hash to identify it!

HASH: quit
Goodbye! 👋
```

### CLI Mode (With Arguments)

```bash
# Identify a hash
$ python hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332"
$ python hash_identifier.py "5d41402abc4b2a76b9719d911017c592"

# Get help
$ python hash_identifier.py -h
$ python hash_identifier.py --help

# Batch processing
$ python hash_identifier.py -f hashes.txt

# Database info
$ python hash_identifier.py --info

# Search modes
$ python hash_identifier.py --search "bcrypt"

# List categories
$ python hash_identifier.py --categories
```

### Using Executables

**Linux/macOS:**
```bash
# Make executable
chmod +x hxmod

# Run it
./hxmod
./hxmod "hash_here"
./hxmod --info
```

**Windows:**
```bash
# Using batch wrapper
hxmod.bat
hxmod.bat "8846f7eaee8fb117ad06bdd810b7e332"
hxmod.bat --info

# Or with cmd
cmd /c hxmod.bat "hash"
```

---

## 📋 Interactive Commands

### help
Shows all available commands

```
HASH: help
```

### quit / exit
Exit the interactive mode

```
HASH: quit
HASH: exit
```

### clear
Clear the screen and redisplay banner

```
HASH: clear
```

### info
Show database information

```
HASH: info
HXMOD DATABASE INFORMATION
Tool: HxMod
Version: v1.0
...
```

### categories
List all hash categories

```
HASH: categories
Available Hash Categories:
...
```

### search <name>
Search for hash modes by name

```
HASH: search bcrypt
Search Results for 'bcrypt':
...
```

### [hash value]
Just type a hash to identify it

```
HASH: 8846f7eaee8fb117ad06bdd810b7e332
Hash Length: 32 characters
[Results...]
```

---

## 🎨 Banner Customization

### Change Banner Style

Edit `hash_identifier.py` in the `main()` function:

```python
# Hacker style (current)
show_banner(style='hacker', use_color=True)

# Simple box style
show_banner(style='simple', use_color=True)
```

### Modify Banner Text

Edit `lib/banner.py`:

```python
HACKER_BANNER = """
    Your custom ASCII art here
"""
```

---

## 💾 File Changes

### New Files
- `hxmod` - Linux/macOS executable wrapper
- `hxmod.bat` - Windows batch wrapper

### Modified Files
- `lib/banner.py` - Updated with hacker-style banner
- `hash_identifier.py` - Added interactive mode

---

## 🔧 How It Works

### Flow When Running Without Arguments
```
1. User runs: python hash_identifier.py
2. Banner displays (hacker style in green)
3. Interactive prompt appears: HASH:
4. User types command or hash
5. Results displayed
6. Loop back to step 4
```

### Flow When Running With Arguments
```
1. User runs: python hash_identifier.py "hash"
2. Banner displays
3. Process hash (CLI mode)
4. Display results
5. Exit
```

---

## 🎯 Smart Mode Detection

The tool automatically detects:

**Interactive Mode** (if no arguments):
- Shows HASH: prompt
- Stays running for multiple inputs
- Allows special commands (help, info, etc.)

**CLI Mode** (if arguments provided):
- Processes arguments
- Displays results
- Exits immediately

---

## 🚀 After Git Clone

Users can do:

```bash
# Clone the repository
git clone https://github.com/your-repo/hxmod.git
cd hxmod

# Run interactive mode
python hash_identifier.py

# Or with wrapper
chmod +x hxmod  (Linux/macOS only)
./hxmod

# Or use CLI
python hash_identifier.py "hash_here"
```

---

## 📊 Features Summary

✅ Hacker-style ASCII banner  
✅ Green color theme (hacker aesthetic)  
✅ Interactive HASH: prompt  
✅ CLI mode with full arguments  
✅ Smart mode detection  
✅ Special commands (help, info, search, etc.)  
✅ Clear screen with banner redisplay  
✅ Executable wrappers for easy access  
✅ Cross-platform support  
✅ Zero external dependencies  

---

## 🎓 Examples

### Example 1: Interactive Session
```
$ python hash_identifier.py

[Hacker Banner displays]

==========================================
Interactive Mode - Type 'help' for commands, 'quit' to exit
==========================================

HASH: 8846f7eaee8fb117ad06bdd810b7e332

Hash Length: 32 characters
Overall Confidence: 100%

[1] NTLM
    Hashcat Mode: 1000
    Confidence: 100%

[2] LM
    Hashcat Mode: 3000
    Confidence: 100%

HASH: search md5

Search Results for 'md5':
Mode    Hash Type                  Category
0       MD5                        Raw Hash

HASH: quit
Goodbye! 👋
```

### Example 2: CLI Mode
```
$ python hash_identifier.py "5d41402abc4b2a76b9719d911017c592"

[Hacker Banner displays]

Hash Length: 32 characters
Overall Confidence: 100%

[1] NTLM
    Hashcat Mode: 1000
    Confidence: 100%

[Results...]
```

### Example 3: Batch Processing
```
$ python hash_identifier.py -f hashes.txt

[Hacker Banner displays]

Processing 22 hashes...

BATCH HASH IDENTIFICATION SUMMARY
Total Hashes Analyzed: 22
...
```

---

## 📝 Notes

- Banner displays automatically for all modes
- Interactive mode is user-friendly for penetration testers
- CLI mode works perfectly with scripts and automation
- Hacker aesthetic maintained throughout
- All features from original tool still available

---

## ✅ Status

✅ Hacker banner implemented  
✅ Interactive mode working  
✅ Executable wrappers created  
✅ CLI mode unchanged (backward compatible)  
✅ Cross-platform support  
✅ All tests passing  

---

**Created:** February 2, 2026  
**For:** HxMod v1.0  
**By:** MD.SHORIF MIA
