


# MAIN SOURCE:
# http://www.sqlitetutorial.net/sqlite-limit/

# USEFUL LINKS: 


# GENERAL INFORMATION:

# The LIMIT clause is an optional part of the SELECT statement. You use
# the LIMIT clause to constrain the number of rows returned by the query.

# For example, a SELECT statement returns one million rows. However, if
# you just need the first 10 rows in the result set, you add the LIMIT 
# clause to the SELECT statement to get exact 10 rows.

print("-" * 20 + "# 1 Introduction to SQLite LIMIT clause" + "-" * 20)

from sqlalchemy import create_engine
engine = create_engine('sqlite:///db_chinook/chinook.db')
con = engine.connect()

rs = con.execute("""SELECT TrackId,
                           Name
                      FROM tracks
                     LIMIT 5;""")

# print(rs.fetchall())                         # Will print as a list
for i in rs: print i
print('-' * 20)

# OUTPUT:
# (1, u'For Those About To Rock (We Salute You)')
# (2, u'Balls to the Wall')
# (3, u'Fast As a Shark')
# (4, u'Restless and Wild')
# (5, u'Princess of the Dawn')

# If you want to get the first 10 rows starting from the 10th row of the
# result set, you use OFFSET keyword

rs = con.execute("""SELECT TrackId,
                           Name
                      FROM tracks
                     LIMIT 5 OFFSET 3;""")

for i in rs: print(i)
print('-' * 20)

# OUTPUT:
# (4, u'Restless and Wild')
# (5, u'Princess of the Dawn')
# (6, u'Put The Finger On You')
# (7, u"Let's Get It Up")
# (8, u'Inject The Venom')

# The same request in the alternative form

# LIMIT offset, row_count;
rs = con.execute("""SELECT TrackId,
                           Name
                      FROM tracks
                     LIMIT 3, 5;""")


for i in rs: print(i)

# OUTPUT:
# (4, u'Restless and Wild')
# (5, u'Princess of the Dawn')
# (6, u'Put The Finger On You')
# (7, u"Let's Get It Up")
# (8, u'Inject The Venom')

print("-" * 20 + "# 2 Introduction to SQLite LIMIT clause" + "-" * 20)

# We typically use the LIMIT clause with ORDER BY clause, because we
# are interested in getting the number of rows in a specified order,
# not in unspecified order.

# 10 largest track

rs = con.execute("""SELECT TrackId,
                           Name,
                           Bytes
                      FROM tracks
                     ORDER BY Bytes DESC
                     LIMIT 5""")

for i in rs: print(i)

# OUTPUT:
# (3224, u'Through a Looking Glass', 1059546140)
# (2820, u'Occupation / Precipice', 1054423946)
# (3236, u'The Young Lords', 587051735)
# (3242, u'The Man With Nine Lives', 577829804)
# (2910, u'Dave', 574325829)

print("-" * 20 + "# 3 Getting the n-th highest and lowest value" + "-" * 20)


# The following statement returns the third smallest track by time in the tracks table.
# By default the order of ORDER BY is ASC.

rs = con.execute("""SELECT TrackId,
                           Name,
                           Milliseconds
                      FROM tracks
                     ORDER BY MIlliseconds
                     LIMIT 1 OFFSET 2;""")

for i in rs: print(i)

# OUTPUT:
# (170, u'A Statistic', 6373)

