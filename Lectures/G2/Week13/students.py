import psycopg2
import csv

conn = psycopg2.connect( # creating a connection
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

def create_table():

    command = """CREATE TABLE students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                major VARCHAR(10),
                gpa NUMERIC,
                year INTEGER
            )"""

    with conn.cursor() as cur:
        # execute the command
        cur.execute(command)
        conn.commit()

def insert_student(name, major, gpa, year):

    command = """INSERT INTO students(name, major, gpa, year) VALUES(%s, %s, %s, %s)"""

    with conn.cursor() as cur:
        # execute the command
        cur.execute(command, (name, major, gpa, year))
        conn.commit()

def insert_student_from_csv(csv_file_name):

    command = "INSERT INTO students(name, major, gpa, year) VALUES(%s, %s, %s, %s)"

    with conn.cursor() as cur:
        # execute the command
        with open(csv_file_name, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            _ = next(csvreader) # getting rid of the headers
            for row in csvreader:
                # print(row)
                name, major, gpa, year = row
                # print(name, major, gpa, year)
                cur.execute(command, (name, major, gpa, year))
        conn.commit()

def get_students_filter_by_gpa(gpa):
    command = "SELECT * FROM students WHERE gpa > %s"
    with conn.cursor() as cur:
        cur.execute(command, (gpa,)) # (,) is to show that we have a tuple
        # just () will not make it a tuple
        return cur.fetchall()

# create_table()

# insert_student('Raimbek Gosling', 'IS', 5.0, 1)

# insert_student_from_csv('students.csv')

gpa = float(input())
print(get_students_filter_by_gpa(gpa))

conn.close()