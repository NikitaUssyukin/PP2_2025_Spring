# Metacharacters
# . ^ $ * + ? { } [ ] \ | ( )
# . - any symbol 
# ^ - matches at the beginning
# $ - matches at the end
# * - quantifier, 0 or more repetitions
# + - quantifier, 1 or more repetitions

import re

txt_file = '../test.txt'

with open(txt_file, 'r') as file:
    text_to_match = file.read()

# print(text_to_match)

pattern = '[A-Z]\\w+' # matching names
# \\ escapes a backslash, such that python does not expect any escape characters
# such as \n

result = re.match(pattern, text_to_match)

print(result)
print(result.group(0))

