import psycopg2
import csv

conn = psycopg2.connect( # creating a connection
    host="localhost",
    database="university",
    user="postgres",
    password="1234"
)

def create_table():
    command = """CREATE TABLE students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            telephone VARCHAR(20),
            year INTEGER
        )"""
    try:
        with conn.cursor() as cur:
            # execute the command
            cur.execute(command)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def csv_to_table(filename):
    command = f"""INSERT INTO students(name, telephone, year) VALUES(%s, %s, %s)"""
    try:
        with conn.cursor() as cur:
            # execute the command
            with open(filename, "r") as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',')
                _ = next(csvreader) # getting rid of the headers
                for row in csvreader:
                    # print(row)
                    name, telephone, year = row
                    # print(id, name, telephone, year)
                    cur.execute(command, (name, telephone, year))
                    conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# create_table()
csv_to_table('students.csv')    



