



# MAIN SOURCE:
# http://www.sqlitetutorial.net/sqlite-inner-join/
# We use the DB from here (chinook.db)

# USEFUL LINKS: 
#
# 1) 
#    https://www.w3schools.com/sql/sql_join_inner.asp
#
# 2) Multiple joins
#    https://stackoverflow.com/questions/10195451/sql-inner-join-with-3-tables
#
# 3) Sqlalchemy create_engine() for various databases
#    http://docs.sqlalchemy.org/en/latest/core/engines.html
#

# GENERAL INFORMATION:

# In relational databases, data is often distributed in many related tables. 
# A table is associated with another table using foreign keys.

# To query data from multiple tables, you use INNER JOIN clause. The INNER 
# JOIN clause combines columns from correlated tables.

# SELECT a1, a2, b1, b2
# FROM A
# INNER JOIN B on B.f = A.f;

# For each row in the A table, the INNER JOIN clause compares the value of
# the f column with the value of the f column in the B table. If the value
# of the f column in the A table equals the value of the f column in the B
# table, it combines data from a1, a2, b1, b2, columns and includes this row
# in the result set.

# In other words, the INNER JOIN clause returns rows from the A table that
# has the corresponding row in B table. This logic is applied if you join 
# more than 2 tables.

from sqlalchemy import create_engine

print("-" * 20 + "# 1 SQLite INNER JOIN examples" + "-" * 20)

# sqlite://<nohostname>/<path>, where <path> is relative
engine = create_engine('sqlite:///db_chinook/chinook.db')

tables_names = engine.table_names()

print(tables_names)
# [u'albums', u'artists', u'customers', u'employees', u'genres', 
#  u'invoice_items', u'invoices', u'media_types', u'playlist_track',
#  u'playlists', u'sqlite_sequence', u'sqlite_stat1', u'tracks']

# Open engine connection
con  = engine.connect()

# In the tracks table, the albumid column is a foreign key. And in
# the albums table, the albumid is the primary key.

# Perform query
rs = con.execute("""SELECT TrackId,
                           Name,
                           Title,
                           tracks.AlbumId AS album_id_tracks,
                           albums.AlbumId AS album_id_albums
                      FROM tracks
                     INNER JOIN albums ON tracks.AlbumId = albums.AlbumId;""")

for i in rs: print(i)

# OUTPUT: 
# ... 
# (2268, u'Seven Seas Of Rhye', u'Greatest Hits I', 185, 185)
# (2269, u'We Will Rock You', u'Greatest Hits I', 185, 185)
# (2270, u'We Are The Champions', u'Greatest Hits I', 185, 185)
# (2271, u'We Will Rock You', u'News Of The World', 186, 186)
# (2272, u'We Are The Champions', u'News Of The World', 186, 186)
# ...

# For each row in the tracks table, SQLite uses the value in the
# albumid column of the tracks table to compare with the value in
# the albumid of the albums table. If SQLite finds a match, it
# combines data of rows in both tables in the result set.

print("-" * 20 + "# 2 SQLite inner join 3 tables example" + "-" * 20)

# One track belongs to one album and one album have many tracks. 
# The tracks table associates with the albums table via albumid column.

# One album belongs to one artist and one artist has one or many albums.
# The albums table links to the artists table via artistid column.


# Pay attention that we can join a table ON fields from other tables.
# See how we join tracks and artists below.

con = engine.connect()
rs = con.execute("""SELECT TrackId,
                           tracks.Name,
                           Title,
                           artists.Name
                      FROM tracks
                     INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
                     INNER JOIN artists ON albums.ArtistId = artists.ArtistId
                     WHERE artists.ArtistId = 10;""")

for i in rs: print(i)

# OUTPUT:
# ...
# (125, u'Spanish moss-"A sound portrait"-Spanish moss', u'The Best Of Billy Cobham', u'Billy Cobham')
# (126, u'Moon germs', u'The Best Of Billy Cobham', u'Billy Cobham')
# (127, u'Stratus', u'The Best Of Billy Cobham', u'Billy Cobham')
# ...


