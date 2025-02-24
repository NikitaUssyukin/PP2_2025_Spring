import os

path = os.getcwd()
# get cwd - current working directory
# cwd is the folder, where the terminal is currently open
# i.e, the cwd of the terminal
# to check it in the terminal, use this command: pwd
print(path)

contents = os.listdir(path)

for element in contents:
    print(element)

