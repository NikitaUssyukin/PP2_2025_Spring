import os 

file_name = 'test.txt'

# using relative path
print(os.access(file_name, os.F_OK)) # check for existence
print(os.access(file_name, os.R_OK)) # check for readibility
print(os.access(file_name, os.W_OK)) # check for writability
print(os.access(file_name, os.X_OK)) # check for executability
