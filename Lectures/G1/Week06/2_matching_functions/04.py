# matching functions
# match - finds the first match according to regex
# fullmatch - return a match only if the whole string matches a given regex
# findall - find all matches and returns a list of strings
# finditer - find all matches and returns an iterator with match objects

import re

text_to_match = """
John's email is john.doe@example.com
Hello John
"""

pattern = r'\w+'

result = re.finditer(pattern, text_to_match) 
# result contains an iterator with match objects

for match in result:
    print(match) # match object
