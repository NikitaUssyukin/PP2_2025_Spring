import re

text_to_match = "some_snake_case"

p = r'_([a-z])'

results = re.finditer(p, text_to_match)
for r in results:
    print(r)
    print(r.group(1))
    print(r.group(1).upper())

def repl(match):
    return match.group(1).upper()

result = re.sub(p, repl, text_to_match)

print(result) RESULT