

# MAIN SOURCE:
# https://pythonspot.com/tag/sql/
#
# USEFUL LINKS: 
# 
# 1) 
#    https://www.pythoncentral.io/introduction-to-sqlite-in-python/
#
# 2) SQL INNER/LEFT/RIGHT/FULL JOIN 
#   https://stackoverflow.com/questions/5706437/whats-the-difference-between-inner-join-left-join-right-join-and-full-join
#
# 3) What is the difference between "INNER JOIN" and "OUTER JOIN"?
#    https://stackoverflow.com/questions/38549/what-is-the-difference-between-inner-join-and-outer-join
# 
# 4) Python file path in Windows and Linux
#    https://askubuntu.com/questions/350458/passing-a-file-location-to-python 
# 
# 5) UPDATE query
#    https://www.tutorialspoint.com/sqlite/sqlite_update_query.htm
#
# 6) GROUP BY query
#    http://www.sqlitetutorial.net/sqlite-group-by/
#    https://stackoverflow.com/questions/7434657/how-does-group-by-work
# 
# 7) fetchall()
#    https://stackoverflow.com/questions/21334767/is-sqlite3-fetchall-necessary
#
# 8) SQLite Subquery
#    http://www.sqlitetutorial.net/sqlite-subquery/


# GENERAL INFORMATION:
#
# Life Cycle of Cursor:
# 1: Declare Cursor: A cursor is declared by defining the SQL
#    statement that returns a result set.
# 2: Open: A Cursor is opened and populated by executing the
#    SQL statement defined by the cursor.
# 3: Fetch: When cursor is opened, rows can be fetched from 
#    the cursor one by one or in a block to do data manipulation.
# 4: Close: After data manipulation, we should close the cursor
#    explicitly.
# 5: Deallocate: Finally, we need to delete the cursor definition
#    and released all the system resources associated with the cursor.

import sqlite3 as lite
import sys
import os

print("-" * 20 + "# 1 SQL basic connection" + "-" * 20)

# We can use 'db_files/test.db' as a DB path.   
# But better is to be OS agnostic (os.path.join)
# https://askubuntu.com/questions/350458/passing-a-file-location-to-python

db_path = os.path.join('db_files', 'test.db')

try:
    os.remove(db_path)
except OSError:
    pass

try:    
    con = lite.connect(db_path)
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')                 # Query the database management system 
    data = cur.fetchone()
    print("SQLite version: %s" % data)
except lite.Error, e:
    print("Error: %s" % e.args[0])
    sys.exit(1)
finally:
    if con:
        con.close()


print("-" * 20 + "# 2 SQL CREATE and INSERT" + "-" * 20)

db_path = os.path.join('db_files', 'user.db')

try:
    os.remove(db_path)
except OSError:
    pass

con = lite.connect(db_path)

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Users(Id INT, Name TEXT)")
    cur.execute("INSERT INTO Users VALUES(1, 'Michelle')")
    cur.execute("INSERT INTO Users VALUES(2, 'Sonya')")
    cur.execute("INSERT INTO Users VALUES(3, 'Greg')")
    

print("-" * 20 + "# 3 SQL SELECT" + "-" * 20)

con = lite.connect(db_path)

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Users")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # OUTPUT:
    # (1, u'Michelle')
    # (2, u'Sonya')
    # (3, u'Greg')

    cur.execute("SELECT * FROM Users WHERE id = 2")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
    # OUTPUT:
    # (2, u'Sonya') 
  
print("-" * 20 + "# 4 INNER JOIN and LEFT JOIN" + "-" * 20)

db_path = os.path.join('db_files', 'system.db')

try:
    os.remove(db_path)
except OSError:
    pass
    
con = lite.connect(db_path)

