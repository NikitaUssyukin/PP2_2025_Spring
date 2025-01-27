'''
Plan for the lecture:
- Tuples, Sets and Dictionaries - briefly
- Functions
- Lambda functions
- Classes and objects
- Inheritance
'''

# List comprehension

ourlist = []

for i in range (1, 6):
    ourlist.append(i)

print(ourlist)

ourlist.clear()

# creating a list using list comprehension
ourlist = [x for x in range(1, 6)]
# syntax: some_var = [expression for item in some_iterable if condition]

print(ourlist)

anotherlist = [x * 2 for x in range(1, 6) if x % 2 == 1]
print(anotherlist)

