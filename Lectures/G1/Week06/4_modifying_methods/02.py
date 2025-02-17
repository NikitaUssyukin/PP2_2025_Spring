import re

text_to_match = """
John's email is john.doe@example.com
Hello John
"""

pattern = r'John'

result = re.sub(pattern, "Johnny" ,text_to_match.strip()) 
# splits the text by newlines

print(result)

