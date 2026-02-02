from lib.hash_patterns import HashPatterns

patterns = HashPatterns()
test_hash = '*81F5E21E35407D884A6CD4A731AEBFB6AF209E1B'

# Check if MySQL4.1+ pattern exists
if 'MySQL4.1+' in patterns.PATTERNS:
    mysql_info = patterns.PATTERNS['MySQL4.1+']
    print(f'Pattern found for MySQL4.1+')
    print(f'Pattern: {mysql_info["pattern"]}')
    
    # Now try to identify
    matches = patterns.identify_by_pattern(test_hash)
    print(f'Matches: {matches}')
else:
    print('MySQL4.1+ pattern not found')
