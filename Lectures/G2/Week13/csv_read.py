import csv

filename = 'students.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    _ = next(csvreader) # getting rid of the headers
    for row in csvreader:
        print(row)
        name, major, gpa, year = row
        print(name, major, gpa, year)