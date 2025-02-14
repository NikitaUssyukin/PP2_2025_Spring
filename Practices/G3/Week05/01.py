def nums_gen(n):
    for i in range(n+1):
        yield i

print(*nums_gen(5), sep=', ')