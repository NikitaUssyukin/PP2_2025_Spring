import re

text_to_match = "someCamelCase"

# some Camel Case

res = re.sub(r'([a-z])([A-Z])', r'\1 \2', text_to_match)

print(res)

