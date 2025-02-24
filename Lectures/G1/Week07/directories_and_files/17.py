file_name = 'sample.txt' # relative path - the file should exist
# at the current working directory
# check os.getcwd() and os.listdir(path)

with open(file_name, 'w') as file:
    file.write('Written from 17.py\n')