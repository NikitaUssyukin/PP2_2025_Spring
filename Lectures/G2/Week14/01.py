import psycopg2
import csv

conn = psycopg2.connect( # creating a connection
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

create_func_select_all = """
    CREATE FUNCTION select_all()
    RETURNS TABLE (id INTEGER, name VARCHAR(255), major VARCHAR(10), gpa NUMERIC, year INTEGER)
    AS
    $$
    BEGIN
        RETURN QUERY
        SELECT * FROM students;
    END;
    $$
    LANGUAGE plpgsql;
"""

create_func_filter_by_first_letter = """
    CREATE OR REPLACE FUNCTION filter_by_first_letter(letter VARCHAR(1))
    RETURNS TABLE (id INTEGER, name VARCHAR(255), major VARCHAR(10), gpa NUMERIC, year INTEGER)
    AS
    $$
    BEGIN
        RETURN QUERY
        SELECT * FROM students WHERE LEFT(students.name, 1) = letter;
    END;
    $$
    LANGUAGE plpgsql;
"""

create_proc_delete_by_name = """
    CREATE OR REPLACE PROCEDURE delete_by_name(name_to_delete VARCHAR)
    AS
    $$
    BEGIN
        DELETE FROM students WHERE students.name = name_to_delete;
    END;
    $$
    LANGUAGE plpgsql;
"""

def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def call_select_all():
    command = "SELECT * FROM select_all()"
    try:
        with conn.cursor() as cur:
            cur.execute(command)
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def call_function(function_name):
    try:
        with conn.cursor() as cur:
            cur.callproc(function_name)
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def call_function_w_args(function_name, args):
    try:
        with conn.cursor() as cur:
            cur.callproc(function_name, args)
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def call_delete_by_name(name):
    command = "CALL delete_by_name(%s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


# execute_query(create_func_select_all)
# print(call_select_all())
# print(call_function('select_all'))

# execute_query(create_func_filter_by_first_letter)
# print(call_function_w_args('filter_by_first_letter', ('R',)))

execute_query(create_proc_delete_by_name)
call_delete_by_name('Ramazan')
