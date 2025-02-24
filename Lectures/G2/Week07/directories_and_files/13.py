import os

path = r'C:\Windows\System32'

print(os.access(path, os.F_OK)) # Existence
print(os.access(path, os.R_OK)) # Readability
print(os.access(path, os.W_OK)) # Writeability
print(os.access(path, os.X_OK)) # Executeability