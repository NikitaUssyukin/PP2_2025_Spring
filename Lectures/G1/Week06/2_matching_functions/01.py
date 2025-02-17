# matching functions
# match - finds the first match according to regex
# fullmatch - return a match only if the whole string matches a given regex
# findall - find all matches and returns a list of strings
# finditer - find all matches and returns an iterator with match objects

import re

text_to_match = "John's email is john.doe@example.com"

pattern = r'[A-Z]\w+'
# raw string - no need to escape a backslash

result = re.match(pattern, text_to_match) # returns the first match
# that starts from the beginning of the string

print(result)
print(result.group(0)) # ok

pattern = r'[a-z]\w+'
# raw string - no need to escape a backslash

result = re.match(pattern, text_to_match) # returns None
# because match() matches only at the beginning of the string

print(result)
print(result.group(0)) # error - not a match object