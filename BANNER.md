# HxMod Banner Effects Documentation

## Overview

HxMod now displays a professional ASCII banner when the tool starts. The banner includes:

- **Tool Name:** HxMod v1.0
- **Description:** Hash Identification Tool  
- **Creator:** MD.SHORIF MIA
- **Color Support:** Terminal colors with fallback for non-color terminals

---

## Banner Display

When you run HxMod, you'll see:

```
    +============================+
    |      H x M o d v1.0        |
    |                            |
    | Hash Identification Tool   |
    | Created by MD.SHORIF MIA   |
    +============================+
```

The banner appears **before** any operation:
- Hash identification
- File processing  
- Database queries
- Help display
- Any other command

---

## Banner Features

### ✅ Color Support
- **Automatic Detection:** Banner detects if terminal supports colors
- **Fallback:** Works in non-color environments
- **Multi-color:** Different colors for each banner line on supported terminals

### ✅ Cross-Platform
- **Windows:** PowerShell, Command Prompt (ASCII-safe characters)
- **Linux:** Full support with colors
- **macOS:** Full support with colors

### ✅ Banner Styles

The banner module provides multiple styles:

1. **SIMPLE_BANNER** (Currently Used)
   ```
   +============================+
   |      H x M o d v1.0        |
   |                            |
   | Hash Identification Tool   |
   | Created by MD.SHORIF MIA   |
   +============================+
   ```

2. **MINIMAL_BANNER**
   ```
   HxMod v1.0 - Hash Identifier
   Created by MD.SHORIF MIA
   ```

3. **BANNER_TEXT**
   - Complex Unicode box drawing (for Linux/macOS terminals)

---

## Color Effect Options

The banner module (`lib/banner.py`) supports multiple effects:

### 1. Static Colors (Current Default)
- Different ANSI colors for each line
- No animation
- Clean and professional look

### 2. Blinking Effect (Available)
- X and O characters blink
- Creates eye-catching animation
- Optional blink cycles

### 3. No Color (Fallback)
- Plain ASCII output
- Works on all terminals
- No color codes

---

## Technical Details

### Color Codes Used
```python
Colors = {
    'CYAN': '\033[96m',
    'MAGENTA': '\033[95m',
    'BRIGHT_BLUE': '\033[94m',
    'BRIGHT_GREEN': '\033[92m',
    'BRIGHT_RED': '\033[91m'
}
```

### Banner Module Location
- **File:** `lib/banner.py`
- **Main Class:** `BannerPrinter`
- **Entry Point:** `show_banner()`

### Integration Point
- **File:** `hash_identifier.py`
- **Function:** `main()`
- **Call:** `show_banner(style='simple', effect='color')`

---

## Customization

### Changing Banner Style

To modify the banner style, edit `hash_identifier.py`:

```python
def main():
    """Main entry point"""
    # Change style to 'minimal' or 'complex'
    show_banner(style='minimal', effect='color')
    print()
    
    cli = HashIdentifierCLI()
    cli.run()
```

### Changing Color Effect

Options for `effect` parameter:
- `'color'` - Colored text (default)
- `'blink'` - Blinking animation
- `'none'` - Plain ASCII, no colors

### Changing Banner Text

Edit `lib/banner.py` to modify banner content:

```python
SIMPLE_BANNER = """
    Your custom banner here
"""
```

---

## Testing the Banner

### Test Individual Styles

Run the banner module directly:
```bash
python lib/banner.py
```

This shows:
1. Simple banner with color
2. Simple banner with blink effect
3. Simple banner without color
4. Minimal banner

### Test with Commands

```bash
# See banner with hash identification
python hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332"

# See banner with help
python hash_identifier.py -h

# See banner with info
python hash_identifier.py --info

# See banner with batch processing
python hash_identifier.py -f hashes.txt
```

---

## Performance Impact

✅ **Minimal Performance Impact**
- Banner renders in ~10-50ms
- Uses simple ANSI codes (no heavy processing)
- Color detection happens once per run
- No external dependencies

---

## Compatibility Matrix

| Platform | Color Support | Unicode | Status |
|----------|---------------|---------|--------|
| Windows PowerShell | Yes | ASCII-safe | ✅ Full |
| Windows CMD | Yes | ASCII-safe | ✅ Full |
| Linux Terminal | Yes | Full | ✅ Full |
| macOS Terminal | Yes | Full | ✅ Full |
| SSH/Remote | Conditional | ASCII-safe | ✅ Fallback |
| Piped Output | No | Yes | ✅ Graceful |

---

## Example Outputs

### Example 1: Hash Identification
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
    ...
```

### Example 2: Help Display
```bash
$ python hash_identifier.py -h

    +============================+
    |      H x M o d v1.0        |
    |                            |
    | Hash Identification Tool   |
    | Created by MD.SHORIF MIA   |
    +============================+


usage: HxMod [-h] [--version] ...
HxMod v1.0 - Identify hash types and find hashcat modes (Offline)
...
```

---

## Future Enhancement Ideas

💡 **Possible Additions:**
1. Configurable banner display (enable/disable flag)
2. Custom banner text via config file
3. More animation styles (scroll, fade, etc.)
4. Thematic banners (hacker, minimal, full, etc.)
5. ASCII art variants

---

## Banner Library API

### Public Functions

#### `show_banner(style='simple', effect='color', show_once=False)`

Display the banner with specified style and effect.

**Parameters:**
- `style` (str): Banner style - 'simple', 'complex', or 'minimal'
- `effect` (str): Effect type - 'color', 'blink', or 'none'
- `show_once` (bool): Print banner only once

**Returns:**
- `bool`: True if banner was displayed

**Example:**
```python
from lib.banner import show_banner

# Show simple colored banner
show_banner(style='simple', effect='color')

# Show minimal banner without colors
show_banner(style='minimal', effect='none')

# Show with blinking effect
show_banner(style='simple', effect='blink')
```

### Class: BannerPrinter

**Methods:**
- `print_colored_banner()` - Print colored banner
- `print_banner_with_blink()` - Print with blinking effect
- `colorize_text()` - Apply color to text

### Class: Colors

**ANSI Color Constants:**
- `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`
- `BRIGHT_RED`, `BRIGHT_GREEN`, `BRIGHT_BLUE`
- `BOLD`, `DIM`, `BLINK`, `RESET`

---

## Summary

✅ **What's Implemented:**
- Professional ASCII banner with creator attribution
- Automatic color detection and fallback
- Cross-platform compatibility (Windows, Linux, macOS)
- Multiple banner styles and effects
- Zero impact on performance
- Clean integration with main application

✅ **User Experience:**
- Professional first impression when tool starts
- Clear branding and creator attribution  
- Works seamlessly across all commands
- Graceful fallback for non-color environments

---

**Banner Module Version:** 1.0  
**Created for:** HxMod v1.0  
**Created by:** MD.SHORIF MIA  
**Date:** February 2, 2026
