# metacharacters
# . ^ $ * + ? { } [ ] \ | ( )
# . - any symbol 
# ^ - matches at the beginning of the string
# $ - matches at the end of the string
# * - quantifier, 0 or more repetitions
# + - quantifier, 1 or more repetitions
# ? - quantifier, 0 or 1 repetitions
# {} - quantifier, allows to specify the exact amount of repetitions
# [] - set of characters
# \ - backslash, used for special sequences or escaping character
# | - or, allows to check for 2 or more patterns
# () - grouping


import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net."

pattern = r"(?:[A-Za-z']+ ){2}(?:[A-Za-z']+)" # our regex
# ?: at the beginning of the group makes it non-capturing

results = re.finditer(pattern, text_to_match)

for result in results:
    print(result)
    print(result.group(0)) # the whole match of the regex
    # print(result.group(1)) # error - group does not capture
    # print(result.group(2)) # error - group does not capture