import json
from sample_str_json import json_str

json_data = {}

json_data = json.loads(json_str) # reads json from json string

# print(json_data)

dn_list = [dn['l1PhysIf']['attributes']['dn'] for dn in json_data['imdata']]

# for elm in dn_list:
#     print(elm)

# print(dn_list)

json_output_file = 'sample_output.json'

with open(json_output_file, 'w') as file:
    json.dump(dn_list, file, indent=4)