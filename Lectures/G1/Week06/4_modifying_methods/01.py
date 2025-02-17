import re

text_to_match = """
John's email is john.doe@example.com
Hello John
"""

pattern = r'\n' # newline

result = re.split(pattern, text_to_match.strip()) 
# splits the text by newlines

print(result)

