import json
from sample_str_json import json_str

json_data = {}

json_data = json.loads(json_str)

# print(json_data)

# print(json_data['imdata'][0]['l1PhysIf']['attributes']['dn'])

dn_list = []

for data in json_data['imdata']:
    dn_list.append(data['l1PhysIf']['attributes']['dn'])

# print(dn_list)

output_json_str = json.dumps(dn_list, indent=4)

print(output_json_str)

