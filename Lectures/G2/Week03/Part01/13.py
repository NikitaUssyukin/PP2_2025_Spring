# Combining collections, on the example of dictionary of dictionaries

ourdict = { 
    "firstCar": {
    "make": "BMW",
    "model": "M5 E34",
    "year": 1995,
    "color": "Black",
    "mileage": 100000,
    "price": "8 million tenge"
    }
}

ourdict["secondCar"] = {
    "make": "Lamborghini",
    "model": "Aventador",
    "year": 2020,
    "color": "Green",
    "mileage": 5000,
    "price": "five hundred thousand dollars (a lot of tenge)"
}

print(ourdict)
print(ourdict["secondCar"])

ourdict["secondCar"]["color"] = "Yellow"

print(ourdict)





