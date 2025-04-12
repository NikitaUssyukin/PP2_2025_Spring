# DB - Database
# Databases are used to store structured information (data)

# RDB - Relational Databases

# In RDB, data is stored in tables (also called relations)
# The data is structured in rows and columns
# also called records and fields
# A record represents one item/entity
# And fields of the record represent individual data items for this record

# RDBMS - Relational Database Management System

# RDBMS is needed to work with RDB

# SQL - Structured Query Language
# PostgreSQL - dialect of SQL

# CRUD - Create Read Update Delete
# We're going to use CRUD operations to work with information in our DB
# For that, we're goint to use the following SQL keywords:
# Create - INSERT
# Read - SELECT
# Update - UPDATE
# Delete - DELETE

# SQL is a declarative language
# Declarative - you write what you want to do
# and you do not specify how to do it

# Examples of imperative languages: C++, Java, C, C#, Python, COBOL, etc

# As our RDBMS we're going to use PostgreSQL
# (Actually, it is ORDBMS, O stands for Object)

# To install PostgreSQL, follow the steps in this tutorial - https://www.w3schools.com/postgresql/postgresql_install.php

# psycopg2 - module that will allow us to work with Postgres via Python

# to install psycopg2, open the teminal and run:
# pip install psycopg2
# or
# pip install psycopg2-binary

# csv - comma-separated values

import psycopg2

conn = psycopg2.connect( # creating a connection
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

command = """SELECT version()"""

with conn.cursor() as cur:
    # execute the command
    cur.execute(command)
    print(cur.fetchone())
