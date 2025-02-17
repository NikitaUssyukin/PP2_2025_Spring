# What are regular expressions?

import re

text = "Hello KBTU"

pattern = "Hello"

result = re.match(pattern, text)

print(result) # match object

print(result.group(0)) # group(0) returns the entire match
