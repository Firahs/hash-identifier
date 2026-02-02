#!/usr/bin/env python3
"""
HxMod v1.0 - Offline CLI Tool for Hash Type Identification
Identifies hash types and returns corresponding hashcat modes
Created by: MD.SHORIF MIA
"""

import argparse
import sys
import os
from pathlib import Path

# Add lib directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from lib.hash_analyzer import HashAnalyzer
from lib.formatter import OutputFormatter, BatchResultFormatter, get_formatter
from lib.banner import show_banner


class HashIdentifierCLI:
    """Command-line interface for HxMod v1.0 - Created by MD.SHORIF MIA"""
    
    APP_NAME = "HxMod"
    VERSION = "v1.0"
    AUTHOR = "MD.SHORIF MIA"
    
    def __init__(self):
        self.analyzer = HashAnalyzer()
        self.parser = self._create_parser()
    
    def _create_parser(self) -> argparse.ArgumentParser:
        """Create argument parser"""
        parser = argparse.ArgumentParser(
            prog='HxMod',
            description='HxMod v1.0 - Identify hash types and find hashcat modes (Offline)',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  # Identify a single hash
  python hash_identifier.py "8846f7eaee8fb117ad06bdd810b7e332"
  
  # Identify from file (one hash per line)
  python hash_identifier.py -f hashes.txt
  
  # Output as JSON
  python hash_identifier.py -f hashes.txt -o json
  
  # Search hashcat modes
  python hash_identifier.py --search "bcrypt"
  
  # List all hash categories
  python hash_identifier.py --categories
  
  # Get database info
  python hash_identifier.py --info

Created by: MD.SHORIF MIA | Version: v1.0
            """
        )
        
        parser.add_argument(
            '--version',
            action='version',
            version='HxMod v1.0 by MD.SHORIF MIA'
        )
        
        # Input options
        input_group = parser.add_mutually_exclusive_group()
        input_group.add_argument('hash', nargs='?', help='Hash string to identify')
        input_group.add_argument('-f', '--file', help='Read hashes from file (one per line)')
        input_group.add_argument('--search', help='Search hashcat modes by name')
        input_group.add_argument('--mode', type=int, help='Get details for specific hashcat mode number')
        input_group.add_argument('--categories', action='store_true', help='List all hash categories')
        input_group.add_argument('--info', action='store_true', help='Show database information')
        input_group.add_argument('--list', help='List modes in a category')
        
        # Output format options
        parser.add_argument('-o', '--output', 
                          choices=['standard', 'table', 'detailed', 'json', 'json_compact', 'csv', 'compact', 'hashcat', 'brief'],
                          default='standard',
                          help='Output format (default: standard)')
        
        # Other options
        parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output with extra details')
        parser.add_argument('--features', action='store_true', help='Show hash feature analysis')
        parser.add_argument('--save', help='Save results to file')
        
        return parser
    
    def run(self):
        """Main entry point"""
        args = self.parser.parse_args()
        
        try:
            if args.categories:
                self._show_categories()
            elif args.info:
                self._show_info()
            elif args.search:
                self._search_modes(args.search)
            elif args.mode is not None:
                self._show_mode_details(args.mode)
            elif args.list:
                self._list_category_modes(args.list)
            elif args.file:
                self._process_file(args.file, args.output, args.save)
            elif args.hash:
                self._process_single_hash(args.hash, args.output, args.features, args.save)
            else:
                self.parser.print_help()
        
        except KeyboardInterrupt:
            print("\n\nInterrupted by user")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    def interactive_mode(self):
        """Interactive mode - HASH: prompt"""
        print("=" * 70)
        print("Interactive Mode - Type 'help' for commands, 'quit' to exit")
        print("=" * 70)
        print()
        
        while True:
            try:
                # Show prompt
                user_input = input("\033[92mHASH:\033[0m ").strip()
                
                if not user_input:
                    continue
                
                # Check for special commands
                if user_input.lower() == 'quit' or user_input.lower() == 'exit':
                    print("\nGoodbye! 👋")
                    break
                
                elif user_input.lower() == 'help':
                    print("""
Commands:
  help                 - Show this help
  quit/exit            - Exit HxMod
  clear                - Clear screen
  info                 - Show database info
  categories           - List all categories
  search <name>        - Search hash modes
  
Just type a hash to identify it!
Examples:
  8846f7eaee8fb117ad06bdd810b7e332        (MD5/NTLM)
  $2a$12$...                               (bcrypt)
  $argon2id$v=19$...                       (Argon2)
                    """)
                
                elif user_input.lower() == 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    show_banner(style='hacker', use_color=True)
                    print()
                
                elif user_input.lower() == 'info':
                    self._show_info()
                
                elif user_input.lower() == 'categories':
                    self._show_categories()
                
                elif user_input.lower().startswith('search '):
                    query = user_input[7:].strip()
                    if query:
                        self._search_modes(query)
                
                else:
                    # Treat as hash
                    self._process_single_hash(user_input, 'standard', show_features=False)
                
                print()  # Add spacing
            
            except KeyboardInterrupt:
                print("\n\nGoodbye! 👋")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def _process_single_hash(self, hash_input: str, output_format: str, show_features: bool = False, save_path: str = None):
        """Process and display single hash identification"""
        result = self.analyzer.identify_hash(hash_input)
        
        # Add features if requested
        if show_features:
            result['features'] = self.analyzer.analyze_hash_features(hash_input)
        
        formatter = get_formatter(output_format)
        formatted_output = formatter(result)
        
        print(formatted_output)
        
        if save_path:
            with open(save_path, 'w') as f:
                f.write(formatted_output)
            print(f"\nResults saved to {save_path}")
    
    def _process_file(self, file_path: str, output_format: str, save_path: str = None):
        """Process multiple hashes from file"""
        try:
            with open(file_path, 'r') as f:
                hashes = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found", file=sys.stderr)
            sys.exit(1)
        
        if not hashes:
            print("No hashes found in file", file=sys.stderr)
            sys.exit(1)
        
        print(f"Processing {len(hashes)} hashes...\n")
        
        results = self.analyzer.identify_multiple(hashes)
        
        if output_format in ['json', 'json_compact']:
            formatter = get_formatter(output_format)
            output = formatter(results)
        elif output_format == 'csv':
            output = BatchResultFormatter.format_csv_batch(results)
        else:
            # Show summary and detailed results
            output = BatchResultFormatter.format_summary(results)
            output += "\n" + BatchResultFormatter.format_detailed_batch(results)
        
        print(output)
        
        if save_path:
            with open(save_path, 'w') as f:
                f.write(output)
            print(f"\nResults saved to {save_path}")
    
    def _search_modes(self, query: str):
        """Search hashcat modes"""
        results = self.analyzer.search_by_name(query)
        
        if not results:
            print(f"No modes found matching '{query}'")
            return
        
        print(f"\nSearch Results for '{query}':")
        print("=" * 80)
        print(f"{'Mode':<8} {'Hash Type':<30} {'Category':<30}")
        print("-" * 80)
        
        for mode in results:
            print(f"{mode['mode']:<8} {mode['name']:<30} {mode['category']:<30}")
        
        print("=" * 80)
    
    def _show_mode_details(self, mode_num: int):
        """Show detailed information for a specific mode"""
        mode = self.analyzer.get_mode_details(mode_num)
        
        if not mode:
            print(f"Mode {mode_num} not found")
            return
        
        print(f"\n{'='*80}")
        print(f"Mode {mode_num}: {mode['name']}")
        print(f"{'='*80}")
        print(f"Category: {mode['category']}")
        print(f"Description: {mode['description']}")
        print(f"Salt Type: {mode.get('salt_type', 'N/A')}")
        print(f"Iterations: {mode.get('iterations', 'N/A')}")
        print(f"Example: {mode.get('example', 'N/A')}")
        
        if mode.get('variants'):
            print(f"Variants: {', '.join(mode['variants'])}")
        
        print(f"{'='*80}\n")
    
    def _show_categories(self):
        """List all hash categories"""
        categories = self.analyzer.list_categories()
        
        print("\nAvailable Hash Categories:")
        print("=" * 60)
        
        for idx, cat in enumerate(categories, 1):
            modes = self.analyzer.get_category_modes(cat)
            print(f"{idx:2}. {cat:<40} ({len(modes)} modes)")
        
        print("=" * 60)
        print(f"\nTotal Categories: {len(categories)}")
        print("Use: python hash_identifier.py --list '<category_name>' to see modes")
    
    def _show_info(self):
        """Show database information"""
        info = self.analyzer.get_database_info()
        
        print("\n" + "=" * 70)
        print("HXMOD DATABASE INFORMATION")
        print("=" * 70)
        print(f"Tool: {info.get('tool_name', 'HxMod')}")
        print(f"Version: {info.get('tool_version', 'v1.0')}")
        print(f"Created by: {info.get('created_by', 'MD.SHORIF MIA')}")
        print(f"Hashcat Version: {info.get('hashcat_version', '7.0.0')}")
        print(f"Source: {info.get('source', 'https://hashcat.net/wiki/')}")
        print(f"Last Updated: {info.get('last_updated', '2026-02-02')}")
        print(f"Total Hash Modes: {info.get('total_modes', '450')}")
        print(f"Total Categories: {info['total_categories']}")
        print("=" * 70 + "\n")
    
    def _list_category_modes(self, category: str):
        """List modes in a specific category"""
        modes = self.analyzer.get_category_modes(category)
        
        if not modes:
            print(f"Category '{category}' not found or has no modes")
            return
        
        print(f"\nModes in '{category}' ({len(modes)} total):")
        print("=" * 90)
        print(f"{'Mode':<8} {'Hash Type':<30} {'Description':<50}")
        print("-" * 90)
        
        for mode in modes:
            desc = mode['description'][:48]
            print(f"{mode['mode']:<8} {mode['name']:<30} {desc:<50}")
        
        print("=" * 90 + "\n")


def main():
    """Main entry point"""
    # Display banner when tool starts
    show_banner(style='hacker', use_color=True)
    print()  # Add spacing after banner
    
    cli = HashIdentifierCLI()
    
    # Check if arguments provided
    if len(sys.argv) > 1:
        # CLI mode - process arguments
        cli.run()
    else:
        # Interactive mode - show prompt
        cli.interactive_mode()


if __name__ == '__main__':
    main()
