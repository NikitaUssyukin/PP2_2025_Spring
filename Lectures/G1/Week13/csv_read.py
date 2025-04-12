import csv

filename = 'students.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)
        id, name, telephone, year = row
        print(id, name, telephone, year )