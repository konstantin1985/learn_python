
# MAIN SOURCE:
# http://www.sqlitetutorial.net/sqlite-group-by/ 
# We use the DB from here (chinook.db)
#
# USEFUL LINKS: 
# 
# 1) Join several tables
#    https://stackoverflow.com/questions/10195451/sql-inner-join-with-3-tables

# GENERAL INFORMATION:

# The GROUP BY clause is an optional clause of the SELECT statement. The GROUP BY
# clause groups a selected group of rows into summary rows by values of one or 
# more columns.

# The GROUP BY clause returns one row for each group. For each group, you can 
# apply an aggregate function such as MIN, MAX, SUM, COUNT, or AVG to provide
# more information about each group.

import os
import sqlite3

print("-" * 20 + "# 1 SQLite GROUP BY clause with COUNT function" + "-" * 20)

# The following statement returns the album id and the number of tracks per album.
# It uses the GROUP BY clause to groups tracks by album and apply the COUNT
# function to each group.

db_path = os.path.join('db_chinook', 'chinook.db')

conn = sqlite3.connect(db_path)

with conn:
    
    curs = conn.execute("""SELECT AlbumId,
                                  COUNT(TrackId)
                             FROM tracks 
                            GROUP BY AlbumId;""")  
    
    for i in curs: print(i)
    print('-' * 20)
    # OUTPUT: 
    # (1, 10)
    # (2, 1)
    # (3, 3)
    # (4, 8)
    # (5, 15)

#You can use the ORDER BY clause to sort the groups as follows:

    curs = conn.execute("""SELECT AlbumId,
                                  COUNT(TrackId)
                             FROM tracks
                            GROUP BY AlbumId
                            ORDER BY COUNT(TrackId) DESC;""") 
    
    for i in curs: print(i)
    # OUTPUT:
    # (141, 57)
    # (23, 34)
    # (73, 30)
    # (229, 26)
    # (230, 25)
                             
print("-" * 20 + "# 2 SQLite GROUP BY clause and INNER JOIN clause" + "-" * 20)

# You can query data from multiple tables using INNER JOIN clause, then use
# the GROUP BY clause to group rows into a set of summary rows.

# For example, the following statement joins the tracks table with the albums
# table to get the album's titles and uses the GROUP BY clause wit the COUNT
# function to get the number of tracks per album.

db_path = os.path.join('db_chinook', 'chinook.db')
conn = sqlite3.connect(db_path)

with conn:
    
    curs = conn.execute("""SELECT tracks.AlbumId,
                                  albums.Title,
                                  COUNT(tracks.TrackId)
                             FROM tracks
                            INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
                            GROUP BY tracks.AlbumId;""")
    
    for i in curs: print(i)
    # OUTPUT:
    # (1, u'For Those About To Rock We Salute You', 10)
    # (2, u'Balls to the Wall', 1)
    # (3, u'Restless and Wild', 3)
    # (4, u'Let There Be Rock', 8)
    # ...

    
print("-" * 20 + "# 2 SQLite GROUP BY with HAVING clause" + "-" * 20)

db_path = os.path.join('db_chinook', 'chinook.db')
conn = sqlite3.connect(db_path)

with conn:
    
    # TrackId and Title can be unqualified, because they are
    # unambiguous 
    curs = conn.execute("""SELECT tracks.AlbumId,
                                  Title,
                                  COUNT(TrackId)
                             FROM tracks
                            INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
                            GROUP BY tracks.AlbumId
                            HAVING COUNT(TrackId) > 20;""")

    for i in curs: print(i)
    # OUTPUT:
    # (23, u'Minha Historia', 34)
    # (24, u'Afrociberdelia', 23)
    # (39, u'International Superhits', 21)
    # (51, u"Up An' Atom", 22)
    # (73, u'Unplugged', 30)
    # ... 
    
    
    
print("-" * 20 + "# 3 SQLite GROUP BY clause with SUM function example" + "-" * 20)

# You can use the SUM function to calculate total per group. For example,
# to get total length and bytes for each album, you use the SUM function
# to calculate total milliseconds and bytes.

db_path = os.path.join('db_chinook', "chinook.db")
conn = sqlite3.connect(db_path)

with conn:
    
    curs = conn.execute("""SELECT AlbumId,
                                  SUM(Milliseconds),
                                  SUM(Bytes)
                             FROM tracks
                            GROUP BY AlbumId;""")

    for i in curs: print(i)
    # OUTPUT:
    # (1, 2400415, 78270414)
    # (2, 342562, 5510424)
    # (3, 858088, 14613294)
    # (4, 2453259, 80239024)
    
print("-" * 20 + "# 4 SQLite GROUP BY with MAX, MIN and AVG functions" + "-" * 20)

# The following statement returns the album id, album title, maximum length,
# minimum length, and the average length of tracks in the tracks table.

db_path = os.path.join('db_chinook', "chinook.db")
conn = sqlite3.connect(db_path)

with conn:
    
    # 2 digits in ROUND
    curs = conn.execute("""SELECT tracks.AlbumId,
                                  Title,
                                  MAX(Milliseconds),
                                  MIN(Milliseconds),
                                  ROUND(AVG(Milliseconds), 2)
                             FROM tracks
                            INNER JOIN albums ON tracks.AlbumId = albums.AlbumId    
                            GROUP BY tracks.AlbumId;""")
    
    for i in curs: print(i)
    # OUTPUT:
    # (1, u'For Those About To Rock We Salute You', 343719, 199836, 240041.5)
    # (2, u'Balls to the Wall', 342562, 342562, 342562.0)
    # (3, u'Restless and Wild', 375418, 230619, 286029.33)
    # (4, u'Let There Be Rock', 369319, 215196, 306657.38)
    
    
print("-" * 20 + "# 5 SQLite GROUP BY multiple columns example" + "-" * 20)
    
# In the previous example, we have used one column in the GROUP BY clause. 
# SQLite allows you to group rows by multiple columns.

# For example, to group tracks by media type and genre, you use the
# following statement

db_path = os.path.join('db_chinook', "chinook.db")
conn = sqlite3.connect(db_path)

with conn:
    
    curs = conn.execute("""SELECT MediaTypeId,
                                  GenreId,
                                  COUNT(TrackId)
                             FROM tracks
                            GROUP BY MediaTypeId, GenreId""")

    for i in curs: print(i)
    print('-' * 20)
    # OUTPUT:
    # (1, 1, 1211)
    # (1, 2, 127)
    # (1, 3, 374)
    # (1, 4, 332)

    # If we want to have names of MediaTypeId and GenreId
    
    curs = conn.execute("""SELECT media_types.Name,
                                  genres.Name,
                                  COUNT(TrackId)
                             FROM tracks 
                            INNER JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
                            INNER JOIN genres ON tracks.GenreId = genres.GenreId
                            GROUP BY tracks.MediaTypeId, 
                                     tracks.GenreId;""")
    
    for i in curs: print(i)
    # OUTPUT:
    # (u'MPEG audio file', u'Rock', 1211)
    # (u'MPEG audio file', u'Jazz', 127)
    # (u'MPEG audio file', u'Metal', 374)
    # (u'MPEG audio file', u'Alternative & Punk', 332)

