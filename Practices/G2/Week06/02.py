import re

text_to_match = "some_snake_case"

# someSnakeCase

def repl(match):
    return match.group(1).upper()

res = re.sub(r'_([a-z])', repl, text_to_match)

print(res)

