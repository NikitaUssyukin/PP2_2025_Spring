# Functions

# arbitrary keyword arguments, *kwargs
def func(**kwargs):
    print(kwargs)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])

func(make = "Toyota", model = "Camry")