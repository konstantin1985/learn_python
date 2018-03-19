

# MAIN: https://suhas.org/sqlalchemy-tutorial/
# https://stackoverflow.com/questions/2942485/psql-fatal-ident-authentication-failed-for-user-postgres
# https://stackoverflow.com/questions/36142952/pgadmin-9-5-not-showing-all-databases
# http://www.yolinux.com/TUTORIALS/LinuxTutorialPostgreSQL.html

# 1) Change config file 
# /var/lib/pgsql/data/pg_hba.conf
# I set all identifications to trust (local, IPv4, IPv6)

# 2) Create a database in pgadmin3 GUI
# or
# in CLI: CREATE DATABASE jerry;
# Read here:
# https://www.cyberciti.biz/faq/howto-add-postgresql-user-account/

# 3) Restart server: sudo /etc/init.d/postgresql start

# 4) Check that the database is created on the server

# konstantin@linux-ks:~> psql
# psql: FATAL:  role "konstantin" does not exist
# konstantin@linux-ks:~> psql --username=postgres
# psql (9.2.7)
# Type "help" for help.
# 
# postgres=# \list
#                                   List of databases
#    Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
# -----------+----------+----------+-------------+-------------+-----------------------
#  postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
#  template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
#            |          |          |             |             | postgres=CTc/postgres
#  template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
#            |          |          |             |             | postgres=CTc/postgres
# (3 rows)



import sqlalchemy

def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect('postgres', '', 'postgres')

con = con.connect()

con.execute("""CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255) 
);""")



# Comparison of MySQL, SQLite and PostgreSQL 
# https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems





