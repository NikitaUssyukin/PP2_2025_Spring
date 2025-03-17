import json
from sample_str_json import json_str

json_data = {}

json_data = json.loads(json_str) # reads json from json string

print(json_data)

for element in json_data['imdata']:
    print(element['l1PhysIf']['attributes']['dn'])