import time
import os

file_name = 'new.txt'

with open(file_name, 'w') as file:
    file.write('Last words before removal...')

time.sleep(5) # 5-second delay

os.remove(file_name)

'''
'r'  -  read mode
'w'  -  write mode
'a'  -  append mode
'x'  -  create mode
'''
