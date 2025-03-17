import json

json_file = 'sample.json'

# json_data = {}

with open(json_file, 'r') as file:
    json_data = json.load(file) # reads json from json file

print(json_data)

for element in json_data['imdata']:
    print(element['l1PhysIf']['attributes']['dn'])