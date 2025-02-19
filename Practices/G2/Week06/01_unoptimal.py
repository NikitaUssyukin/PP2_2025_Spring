import re

text_to_match = "some_snake_case"

# someSnakeCase

res = re.split(r'_', text_to_match)

print(res)

ans = ''

for word in res:
    ans += word.capitalize()

res = ''
res += ans[0].lower() + ans[1:]

print(res)

