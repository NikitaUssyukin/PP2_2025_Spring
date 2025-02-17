import re

text = "Hello KBTU"

pattern = re.compile("Hello")
# pattern now contains a regex object

result = pattern.match(text)

print(result) # match object

print(result.group(0)) # group(0) returns the entire match
