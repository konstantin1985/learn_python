


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

# GENERAL INFORMATION:


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

    curs = conn.execute("""SELECT trackid, 
                                  name, 
                                  albumid
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

    curs = conn.execute("""SELECT employeeid, 
                                  lastname, 
                                  country
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

    curs = conn.execute("""SELECT customerid, 
                                  firstname, 
                                  lastname
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
    
    # AS is optional
    curs = conn.execute("""SELECT sum(bytes) AS size
                             FROM tracks
                            GROUP BY albumid;""")
    
    for i in curs: print(i)
    print("-" * 20)
    
    # The AS keyword is to give an ALIAS name to your database table or
    # to table column.
    curs = conn.execute("""SELECT avg(album.size)
                             FROM (
                                    SELECT sum(bytes) AS size
                                      FROM tracks
                                     GROUP BY albumid
                                  )
                                  AS album;""")
    
    # Request with the same result (no alias for the inner query)
    # curs = conn.execute("""SELECT avg(size)
    #                          FROM (
    #                                 SELECT sum(bytes) AS size
    #                                   FROM tracks
    #                                  GROUP BY albumid
    #                               );""")
    
    for i in curs: print(i)
    
    # OUTPUT:
    # (338288920.3170029,)


print("-" * 20 + "# 3 SQLite correlated subquery in the WHERE clause" + "-" * 20)

# All the subqueries you have seen so far can be executed independently. 
# In other words, it does not depend on the outer query.

# The correlated subquery is a subquery that uses the values from the outer
# query. Unlike the ordinal subquery, the correlated subquery cannot be
# executed independently.

# The correlated subquery is not efficient because it is evaluated for each
# row processed by the outer query.



db_path = os.path.join('db_chinook', 'chinook.db')

conn = lite.connect(db_path)

with conn:

    # The following query uses a correlated subquery to return the albums whose
    # size is less than 10MB. Correlation is in the line 
    # WHERE tracks.AlbumId = albums.AlbumId
    
    curs = conn.execute("""SELECT albumid,
                                  title
                             FROM albums
                            WHERE 10000000 > (
                                               SELECT sum(bytes)
                                                 FROM tracks
                                                WHERE tracks.AlbumId = albums.AlbumId
                                             )
                            ORDER BY title;""")

    for i in curs: print(i)

    # OUTPUT:
    # (296, u'A Copland Celebration, Vol. I')
    # (285, u'A Soprano Inspired')
    # (307, u'Adams, John: The Chairman Dances')
    # ...

# How the query works:

# - For each row processed in the outer query, the correlated subquery calculates 
#   the size of the albums from the tracks that belong the current album using the
#   SUM function.
# - The predicate in the WHERE clause filters the albums that have the size greater
#   than or equal 10MB (10000000 bytes).

print("-" * 20 + "# 4 SQLite correlated subquery in the SELECT clause example" + "-" * 20)

# The following query uses a correlated subquery in the SELECT clause to return
# the number of tracks in an album.

db_path = os.path.join('db_chinook', 'chinook.db')

conn = lite.connect(db_path)

with conn:
    
    # AS is omitted before tracks_count
    curs = conn.execute("""SELECT albumid,
                                  title,
                                  (
                                    SELECT count(trackid)
                                      FROM tracks
                                     WHERE tracks.AlbumId = albums.AlbumId 
                                  )
                                  tracks_count
                             FROM albums
                            ORDER BY tracks_count DESC;""")
                            
    for i in curs: print(i)

    # OUTPUT:
    # (141, u'Greatest Hits', 57)
    # (23, u'Minha Historia', 34)
    # (73, u'Unplugged', 30)
    # (229, u'Lost, Season 3', 26)
    # (230, u'Lost, Season 1', 25)
    # (251, u'The Office, Season 3', 25)
    # ...

# READ
# https://www.pluralsight.com/blog/it-ops/linux-file-permissions