with con:
    
    cur = con.cursor()
    cur.execute("CREATE TABLE Users(Id INT, Name TEXT)")
    cur.execute("INSERT INTO Users VALUES(1,'Michelle')")
    cur.execute("INSERT INTO Users VALUES(2,'Howard')")
    cur.execute("INSERT INTO Users VALUES(3,'Greg')")
    cur.execute("INSERT INTO Users VALUES(4,'Michael')")
 
    cur.execute("CREATE TABLE Jobs(Id INT, Uid INT, Profession TEXT)")
    cur.execute("INSERT INTO Jobs VALUES(10,1,'Scientist')")
    cur.execute("INSERT INTO Jobs VALUES(20,2,'Marketeer')")
    cur.execute("INSERT INTO Jobs VALUES(30,3,'Developer')")
    cur.execute("INSERT INTO Jobs VALUES(40,5,'Seller')")

# The jobs table has an extra parameter, Uid. We use that to 
# connect the two tables in an SQL query.

con = lite.connect(db_path)

with con:
    
    cur = con.cursor()
    
    # INNER JOIN 
    # it gives the intersection of the two tables, i.e. rows
    # they have common in TableA and TableB
    
    # SELECT TableA.firstName,TableA.lastName,TableB.age,TableB.Place
    # FROM TableA
    # INNER JOIN TableB
    # ON TableA.id = TableB.id2;
    
    # Not case sensitive Jobs == jobs 
    cur.execute("""SELECT users.id, users.name, jobs.profession 
                   FROM jobs 
                   INNER JOIN users 
                   ON users.id = jobs.uid""")

    rows = cur.fetchall() 
    for row in rows:
        print(row)

    # OUTPUT:
    # (1, u'Michelle', u'Scientist')
    # (2, u'Howard', u'Marketeer')
    # (3, u'Greg', u'Developer')

        
    # LEFT JOIN
    # will give all selected rows in TableA, plus any common selected
    # rows in TableB.

    # SELECT TableA.firstName,TableA.lastName,TableB.age,TableB.Place
    # FROM TableA
    # LEFT JOIN TableB
    # ON TableA.id = TableB.id2;

    print('-' * 20)

    cur.execute("""SELECT users.id, users.name, jobs.profession 
                   FROM jobs 
                   LEFT JOIN users 
                   ON users.id = jobs.uid""")

    rows = cur.fetchall() 
    for row in rows:
        print(row)

    # OUTPUT:
    # (1, u'Michelle', u'Scientist')
    # (2, u'Howard', u'Marketeer')
    # (3, u'Greg', u'Developer')
    # (None, None, u'Seller')
        
print("-" * 20 + "# 5 UPDATE and DELETE" + "-" * 20)

db_path = os.path.join('db_files', 'employees.db')

try:
    os.remove(db_path)
except OSError:
    pass

conn = lite.connect(db_path)
    
# Create and fill the table

with conn:
    
    # Semicolon here is optional
    conn.execute('''CREATE TABLE Company
                    (Id INT PRIMARY KEY,
                     Name TEXT,
                     Age INT,
                     Address CHAR(50),
                     Salary REAL);''')
    print("Table created successfully")
    
    conn.execute("INSERT INTO Company VALUES(1, 'Paul', 32, 'California', 20000.00)")
    conn.execute("INSERT INTO Company VALUES(2, 'Allen', 25, 'Texas', 15000.00)")
    conn.execute("INSERT INTO Company VALUES(3, 'Teddy', 23, 'Norway', 20000.00)")
    conn.execute("INSERT INTO Company VALUES(4, 'Mark', 25, 'Rich-Mond ', 65000.00)")
    conn.commit()
    print("Records created successfully")
    
    # Unnecessary when we have 'with'
    # conn.close
    
# UPDATE

conn = lite.connect(db_path)

