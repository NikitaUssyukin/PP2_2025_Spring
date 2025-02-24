file_name = 'sample.txt' # relative path - the file should exist
# at the current working directory
# check os.getcwd() and os.listdir(path)

with open(file_name, 'a') as file:
    file.write('Appended from 18.py\n')