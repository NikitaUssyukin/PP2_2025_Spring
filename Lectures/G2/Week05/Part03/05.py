# json

# https://docs.python.org/3/library/json.html#module-json

# added after the lecture
# don't forget to put data into the actual json file
# python to JSON table:
# https://docs.python.org/3/library/json.html#py-to-json-table

import json

json_file = 'ferrari.json'

with open(json_file, 'r') as file:
    global ferrari
    ferrari = json.load(file)

print(type(ferrari))

print(ferrari)
print(ferrari["price"])