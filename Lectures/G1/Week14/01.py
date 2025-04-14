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

def create_function_count_with_year():
    command =   """ CREATE OR REPLACE FUNCTION count_with_year(selected_year INTEGER)
                    RETURNS INTEGER AS
                    $$
                    BEGIN
                        RETURN COUNT(*) FROM students WHERE students.year = selected_year;
                    END; $$
                    LANGUAGE plpgsql;
                """
    try:
        with conn.cursor() as cur:
            cur.execute(command)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_new(student_to_insert):
    command = "CALL add_new_student(%s, %s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, student_to_insert)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def delete_by_name(name):
    command = "CALL delete_student(%s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# create_table()
# csv_to_table('students.csv')   
# create_function_count_with_year()

create_function_count_with_year =   """ 
    CREATE OR REPLACE FUNCTION count_with_year(selected_year INTEGER)
    RETURNS INTEGER AS
    $$
    BEGIN
        RETURN COUNT(*) FROM students WHERE students.year = selected_year;
    END; $$
    LANGUAGE plpgsql;
"""

create_procedure_insert_new =   """
    CREATE OR REPLACE PROCEDURE add_new_student(
        new_student_name varchar,
        new_student_telephone varchar,
        new_student_year integer
    )
    AS $$
    BEGIN
        -- insert into the students table
        INSERT INTO students(name, telephone, year)
        VALUES(new_student_name, new_student_telephone, new_student_year);
    END;
    $$
    LANGUAGE PLPGSQL;
"""

create_procedure_delete =   """
    CREATE OR REPLACE PROCEDURE delete_student(
        student_name varchar
    )
    AS $$
    BEGIN
        -- delete from students table
        DELETE FROM students WHERE name = student_name;
    END;
    $$
    LANGUAGE PLPGSQL;
"""

students_to_insert = [
    ('Raim', '+77077070000', 2),
    ('Alexandra', '+77077878787', 2),
    ('Jennifer', '+77077878787', 2)
]


# execute_query(create_procedure_insert_new)
# insert_new(students_to_insert[0])

execute_query(create_procedure_delete)
delete_by_name('Raim')



