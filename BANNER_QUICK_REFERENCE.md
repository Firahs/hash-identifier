# HxMod Banner - Quick Reference

## 🎯 What You See Now

Every time you run HxMod, you'll see this banner first:

```
    +============================+
    |      H x M o d v1.0        |
    |                            |
    | Hash Identification Tool   |
    | Created by MD.SHORIF MIA   |
    +============================+
```

Then your command results appear below.

---

## 📋 Examples

### Example 1: Identifying a Hash
```bash
$ python hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332"

    +============================+
    |      H x M o d v1.0        |
    |                            |
    | Hash Identification Tool   |
    | Created by MD.SHORIF MIA   |
    +============================+


Hash Length: 32 characters
Overall Confidence: 100%
======================================================================

[1] NTLM
    Hashcat Mode: 1000
    Category: Operating System
    Confidence: 100%
    ...
```

### Example 2: Getting Help
```bash
$ python hash_identifier.py -h

    +============================+
    |      H x M o d v1.0        |
    |                            |
    | Hash Identification Tool   |
    | Created by MD.SHORIF MIA   |
    +============================+


usage: HxMod [-h] [--version] ...
HxMod v1.0 - Identify hash types and find hashcat modes
...
```

### Example 3: Checking Version
```bash
$ python hash_identifier.py --version

    +============================+
    |      H x M o d v1.0        |
    |                            |
    | Hash Identification Tool   |
    | Created by MD.SHORIF MIA   |
    +============================+


HxMod v1.0 by MD.SHORIF MIA
```

### Example 4: Database Info
```bash
$ python hash_identifier.py --info

    +============================+
    |      H x M o d v1.0        |
    |                            |
    | Hash Identification Tool   |
    | Created by MD.SHORIF MIA   |
    +============================+


HXMOD DATABASE INFORMATION
Tool: HxMod
Version: v1.0
Created by: MD.SHORIF MIA
...
```

---

## ⚙️ Banner Customization

Want to change the banner? Edit `hash_identifier.py`:

```python
def main():
    # Change 'simple' to 'minimal' for simpler banner
    show_banner(style='simple', effect='color')
    
    cli = HashIdentifierCLI()
    cli.run()
```

**Style Options:**
- `'simple'` - Current box banner ✅
- `'minimal'` - Just text, no box
- `'complex'` - Unicode art (Linux only)

**Effect Options:**
- `'color'` - Colored text ✅
- `'blink'` - Blinking animation
- `'none'` - Plain ASCII

---

## 🎨 Color Effects

The banner automatically:
- ✅ Detects color support
- ✅ Uses colors on modern terminals
- ✅ Falls back to plain text if needed
- ✅ Works on Windows, Linux, macOS

---

## 💻 What Works

✅ Hash identification
✅ Batch file processing
✅ Database searching
✅ Help display
✅ Version check
✅ Mode lookup
✅ All output formats

**Banner displays for every command!**

---

## 📚 Banner Files

| File | Purpose |
|------|---------|
| `lib/banner.py` | Banner module (do not edit unless you know Python) |
| `BANNER.md` | Complete banner documentation |
| `BANNER_IMPLEMENTATION.md` | How banner was implemented |
| `hash_identifier.py` | Main app (line ~2-3 shows how banner is called) |

---

## ❓ FAQ

**Q: Can I disable the banner?**  
A: Not yet, but you can edit `hash_identifier.py` to comment out `show_banner()` line

**Q: Why do I see banner before help?**  
A: Banner shows for all commands - it's part of the startup sequence

**Q: Does banner slow down the tool?**  
A: No - it takes ~10-50ms and doesn't affect hash processing

**Q: Will banner work on my system?**  
A: Yes! Works on Windows, Linux, and macOS with automatic fallback

**Q: Can I customize the banner text?**  
A: Yes! Edit `SIMPLE_BANNER` in `lib/banner.py`

---

## 🚀 Professional Features

✅ Clean ASCII design  
✅ Tool branding (HxMod v1.0)  
✅ Creator attribution (MD.SHORIF MIA)  
✅ Purpose statement  
✅ Color support  
✅ Cross-platform compatibility  

---

## Summary

Your **HxMod v1.0** tool now has a professional banner that:

- Displays every time you run the tool
- Shows tool name, version, and creator
- Uses colors when available
- Works on all platforms
- Has minimal performance impact
- Can be customized if needed

**It's already fully integrated and working!**

---

*Questions?* Check `BANNER.md` for full documentation  
*Want to modify?* See customization section above  
*All set?* Just use the tool normally - banner will appear automatically!

---

Created: February 2, 2026  
For: HxMod v1.0  
By: MD.SHORIF MIA
