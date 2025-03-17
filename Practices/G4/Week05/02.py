def nums(n):
    for i in range(n + 1):
        yield i

a = int(input())

print(*nums(a), sep=', ')

