# compile()

import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net."

pattern = r'\b\w+\b'

def repl(match):
    matched_word = match.group(0)
    result = ''
    for i in range(len(matched_word)):
        if i % 2 == 0:
            result += matched_word[i].lower()
        else:
            result += matched_word[i].upper()
    return result

result = re.sub(pattern, repl, text_to_match)

print(result)