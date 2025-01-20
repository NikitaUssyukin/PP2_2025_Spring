# Conditional statements

a = int(input())

if a > 0: 
    print("positive")
    if a % 2 == 0:
        print("even")
    else:
        print("odd")
elif a < 0:
    print("negative")
    if a % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("zero")