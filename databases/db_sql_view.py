

# MAIN SOURCE:
# http://www.sqlitetutorial.net/sqlite-create-view/ 
# We use the DB from here (chinook.db)

# USEFUL LINKS: 



# GENERAL INFORMATION:

# In database theory, a view is a result set of a stored query. A view is the
# way to pack a query into a named object. You can access the data of the
# underlying tables through the view. The tables that the query in the view
# definition refers to are called base tables.

# A view is useful in some cases:
# - First, views provide an abstraction layer over tables. You can add and
#   remove the columns in the view without touching the schema of the
#   underlying tables.
# - Second, you can use views to encapsulate complex queries with joins to
#   simplify the data access.

# SQLite view is read only. It means you cannot use INSERT, DELETE, and UPDATE
# statement to update data in the base tables through the view.

# To create a view, you use the CREATE VIEW statement as follows:

# CREATE [TEMP] VIEW [IF NOT EXISTS] view_name(column-name-list)
# AS 
#     select-statement;

# The IF NOT EXISTS option helps you prevent an error of creating a view that
# already exists.

# Second, if you want the view to be only visible in the current database
# connection, you need to create a temporary view using the TEMP or TEMPORARY
# option. SQLite automatically removes the temporary views whenever the database
# connection is closed.

# Third, you specify the SELECT statement for the view. By default, the columns
# of the view derive from the result set of the SELECT statement. However, you
# can use different columns for the view by specifying the columns (column-name-list)
# explicitly after the view's name.



import sys
import os

from sqlalchemy import create_engine

print("-" * 20 + "# 1 SQLite CREATE VIEW example" + "-" * 20)

engine = create_engine('sqlite:///db_chinook/chinook.db')
con = engine.connect()

rs = con.execute("""DROP VIEW IF EXISTS v_tracks""")

rs = con.execute("""CREATE VIEW v_tracks
                    AS
                    SELECT 
                     TrackId,
                     tracks.Name,
                     albums.Title AS album,
                     media_types.Name AS media,
                     genres.Name AS genres
                    FROM
                     tracks
                    INNER JOIN albums ON albums.AlbumId = tracks.AlbumId
                    INNER JOIN media_types ON media_types.MediaTypeId = tracks.MediaTypeId
                    INNER JOIN genres ON genres.GenreId = tracks.GenreId;""")

rs = con.execute("""SELECT *
                    FROM v_tracks LIMIT 5;""")

for i in rs: print(i)

# (1, u'For Those About To Rock (We Salute You)', u'For Those About To Rock We Salute You', u'MPEG audio file', u'Rock')
# (6, u'Put The Finger On You', u'For Those About To Rock We Salute You', u'MPEG audio file', u'Rock')
# (7, u"Let's Get It Up", u'For Those About To Rock We Salute You', u'MPEG audio file', u'Rock')
# (8, u'Inject The Venom', u'For Those About To Rock We Salute You', u'MPEG audio file', u'Rock')
# (9, u'Snowballed', u'For Those About To Rock We Salute You', u'MPEG audio file', u'Rock')






