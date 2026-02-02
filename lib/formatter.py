"""
Output Formatter Module
Formats hash identification results for CLI display
"""

import json
from typing import Dict, List
from datetime import datetime


class OutputFormatter:
    """Formats output in various styles"""
    
    @staticmethod
    def format_standard(result: Dict) -> str:
        """Format result in standard readable format"""
        output = []
        output.append("=" * 70)
        output.append(f"Hash Length: {result['hash_length']} characters")
        output.append(f"Overall Confidence: {result['confidence']}%")
        output.append("=" * 70)
        
        if not result['matches']:
            output.append("No matches found.")
            return "\n".join(output)
        
        for idx, match in enumerate(result['matches'], 1):
            output.append(f"\n[{idx}] {match['hash_type']}")
            output.append(f"    Hashcat Mode: {match['hashcat_mode']}")
            output.append(f"    Category: {match['category']}")
            output.append(f"    Description: {match['description']}")
            output.append(f"    Confidence: {match['confidence']}%")
            output.append(f"    Salt Type: {match['salt_type']}")
            if match['variants']:
                output.append(f"    Variants: {', '.join(match['variants'])}")
        
        return "\n".join(output)
    
    @staticmethod
    def format_table(result: Dict) -> str:
        """Format result in table format"""
        if not result['matches']:
            return "No matches found."
        
        output = []
        output.append("\nHash Identification Results")
        output.append("=" * 100)
        
        # Header
        header = f"{'#':<3} {'Hash Type':<25} {'Mode':<8} {'Category':<25} {'Confidence':<12}"
        output.append(header)
        output.append("-" * 100)
        
        # Rows
        for idx, match in enumerate(result['matches'], 1):
            row = f"{idx:<3} {match['hash_type']:<25} {match['hashcat_mode']:<8} {match['category']:<25} {match['confidence']}%"
            output.append(row)
        
        output.append("=" * 100)
        return "\n".join(output)
    
    @staticmethod
    def format_detailed(result: Dict) -> str:
        """Format result with detailed information"""
        output = []
        output.append("\n" + "=" * 80)
        output.append("DETAILED HASH IDENTIFICATION RESULTS")
        output.append("=" * 80)
        output.append(f"\nInput Hash (first 100 chars): {result['input_hash']}")
        output.append(f"Hash Length: {result['hash_length']} characters")
        output.append(f"Overall Confidence: {result['confidence']}%")
        output.append(f"Matches Found: {len(result['matches'])}")
        
        if not result['matches']:
            output.append("\nNo matches found.")
            return "\n".join(output)
        
        output.append("\n" + "-" * 80)
        
        for idx, match in enumerate(result['matches'], 1):
            output.append(f"\n[Match #{idx}]")
            output.append(f"  Hash Type:        {match['hash_type']}")
            output.append(f"  Hashcat Mode:     {match['hashcat_mode']}")
            output.append(f"  Category:         {match['category']}")
            output.append(f"  Description:      {match['description']}")
            output.append(f"  Confidence Level: {match['confidence']}%")
            output.append(f"  Salt Type:        {match['salt_type']}")
            output.append(f"  Example Hash:     {match['example']}")
            if match['variants']:
                output.append(f"  Variants:         {', '.join(match['variants'])}")
        
        output.append("\n" + "=" * 80)
        return "\n".join(output)
    
    @staticmethod
    def format_json(result: Dict) -> str:
        """Format result as JSON"""
        return json.dumps(result, indent=2)
    
    @staticmethod
    def format_json_compact(result: Dict) -> str:
        """Format result as compact JSON"""
        return json.dumps(result, separators=(',', ':'))
    
    @staticmethod
    def format_csv(result: Dict) -> str:
        """Format result as CSV"""
        if not result['matches']:
            return "hash_type,hashcat_mode,category,confidence,salt_type"
        
        lines = ["hash_type,hashcat_mode,category,confidence,salt_type"]
        for match in result['matches']:
            line = f"\"{match['hash_type']}\",{match['hashcat_mode']},\"{match['category']}\",{match['confidence']},{match['salt_type']}"
            lines.append(line)
        
        return "\n".join(lines)
    
    @staticmethod
    def format_compact(result: Dict) -> str:
        """Format result in compact single-line format"""
        if not result['matches']:
            return "No matches found"
        
        matches_str = " | ".join([
            f"{m['hash_type']} (Mode: {m['hashcat_mode']}, Conf: {m['confidence']}%)"
            for m in result['matches'][:3]
        ])
        
        if len(result['matches']) > 3:
            matches_str += f" | ... and {len(result['matches']) - 3} more"
        
        return matches_str
    
    @staticmethod
    def format_unix_hashcat(result: Dict) -> str:
        """Format as hashcat command suggestions"""
        output = []
        output.append("\nHashcat Command Suggestions:")
        output.append("=" * 70)
        
        if not result['matches']:
            output.append("No matches found.")
            return "\n".join(output)
        
        for idx, match in enumerate(result['matches'][:5], 1):
            output.append(f"\n[{idx}] {match['hash_type']} (Mode {match['hashcat_mode']})")
            output.append(f"    hashcat -m {match['hashcat_mode']} -a 0 <hash_file> <wordlist>")
            output.append(f"    hashcat -m {match['hashcat_mode']} -a 3 <hash_file> ?a?a?a?a")
        
        if len(result['matches']) > 5:
            output.append(f"\n... and {len(result['matches']) - 5} more modes available")
        
        return "\n".join(output)
    
    @staticmethod
    def format_brief(result: Dict) -> str:
        """Format result in brief format"""
        if not result['matches']:
            return "No matches found"
        
        top_match = result['matches'][0]
        return f"{top_match['hash_type']} (Mode: {top_match['hashcat_mode']}, Confidence: {top_match['confidence']}%)"


