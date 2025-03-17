def nums(n):
    for i in range(n + 1):
        yield i

a = int(input())

result = ', '.join(map(str, list(nums(a))))

print(result)