# compile()

import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net."

pattern = r'[Jj]ohn'

replace_matched_with = 'Johnny'

result = re.sub(pattern, replace_matched_with, text_to_match)

print(result)