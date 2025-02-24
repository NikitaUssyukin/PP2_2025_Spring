import os 

file_name = 'test.txt'

path = os.getcwd()

files_and_folders = os.scandir(path) 
# returns a scandir iterator

print(files_and_folders)
print(type(files_and_folders))