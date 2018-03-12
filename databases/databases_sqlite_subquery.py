


# MAIN SOURCE:
# http://www.sqlitetutorial.net/sqlite-subquery/ 
# We use the DB from here (chinook.db)
#
# USEFUL LINKS: 
# 
# 1) SQLite Subquery
#    http://www.dofactory.com/sql/subquery
#
# 2) SQL Wildcard
#    https://www.w3schools.com/sql/sql_wildcards.asp
#
# 3) SQL AND, OR and NOT Operators
#    https://www.w3schools.com/sql/sql_and_or.asp
#
# 4) Good exercises on SQL
#    https://www.khanacademy.org/computing/computer-programming/sql
#


import sqlite3 as lite
import sys
import os

# A subquery is a SELECT statement nested in another statement. 

# SELECT column_1
# FROM table_1
# WHERE column_1 = (
#                   SELECT column_1
#                   FROM table_2
#                  );

# Typically, a subquery returns a single row as an atomic value, 
# though it may return multiple rows for comparing values with 
# the IN operator. You can use a subquery in the SELECT, FROM,
# WHERE, or JOIN clause.

print("-" * 20 + "# 1 SQLite subquery in the WHERE clause example" + "-" * 20)


db_path = os.path.join('db_chinook', 'chinook.db')

conn = lite.connect(db_path)

with conn:

# You can use a simple subquery as a search condition. For example,
# the following statement returns all the tracks in the album with 
# the title "Let There Be Rock" (table 'tracks' doesn't have title of 
# albums, only albumid's).

# The subquery returns the id of the album with the title "Let There
# Be Rock". The query uses the equal operator (=) to compare albumid 
#returned by the subquery with the albumid in the tracks table.

    curs = conn.execute("""SELECT trackid, name, albumid
                           FROM tracks
                           WHERE albumid = (
                                               SELECT albumid
                                               FROM albums
                                               WHERE title = 'Let There Be Rock'
                                           );
                        """)
    
    for i in curs: print(i)
    print('-' * 20)

    # OUTPUT:
    # (15, u'Go Down', 4)
    # (16, u'Dog Eat Dog', 4)
    # (17, u'Let There Be Rock', 4)
    # (18, u'Bad Boy Boogie', 4)
    # (19, u'Problem Child', 4)
    # (20, u'Overdose', 4)
    # (21, u"Hell Ain't A Bad Place To Be", 4)
    # (22, u'Whole Lotta Rosie', 4)

# If the subquery returns multiple values, you can use the IN operator
# to check for the existence of a single value against a set of value.
# For example, the following query returns the customers whose sales
# representatives are in Canada.


    # At first, let's see the last names of employees 

    curs = conn.execute("""SELECT employeeid, lastname, country
                           FROM employees;""")
    
    for i in curs: print(i)       
    print('-' * 20)

    # OUTPUT:
    # (1, u'Adams', u'Canada')
    # (2, u'Edwards', u'Canada')
    # (3, u'Peacock', u'Canada')
    # (4, u'Park', u'Canada')
    # (5, u'Johnson', u'Canada')
    # (6, u'Mitchell', u'Canada')
    # (7, u'King', u'Canada')
    # (8, u'Callahan', u'Canada')

    # Now let's get all customers that are supported by employees from Canada
    # and the last names of these employees starts with 'P'. The outer query
    # uses the IN operator to find the customers who have the sales 
    # representative id in the list.

    curs = conn.execute("""SELECT customerid, firstname, lastname
                           FROM customers
                           WHERE supportrepid IN (
                                                   SELECT employeeid
                                                   FROM employees
                                                   WHERE country = 'Canada' AND lastname LIKE 'P%'
                                                 );""")
    for i in curs: print(i)
    print('-' * 20)

    # OUTPUT:
    # (1, u'Lu\xeds', u'Gon\xe7alves')
    # (3, u'Fran\xe7ois', u'Tremblay')
    # (12, u'Roberto', u'Almeida')
    # (15, u'Jennifer', u'Peterson')
    # (18, u'Michelle', u'Brooks')
    # (19, u'Tim', u'Goyer')
    # ...
    
print("-" * 20 + "# 2 SQLite subquery in the FROM clause example" + "-" * 20)

# Sometimes you want to apply aggregate functions to a column multiple times. 
# For example, first, you want to sum the size of an album and then calculate
# the average size of all albums.

# This query isn't valid:

# SELECT avg(sum(bytes) ) 
# FROM tracks
# GROUP BY albumid;

db_path = os.path.join('db_chinook', 'chinook.db')

conn = lite.connect(db_path)

with conn:
    
    curs = conn.execute("""SELECT sum(bytes) AS size
                           FROM tracks
                           GROUP BY albumid""")
    
    for i in curs: print(i)
    print("-" * 20)
    
    # The AS keyword is to give an ALIAS name to your database table or to table column.
    
    curs = conn.execute("""SELECT avg(album.size)
                           FROM (
                                   SELECT sum(bytes) AS size
                                   FROM tracks
                                   GROUP BY albumid
                                 )
                                 AS album;""")
    
    for i in curs: print(i)
    
    # OUTPUT:
    # (117386255350.0,)


print("-" * 20 + "# 3 SQLite correlated subquery" + "-" * 20)


# READ
# https://www.pluralsight.com/blog/it-ops/linux-file-permissions


