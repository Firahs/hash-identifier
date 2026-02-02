from lib.hash_analyzer import HashAnalyzer

analyzer = HashAnalyzer()
test_hash = '*81F5E21E35407D884A6CD4A731AEBFB6AF209E1B'

result = analyzer.identify_hash(test_hash)
print("Result:")
for match in result['matches']:
    print(match)
