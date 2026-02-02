"""
Hash Analyzer Module
Core logic for hash identification and analysis
Integrates pattern matching with hashcat modes database
"""

import json
import os
import re
from typing import Dict, List, Optional
from lib.hash_patterns import HashPatterns


class HashcatModeManager:
    """Manages hashcat modes database and lookups"""
    
    def __init__(self, db_path: str = "database/hashcat_modes.json"):
        self.db_path = db_path
        self.modes_data = self._load_database()
        self._build_indexes()
    
    def _load_database(self) -> Dict:
        """Load hashcat modes database"""
        try:
            with open(self.db_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Database not found at {self.db_path}")
            return {"hash_modes": [], "metadata": {}}
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in database")
            return {"hash_modes": [], "metadata": {}}
    
    def _build_indexes(self):
        """Build fast lookup indexes"""
        self.mode_by_number = {}
        self.modes_by_category = {}
        self.modes_by_name = {}
        
        for mode in self.modes_data.get("hash_modes", []):
            # Index by mode number
            self.mode_by_number[mode["mode"]] = mode
            
            # Index by name (case-insensitive)
            self.modes_by_name[mode["name"].lower()] = mode
            
            # Index by category
            cat = mode.get("category", "Unknown")
            if cat not in self.modes_by_category:
                self.modes_by_category[cat] = []
            self.modes_by_category[cat].append(mode)
    
    def get_mode_by_number(self, mode_num: int) -> Optional[Dict]:
        """Get hash mode by hashcat mode number"""
        return self.mode_by_number.get(mode_num)
    
    def get_mode_by_name(self, name: str) -> Optional[Dict]:
        """Get hash mode by name"""
        return self.modes_by_name.get(name.lower())
    
    def get_modes_by_category(self, category: str) -> List[Dict]:
        """Get all modes in a category"""
        return self.modes_by_category.get(category, [])
    
    def search_modes(self, query: str) -> List[Dict]:
        """Search modes by name or description"""
        results = []
        query_lower = query.lower()
        
        for mode in self.modes_data.get("hash_modes", []):
            if (query_lower in mode["name"].lower() or 
                query_lower in mode.get("description", "").lower()):
                results.append(mode)
        
        return results
    
    def get_all_categories(self) -> List[str]:
        """Get all available categories"""
        return sorted(self.modes_by_category.keys())
    
    def get_metadata(self) -> Dict:
        """Get database metadata"""
        return self.modes_data.get("metadata", {})


class HashAnalyzer:
    """Main hash analyzer class"""
    
    def __init__(self, hashcat_db_path: str = "database/hashcat_modes.json"):
        self.hashcat_mgr = HashcatModeManager(hashcat_db_path)
        self.patterns = HashPatterns()
    
    def identify_hash(self, hash_input: str) -> Dict:
        """
        Identify hash and return comprehensive analysis
        
        Args:
            hash_input: The hash string to identify
            
        Returns:
            Dictionary containing identification results
        """
        hash_input = hash_input.strip()
        
        # Step 1: Match against regex patterns
        pattern_matches = self.patterns.identify_by_pattern(hash_input)
        
        # Step 2: Try to find corresponding hashcat modes
        results = {
            'input_hash': hash_input[:50] + ('...' if len(hash_input) > 50 else ''),
            'hash_length': len(hash_input),
            'matches': [],
            'confidence': 'Unknown'
        }
        
        seen_modes = set()
        
        for hash_type, description, confidence in pattern_matches:
            # Search for matching hashcat mode
            mode_info = self.hashcat_mgr.get_mode_by_name(hash_type)
            
            if mode_info:
                match_entry = {
                    'hash_type': mode_info['name'],
                    'hashcat_mode': mode_info['mode'],
                    'category': mode_info['category'],
                    'description': mode_info['description'],
                    'confidence': confidence,
                    'salt_type': mode_info.get('salt_type', 'unknown'),
                    'example': mode_info.get('example', 'N/A'),
                    'variants': mode_info.get('variants', [])
                }
                
                # Avoid duplicates
                mode_key = (mode_info['mode'], mode_info['name'])
                if mode_key not in seen_modes:
                    results['matches'].append(match_entry)
                    seen_modes.add(mode_key)
        
        # Sort matches by confidence (highest first)
        results['matches'].sort(key=lambda x: x['confidence'], reverse=True)
        
        # Set overall confidence
        if results['matches']:
            results['confidence'] = results['matches'][0]['confidence']
        
        return results
    
    def identify_multiple(self, hashes: List[str]) -> List[Dict]:
        """
        Identify multiple hashes at once
        
        Args:
            hashes: List of hash strings
            
        Returns:
            List of identification results
        """
        return [self.identify_hash(h) for h in hashes]
    
    def get_mode_details(self, mode_number: int) -> Optional[Dict]:
        """Get detailed information about a specific hashcat mode"""
        return self.hashcat_mgr.get_mode_by_number(mode_number)
    
    def search_by_mode_number(self, mode_num: int) -> Optional[Dict]:
        """Search hashcat database by mode number"""
        return self.hashcat_mgr.get_mode_by_number(mode_num)
    
    def search_by_name(self, name: str) -> List[Dict]:
        """Search hashcat database by hash name"""
        return self.hashcat_mgr.search_modes(name)
    
    def get_category_modes(self, category: str) -> List[Dict]:
        """Get all modes in a specific category"""
        return self.hashcat_mgr.get_modes_by_category(category)
    
    def list_categories(self) -> List[str]:
        """List all available hash categories"""
        return self.hashcat_mgr.get_all_categories()
    
    def list_modes(self, category: Optional[str] = None) -> List[Dict]:
        """
        List all modes, optionally filtered by category
        
        Args:
            category: Optional category filter
            
        Returns:
            List of hash modes
        """
        if category:
            return self.hashcat_mgr.get_modes_by_category(category)
        
        return self.hashcat_mgr.modes_data.get("hash_modes", [])
    
    def get_database_info(self) -> Dict:
        """Get information about the hashcat database"""
        metadata = self.hashcat_mgr.get_metadata()
        categories = self.hashcat_mgr.get_all_categories()
        total_modes = len(self.hashcat_mgr.modes_data.get("hash_modes", []))
        
        return {
            'version': metadata.get('version', 'Unknown'),
            'source': metadata.get('source', 'Unknown'),
            'last_updated': metadata.get('last_updated', 'Unknown'),
            'total_modes': total_modes,
            'total_categories': len(categories),
            'categories': categories
        }
    
    def analyze_hash_features(self, hash_input: str) -> Dict:
        """
        Analyze specific features of a hash
        
        Args:
            hash_input: The hash string to analyze
            
        Returns:
            Dictionary with feature analysis
        """
        hash_input = hash_input.strip()
        
        features = {
            'length': len(hash_input),
            'is_hex': bool(re.match(r'^[a-f0-9]*$', hash_input, re.IGNORECASE)),
            'is_base64': bool(re.match(r'^[A-Za-z0-9+/]*={0,2}$', hash_input)),
            'contains_delimiter': ':' in hash_input or '#' in hash_input or '$' in hash_input,
            'delimiter_chars': list(set([c for c in hash_input if c in ':$#'])),
            'has_prefix': any(hash_input.startswith(p) for p in ['$', '*', '$1$', '$2$', '$5$', '$6$']),
            'prefix': None,
            'case_sensitive': not hash_input.islower() and not hash_input.isupper(),
        }
        
        # Identify prefix
        for prefix in ['$1$', '$2a$', '$2b$', '$2y$', '$5$', '$6$', '$7z$', '$pbkdf2', '$scrypt', '$argon2']:
            if hash_input.startswith(prefix):
                features['prefix'] = prefix
                break
        
        if hash_input.startswith('*'):
            features['prefix'] = '*'
        
        return features
