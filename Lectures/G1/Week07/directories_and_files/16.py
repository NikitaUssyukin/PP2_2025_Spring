file_name = 'test.txt' # relative path - the file should exist
# at the current working directory
# check os.getcwd() and os.listdir(path)

with open(file_name, 'r') as file: # by default, files are opened in 'r' mode
    print(f'File {file_name} is closed:', file.closed)

print(f'File {file_name} is closed:', file.closed)