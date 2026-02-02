#!/bin/bash

# HxMod v1.0 Installation Script for Linux
# Created by: MD.SHORIF MIA
# This script sets up the hash identifier tool for use on Linux systems

set -e  # Exit on error

echo "=========================================="
echo "HxMod v1.0 - Installation Script"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3.6 or later and try again."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✓ Python 3 found: $PYTHON_VERSION"

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "✓ Installation directory: $SCRIPT_DIR"

# Install optional dependencies
echo ""
echo "Installing optional dependencies..."
if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
    pip3 install -q -r "$SCRIPT_DIR/requirements.txt" 2>/dev/null || echo "  (Optional dependencies installation skipped)"
fi

# Make the main script executable
chmod +x "$SCRIPT_DIR/hash_identifier.py"
chmod +x "$SCRIPT_DIR/hxmod"
echo "✓ Made hash_identifier.py executable"
echo "✓ Made hxmod executable"

# Create symlink in common location (optional)
if [ -d "/usr/local/bin" ]; then
    echo ""
    echo "Would you like to create a symlink in /usr/local/bin? (y/n)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        sudo ln -sf "$SCRIPT_DIR/hxmod" /usr/local/bin/hxmod
        echo "✓ Created symlink: /usr/local/bin/hxmod"
        echo "  You can now run: hxmod <hash>"
    fi
fi

# Verify database exists
if [ ! -f "$SCRIPT_DIR/database/hashcat_modes.json" ]; then
    echo ""
    echo "Warning: Hashcat modes database not found!"
    echo "Expected at: $SCRIPT_DIR/database/hashcat_modes.json"
    exit 1
fi
echo "✓ Database verified: database/hashcat_modes.json"

# Test the installation
echo ""
echo "Testing installation..."
cd "$SCRIPT_DIR"
python3 hash_identifier.py -h > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Installation test passed"
else
    echo "✗ Installation test failed"
    exit 1
fi

echo ""
echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo ""
echo "Usage:"
echo "  # Quick command (if symlink installed)"
echo "  hxmod \"8846f7eaee8fb117ad06bdd810b7e332\""
echo ""
echo "  # Direct Python execution"
echo "  python3 hash_identifier.py \"8846f7eaee8fb117ad06bdd810b7e332\""
echo ""
echo "  # Identify from file"
echo "  python3 hash_identifier.py -f hashes.txt"
echo ""
echo "  # Show help"
echo "  python3 hash_identifier.py -h"
echo ""
echo "For more examples, see README.md"
echo ""
