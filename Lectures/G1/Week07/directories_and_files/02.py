import os

path = r'C:\Users\n.ussyukin\Desktop\PP2_2025_Spring\Lectures\G1\Week07\directories_and_files' # absolute path
# .. - shorthand for previous directory
# .  - shorthand for current directory

contents = os.listdir(path)

for element in contents:
    print(element)