with conn:
    
    # If you want to modify all the SALARY column values in the CCOMPANY table, 
    # you do not need to use the WHERE clause as the UPDATE query would be enough.
    
    conn.execute("""UPDATE Company
                    SET Salary = 25000.00
                    WHERE Id = 1""")
    conn.commit()
    
    # total_changes: Returns the total number of database rows that
    # have been modified, inserted, or deleted since the database
    # connection was opened.
    print("Total number of rows updated: %s" % conn.total_changes)
    
    cursor = conn.execute("""SELECT Id, Name, Address, Salary
                             FROM Company""")
    
    for row in cursor:
        print("ID = {}; NAME = {}; ADDRESS = {}, SALARY = {}".format(row[0], row[1], row[2], row[3]))
    
    # OUTPUT:
    # ID = 1; NAME = Paul; ADDRESS = California, SALARY = 25000.0
    # ID = 2; NAME = Allen; ADDRESS = Texas, SALARY = 15000.0
    # ID = 3; NAME = Teddy; ADDRESS = Norway, SALARY = 20000.0
    # ID = 4; NAME = Mark; ADDRESS = Rich-Mond , SALARY = 65000.0
    
    print("Update is done successfully")

# DELETE

with conn:
    conn.execute("""DELETE FROM Company
                    WHERE Name = 'Allen';""")
    conn.commit()
    print("Total number of rows deleted: %s" % (conn.total_changes,))
    
    cursor = conn.execute("""SELECT Id, Name, Address, Salary
                             FROM Company
                             ORDER BY Salary""")

    for row in cursor:
        print("ID = {}; NAME = {}; ADDRESS = {}, SALARY = {}".format(row[0], row[1], row[2], row[3]))

    # OUTPUT:
    # ID = 3; NAME = Teddy; ADDRESS = Norway, SALARY = 20000.0
    # ID = 1; NAME = Paul; ADDRESS = California, SALARY = 25000.0
    # ID = 4; NAME = Mark; ADDRESS = Rich-Mond , SALARY = 65000.0
    
    print("Delete is done successfully")


conn.close()
    
print("-" * 20 + "# 5 GROUP BY" + "-" * 20)

db_path = os.path.join('db_files','albums')

try:
    os.remove(db_path)
except OSError:
    pass

conn = lite.connect(db_path)

with conn:
    
    # PRIMARY KEY doesn't allow TrackId to have the same values
    conn.execute("""CREATE TABLE Tracks
                    (TrackId INT PRIMARY KEY,
                     Name TEXT,
                     AlbumId INT);""")
    conn.execute("""INSERT INTO Tracks VALUES(1, 'Lesnik', 2)""")
    conn.execute("""INSERT INTO Tracks VALUES(2, 'Posledniy Geroy', 1)""")
    conn.execute("""INSERT INTO Tracks VALUES(3, 'Gulaut teni', 2)""")
    conn.execute("""INSERT INTO Tracks VALUES(4, 'April', 1)""")
    conn.execute("""INSERT INTO Tracks VALUES(5, 'Peremen', 1)""")
    conn.commit()
    
    # GROUP BY returns a single row for each unique combination
    # of the GROUP BY fields. Aggregate functions like SUM() are
    # computed over the members of each group.
    
    # The following statement returns the album id and the number
    # of tracks per album. It uses the GROUP BY clause to groups
    # tracks by album and apply the COUNT function to each group.
    cursor = conn.execute("""SELECT AlbumId, COUNT(TrackId)
                             FROM Tracks
                             GROUP BY AlbumId""")
    for row in cursor:
        print(row)
    
    # OUTPUT: 
    # (1, 2)
    # (2, 3)

    print('-' * 20)

    # You can use the ORDER BY clause to sort the groups
    cursor = conn.execute("""SELECT AlbumId, COUNT(TrackId)
                             FROM Tracks
                             GROUP BY AlbumId
                             ORDER BY COUNT(TrackId) ASC""")   # ASC - default, DESC
                             
    for row in cursor:
        print(row)
    
    # OUTPUT:
    #(2, 2)
    #(1, 3)
    

# Some more good examples to try are here: http://www.sqlitetutorial.net/sqlite-group-by/





