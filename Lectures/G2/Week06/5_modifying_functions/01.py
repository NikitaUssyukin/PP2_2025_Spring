# compile()

import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net."

pattern = r'\b\w{3}\b'

result = re.split(pattern, text_to_match)

print(result)