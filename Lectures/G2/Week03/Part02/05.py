# Functions

# arbitrary arguments, *args
def func(*args):
    print(args)
    for arg in args:
        print(arg)

func(1, 2, 3, "Dog", "Pineapple", "whatever")