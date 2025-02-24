file_name = 'test.txt' # relative path - the file should exist
# at the current working directory
# check os.getcwd() and os.listdir(path)

file = open(file_name, 'r') # by default, files are opened in 'r' mode

print(f'File {file_name} is closed:', file.closed)

file.close()

print(f'File {file_name} is closed:', file.closed)