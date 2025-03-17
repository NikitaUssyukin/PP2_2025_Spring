def nums(n):
    for i in range(n + 1):
        yield i

for num in nums(5):
    print(num, end=', ')