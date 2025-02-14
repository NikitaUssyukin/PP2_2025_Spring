import json

json_file = 'sample.json'

json_data = {}

with open(json_file, 'r') as file:
    json_data = json.load(file)

# print(json_data)

# print(json_data['imdata'][0]['l1PhysIf']['attributes']['dn'])

for data in json_data['imdata']:
    print(data['l1PhysIf']['attributes']['dn'])