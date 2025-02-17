# compile()

import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net."

pattern = re.compile('John')
# pattern now is a regex object
print(type(pattern)) # re.Pattern

result = pattern.match(text_to_match)

print(result) # match object

print(result.group()) # print the match as a string