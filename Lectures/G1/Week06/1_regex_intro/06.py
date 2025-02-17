# Metacharacters
# . ^ $ * + ? { } [ ] \ | ( )
# . - any symbol 
# ^ - matches at the beginning
# $ - matches at the end
# * - quantifier, 0 or more repetitions
# + - quantifier, 1 or more repetitions
# ? - quantifier, 0 or 1 repetitions
# {} - quantifier, allows to specify the exact amount of repetitions
# [] - set of characters
# \ - backslash, used for special sequences or escaping character
# | - or, allows to check for 2 or more patterns
# () - grouping

import re

txt_file = '../test.txt'

with open(txt_file, 'r') as file:
    text_to_match = file.read()

# print(text_to_match)

pattern = r'[A-Z]\w+' # matching names
# raw string - no need to escape a backslash

result = re.match(pattern, text_to_match)

print(result)
print(result.group(0))

