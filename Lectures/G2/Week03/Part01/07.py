# Sets

ourset = {"BMW", "Toyota", "Mercedes"}

ourset.add("Lexus")
ourset.add("Zeekr")
ourset.add("Audi")

if "Lexus" in ourset:
    print("Lexus found")
else:
    print("Lexus not found")

if "Honda" in ourset:
    print("Honda found")
else:
    print("Honda not found")

if "Ferrari" not in ourset:
    print("Sadly, Ferrari not found")
else:
    print("Ferrari found")