class BatchResultFormatter:
    """Format results from multiple hashes"""
    
    @staticmethod
    def format_summary(results: List[Dict]) -> str:
        """Format summary of multiple hash identifications"""
        output = []
        output.append("\n" + "=" * 80)
        output.append("BATCH HASH IDENTIFICATION SUMMARY")
        output.append("=" * 80)
        output.append(f"Total Hashes Analyzed: {len(results)}")
        output.append(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        output.append("=" * 80)
        
        for idx, result in enumerate(results, 1):
            output.append(f"\n[Hash #{idx}]")
            output.append(f"  Length: {result['hash_length']} chars")
            if result['matches']:
                top_match = result['matches'][0]
                output.append(f"  Top Match: {top_match['hash_type']} (Mode: {top_match['hashcat_mode']})")
                output.append(f"  Confidence: {top_match['confidence']}%")
            else:
                output.append(f"  Result: No matches found")
        
        output.append("\n" + "=" * 80)
        return "\n".join(output)
    
    @staticmethod
    def format_detailed_batch(results: List[Dict]) -> str:
        """Format detailed results for multiple hashes"""
        output = []
        output.append("\n" + "=" * 100)
        output.append("DETAILED BATCH RESULTS")
        output.append("=" * 100)
        
        for idx, result in enumerate(results, 1):
            output.append(f"\n--- Hash #{idx} ---")
            output.append(f"Length: {result['hash_length']}")
            
            if result['matches']:
                output.append(f"Matches ({len(result['matches'])} total):")
                for jdx, match in enumerate(result['matches'][:3], 1):
                    output.append(f"  {jdx}. {match['hash_type']} - Mode: {match['hashcat_mode']} - Confidence: {match['confidence']}%")
                if len(result['matches']) > 3:
                    output.append(f"  ... and {len(result['matches']) - 3} more")
            else:
                output.append("No matches found")
        
        output.append("\n" + "=" * 100)
        return "\n".join(output)
    
    @staticmethod
    def format_json_batch(results: List[Dict]) -> str:
        """Format batch results as JSON"""
        return json.dumps(results, indent=2)
    
    @staticmethod
    def format_csv_batch(results: List[Dict]) -> str:
        """Format batch results as CSV"""
        lines = ["hash_number,hash_length,top_match,mode,confidence,total_matches"]
        
        for idx, result in enumerate(results, 1):
            if result['matches']:
                top = result['matches'][0]
                line = f"{idx},{result['hash_length']},\"{top['hash_type']}\",{top['hashcat_mode']},{top['confidence']},{len(result['matches'])}"
            else:
                line = f"{idx},{result['hash_length']},No match,N/A,0,0"
            lines.append(line)
        
        return "\n".join(lines)


def get_formatter(format_type: str):
    """Get formatter instance based on format type"""
    formatters = {
        'standard': OutputFormatter.format_standard,
        'table': OutputFormatter.format_table,
        'detailed': OutputFormatter.format_detailed,
        'json': OutputFormatter.format_json,
        'json_compact': OutputFormatter.format_json_compact,
        'csv': OutputFormatter.format_csv,
        'compact': OutputFormatter.format_compact,
        'hashcat': OutputFormatter.format_unix_hashcat,
        'brief': OutputFormatter.format_brief,
    }
    return formatters.get(format_type, OutputFormatter.format_standard)
