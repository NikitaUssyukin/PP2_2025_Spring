# compile()

import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net."

pattern = r'[Jj]ohn'

def repl(match):
    matched_word = match.group(0)
    if matched_word[0].isupper():
        return "Johnny"
    else:
        return "johnny"

result = re.sub(pattern, repl, text_to_match)

print(result)