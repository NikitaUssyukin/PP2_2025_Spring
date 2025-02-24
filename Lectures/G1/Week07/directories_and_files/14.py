file_name = 'test.txt' # relative path - the file should exist
# at the current working directory
# check os.getcwd() and os.listdir(path)

file = open(file_name, 'r') # by default, files are opened in 'r' mode

'''
'r' - read mode
'w' - write mode
'a' - append mode
'x' - create mode
'''

contents = file.read()

print(contents)