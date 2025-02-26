test_str = 'hello'

rev = reversed(test_str)

res = ''

for symbol in rev:
    res += symbol

print(res)