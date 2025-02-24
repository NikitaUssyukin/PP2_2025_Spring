file_name = 'info.txt' # relative path - the file should exist
# at the current working directory
# check os.getcwd() and os.listdir(path)

with open(file_name, 'r') as file: 
    print(file.readline())
    print(file.readline())
    print(file.readline())