import os

def check_dir_file(name):
    return 'Is file/Is folder: ' + str(os.path.isfile(entry)) + '/' + str(os.path.isdir(entry))

path = r'C:\Windows\System32'

for entry in os.listdir(path):
    existence = os.access(entry, os.F_OK) # Existence
    readability = os.access(entry, os.R_OK) # Readability
    writeability = os.access(entry, os.W_OK) # Writeability
    executability = os.access(entry, os.X_OK)  # Executeability
    if not existence:
        print(check_dir_file(entry)) 
        print(entry, 'does not exist')
        break
    if not readability:
        print(check_dir_file(entry)) 
        print(entry, 'no access to read')
        break
    if not writeability:
        print(check_dir_file(entry)) 
        print(entry, 'no access to write')
        break
    if not executability:
        print(check_dir_file(entry)) 
        print(entry, 'no access to execute')
        break
    