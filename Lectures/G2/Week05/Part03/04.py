# json

# https://docs.python.org/3/library/json.html#module-json

import json

json_string = '{"make": "Ferrari", "model": "458 Italia", "price": 300000}'

ferrari = json.loads(json_string)

print(type(ferrari))
print(ferrari)
print(ferrari["model"])