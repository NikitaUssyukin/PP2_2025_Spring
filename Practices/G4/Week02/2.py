n = int(input())
 
nums = []

for _ in range(n):
    nums += [[0] * n]
 
row_start = 0
row_end = n-1
 
col_start = 0
col_end = n-1
 
cur = 0
 
while row_start <= row_end and col_start <= col_end:
 
    for j in range(col_start, col_end+1):
        cur += 1
        nums[row_start][j] = cur
 
    row_start += 1
 
    for i in range(row_start,row_end+1):
        cur += 1
        nums[i][col_end] = cur
 
    col_end -= 1
 
    for j in range(col_end,col_start-1,-1):
        cur += 1
        nums[row_end][j] = cur
    row_end -= 1
 
    for i in range(row_end,row_start-1,-1):
        cur += 1
        nums[i][col_start] = cur
 
    col_start += 1
 
 
print(nums)