# Dictionaries

ourdict = {
    "Make": "Ford",
    "Model": "Mustang",
    "Year": 1971,
    "Color": "Black"
}

for key in ourdict:
    print(key, ourdict[key])

for value in ourdict.values():
    print(value)

for key, value in ourdict.items():
    print(key, value)