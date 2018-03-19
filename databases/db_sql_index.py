

# MAIN SOURCE:
# http://www.sqlitetutorial.net/sqlite-index/
# We use the DB from here (chinook.db)

# USEFUL LINKS: 


# GENERAL INFORMATION:

# In relational databases, a table is a list of rows. In the
# same time, each row has the same column structure that consists
# of cells. Each row also has a consecutive rowid sequence number
# used to identify the row. Therefore, we can consider a table as
# a list of pairs: (rowid, row).

# CONTACTS:
# |rowid|first_name|last_name|email|

# Unlike a table, an index has an opposite relationship: (row, rowid).
# An index is an additional data structure that helps speed up querying,
# join, and grouping operations.

# IDX_CONTACTS_EMAIL

# |email|rowid|

# SQLite uses B-tree index (balanced trees). 

# Each index must be associated with a specific table. An index consists
# of one or more columns, but all columns of an index must be in the same
# table. A table may have multiple indexes.

# Whenever you create an index, SQLite creates a B-tree structure to hold
# the index data. The index contains data from the columns that you specify
# in the index and the corresponding rowid value. This helps SQlite find
# the row quickly based on the values of the indexed columns.

# Imagine an index in the database like an index of a book. By looking at
# the index, you can quickly identify the page number based on the keyword.

# To create an index, you use the CREATE INDEX statement. The following
# illustrates its syntax:

# CREATE [UNIQUE] INDEX index_name ON table_name(indexed_column);

# To create an index, you specify three important information:
# - The table that the index associated with.
# - The list of indexed columns.
# - The name of the index.

# In case you want to make sure that the value of the column is unique like email, phone, etc., you use the UNIQUE option in the CREATE INDEX statement.

from sqlalchemy import create_engine
import os

print("-" * 20 + "# 1 SQLite UNIQUE index example" + "-" * 20)

# Create a new table

try:
    os.remove(os.path.join("db_files/forindex.db"))
except:
    pass

engine = create_engine("sqlite:///db_files/forindex.db")

conn = engine.connect()

rs = conn.execute("""CREATE TABLE contacts (
                       first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                            email TEXT NOT NULL);""")

# Suppose that you want to enforce that the email is unique

rs = conn.execute("""CREATE UNIQUE INDEX idx_contacts_email 
                                      ON contacts (email);""")

# To test this, first, you insert a row into the contacts table

rs = conn.execute("""INSERT INTO contacts (first_name, last_name, email)
                          VALUES ('John', 'Doe', 'john.doe@gmail.com');""")

# Second, try to insert another row with a duplicate email.

# rs = conn.execute("""INSERT INTO contacts (first_name, last_name, email)
#                           VALUES ('Bob', 'Smith', 'john.doe@gmail.com');""")

# ERROR: sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) column
#        email is not unique

# This is because when you inserted the second row, SQLite checked and
# made sure that the email is unique across of rows in the contacts table.

# Let's insert two more rows into the contacts table.

rs = conn.execute("""INSERT INTO contacts (first_name, last_name, email)
                          VALUES ('David', 'Brown', 'david.brown@gmail.com'),
                                 ('Lisa', 'Smith', 'lisa.smith@gmail.com');""")

# If you query data in the contacts table using the email column, SQLite
# will use the index to locate the data.

rs = conn.execute("""SELECT first_name,
                            last_name,
                            email
                       FROM contacts
                      WHERE email = 'lisa.smith@gmail.com';""")
                      
for i in rs: print(i)
# OUTPUT:
# (u'Lisa', u'Smith', u'lisa.smith@gmail.com')

# To check if SQLite uses index or not, you use the EXPLAIN QUERY PLAN
# statement as follows

rs = conn.execute("""EXPLAIN QUERY PLAN
                      SELECT first_name,
                             last_name,
                             email
                        FROM contacts
                       WHERE email = 'lisa.smith@gmail.com';""")
                      
for i in rs: print(i)
# OUTPUT:
# (0, 0, 0, u'SEARCH TABLE contacts USING INDEX idx_contacts_email (email=?) (~1 rows)')

print("-" * 20 + "# 2 SQLite multicolumn index example" + "-" * 20)

# If you create an index that consists of one column, SQLite uses that
# column as the sort key. In case you create an index that has multiple
# columns, SQLite uses the additional columns as the second ... sort keys.

# SQLite sorts the data on the multicolumn index by the first column
# specified in the CREATE INDEX statement. Then it sorts the duplicate
# values by the second column, and so on. Therefore, the column order
# is very important when you create the multicolumn index.

# To utilize a multicolumn index, the query must contain the condition
# that has the same column order as defined in the index.

# The following statement creates a multicolumn index on the first_name
# and last_name columns of the contacts table

rs = conn.execute("""CREATE INDEX idx_contacts_name
                               ON contacts(first_name, last_name)""")

# If you query the contacts table with the one of following conditions
# in the WHERE clause, SQLite will utilize the multicolumn index to search
# for data.

# 1) UTILIZE MULTICOLUMN INDEX: Querying by the first_name column

rs = conn.execute(""" SELECT email
                        FROM contacts
                       WHERE first_name = 'John'""")

for i in rs: print(i)
# (u'john.doe@gmail.com',)

# 2) UTILIZE MULTICOLUMN INDEX: Querying by both first_name and last_name 
#                               columns

rs = conn.execute(""" SELECT email
                        FROM contacts
                       WHERE first_name = 'John' AND last_name = 'Doe'""")

for i in rs: print(i)
# (u'john.doe@gmail.com',)

# However, SQLite will not use the multicolumn index if you use one of the
# following conditions.

# 1) IS NOT UTILIZED MULTICOLUMN INDEX: Querying by the last_name column only

rs = conn.execute(""" SELECT email
                        FROM contacts
                       WHERE last_name = 'Doe'""")

for i in rs: print(i)

# 2) IS NOT UTILIZED MULTICOLUMN INDEX: Querying by first_name OR last_name columns.

rs = conn.execute(""" SELECT email
                        FROM contacts
                       WHERE first_name = 'John' OR last_name = 'Doe'""")

for i in rs: print(i)

print("-" * 20 + "# 3 SQLite DROP INDEX statement" + "-" * 20)

# To remove an index, you use the DROP INDEX statement as follows
# DROP INDEX [IF EXISTS] index_name;
# The IF EXISTS option prevents you from an error of removing a non-existent index.

rs = conn.execute(""" DROP INDEX idx_contacts_name; """)



