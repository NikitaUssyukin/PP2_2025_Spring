import re

text_to_match = """
John's email is john.doe@example.com
Hello John
"""

pattern = r'\w+'

def repl(match):
    word = str(match.group(0))
    res = ''
    for i in range(len(word)):
        if i % 2 == 0:
            res += word[i].lower()
        else:
            res += word[i].upper()
    return res

result = re.sub(pattern, repl, text_to_match.strip()) 
# splits the text by newlines

print(result)

