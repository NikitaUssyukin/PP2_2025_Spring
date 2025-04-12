# DB - Database
# Databases are used to store structured data

# RDB - Relational Database

# In RDBs, data is stored in table-like manner
# tables in this case are called 'relations'

# These tables have rows and columns
# also called records and fields

# Rows represent individual items, entities
# e.g., one individual student, his/her id, name, specialty, phone, etc

# Columns represend individual data items within one row
# e.g., one student's name, or id, or specialy, etc

# RDBMS - Relational Database Mangement System

# RDBMS example - PostgreSQL

# SQL - Structured Query Language

# SQL is used for working with RDBs
# SQL is a declarative language
# i.e., you tell it what you want to do, but you don't tell exactly how

# There are also imperative languages, where the opposite is true
# Examples: C++, C#, C, Java, Python

# To work with databases, we need CRUD

# CRUD - Create, Retrieve, Update, Delete
# In SQL, this maps to the following keywords:
# Create - INSERT
# Retrieve - SELECT
# Update - UPDATE
# Delete - DELETE

# psycopg2 - module used to work with PostgreSQL in python

# To work with a database via psycopg2, you need 2 things:
# connection
# cursor

import psycopg2

conn = psycopg2.connect( # creating a connection
    host="localhost",
    database="suppliers",
    user="postgres",
    password="1234"
)

command = """SELECT version()"""

with conn.cursor() as cur:
    # execute the command
    cur.execute(command)
    print(cur.fetchone())