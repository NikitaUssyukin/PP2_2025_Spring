file_name = 'test.txt' # relative path - the file should exist
# at the current working directory
# check os.getcwd() and os.listdir(path)

file = open(file_name)

contents = file.read()

print(contents)