"""
HxMod Banner - ASCII Art Banner with Color Effects
Created by: MD.SHORIF MIA
"""

import sys
import time


class Colors:
    """ANSI Color codes for terminal output"""
    # Regular Colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Bright Colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_BLUE = '\033[94m'
    
    # Effects
    BOLD = '\033[1m'
    DIM = '\033[2m'
    BLINK = '\033[5m'
    
    # Reset
    RESET = '\033[0m'
    
    @staticmethod
    def supports_color():
        """Check if terminal supports color"""
        if not hasattr(sys.stdout, "isatty"):
            return False
        if not sys.stdout.isatty():
            return False
        return True


class BannerPrinter:
    """Print ASCII banner with color effects"""
    
    # Hacker style banner - Custom ASCII art (using raw string to avoid escape issues)
    HACKER_BANNER = r"""
    
    #                                                              
    )          *         (      
 ( /(        (  `        )\ )   
 )\())    )  )\))(      (()/(   
((_)\  ( /( ((_)()\   (  /(_))  
 _((_) )\())(_()((_)  )\(_))_   
| || |((_)\ |  \/  | ((_)|   \  
| __ |\ \ / | |\/| |/ _ \| |) | 
|_||_|/_\_\ |_|  |_|\___/|___/                                                                                         
         
            v1.0 - Hash Identification Tool       #
                 By MD.SHORIF MIA                #
         #       www.firahs.github.io           #
        #        sa21iu.cse@gmail.com          #                                        
       ========================================
    """
    
    # Simpler banner with color code theme
    SIMPLE_BANNER = """
    +============================+
    |      H x M o d v1.0        |
    |                            |
    | Hash Identification Tool   |
    | Created by MD.SHORIF MIA   |
    +============================+
    """
    
    # Minimal banner
    MINIMAL_BANNER = """
    HxMod v1.0 - Hash Identifier
    Created by MD.SHORIF MIA
    """
    
    @staticmethod
    def colorize_text(text, color):
        """Apply color to text"""
        if not Colors.supports_color():
            return text
        return f"{color}{text}{Colors.RESET}"
    
    @staticmethod
    def print_colored_banner(use_hacker=True, use_color=True):
        """
        Print banner with colors
        
        Args:
            use_hacker: Use hacker style banner
            use_color: Enable color output
        """
        if not use_color or not Colors.supports_color():
            use_color = False
        
        if use_hacker:
            banner = BannerPrinter.HACKER_BANNER
        else:
            banner = BannerPrinter.SIMPLE_BANNER
        
        if not use_color:
            print(banner)
            return
        
        BannerPrinter._print_static_banner(banner)
    
    @staticmethod
    def _print_static_banner(banner):
        """Print static colored banner (no animation)"""
        lines = banner.split('\n')
        
        colors = [Colors.GREEN, Colors.GREEN, Colors.BRIGHT_GREEN, 
                 Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.BRIGHT_GREEN,
                 Colors.GREEN, Colors.GREEN, Colors.GREEN]
        
        for i, line in enumerate(lines):
            if line.strip():
                # Get color for this line
                color = colors[i % len(colors)]
                # Colorize the line
                colored_line = BannerPrinter.colorize_text(line, color)
                print(colored_line)
            else:
                print(line)


def show_banner(style='hacker', use_color=True):
    """
    Convenience function to show banner
    
    Args:
        style: 'hacker' or 'simple'
        use_color: Enable colors
    
    Returns:
        True if banner was shown
    """
    if style == 'simple':
        BannerPrinter.print_colored_banner(use_hacker=False, use_color=use_color)
    else:  # hacker
        BannerPrinter.print_colored_banner(use_hacker=True, use_color=use_color)
    
    return True


if __name__ == "__main__":
    print("=" * 70)
    print("Testing Banner Styles")
    print("=" * 70)
    
    print("\n1. Hacker Banner with Color:")
    print("-" * 70)
    show_banner(style='hacker', use_color=True)
    
    print("\n2. Simple Banner with Color:")
    print("-" * 70)
    show_banner(style='simple', use_color=True)
