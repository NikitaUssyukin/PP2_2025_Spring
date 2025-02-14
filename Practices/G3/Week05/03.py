import json
from sample_str_json import json_str

json_data = {}

json_data = json.loads(json_str)

# print(json_data)

# print(json_data['imdata'][0]['l1PhysIf']['attributes']['dn'])

for data in json_data['imdata']:
    print(data['l1PhysIf']['attributes']['dn'])