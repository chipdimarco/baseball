# 11-26-2019, 12-12-2019
# for writing data to database

import psycopg2
import json

'''
PG_USER     = "admin"
PG_DB       = "clibaseball"
PG_PASSWORD = "02468abcd"
PG_HOST     = "localhost"
PG_PORT     = "5432"
'''

#   F U N C T I O N S
#   pass the conn object

def dbq_hr_max( conn, rows ):
    cur = conn.cursor()
    q = "SELECT   boxline.name, boxline.id, SUM (boxline.hr) " \
        "FROM     public.boxline " \
        "GROUP BY boxline.name, boxline.id " \
        "ORDER BY SUM (boxline.hr) DESC;"
    cur.execute(q)
    response = cur.fetchmany(rows)
    cur.close()
    return ( response )

def dbq_h_max( conn, rows ):
    cur = conn.cursor()
    q = "SELECT   boxline.name, boxline.id, SUM (boxline.h) " \
        "FROM     public.boxline " \
        "GROUP BY boxline.name, boxline.id " \
        "ORDER BY SUM (boxline.h) DESC;"
    cur.execute(q)
    response = cur.fetchmany(rows)
    cur.close()
    return ( response )

def dbq_avg_max( conn, rows, min_ab ):
    cur = conn.cursor()
    q = "SELECT   boxline.name, boxline.id, SUM (boxline.h) / NULLIF ( SUM (boxline.ab) ,0)::float AS avg " \
        "FROM     public.boxline " \
        "GROUP BY boxline.name, boxline.id " \
        "HAVING   SUM (boxline.ab) > %s " \
        "ORDER BY avg DESC ;"
    cur.execute(q, (min_ab,))
    response = cur.fetchmany(rows)
    cur.close()
    return ( response )

def dbq_p_k_max( conn, rows ):
    cur = conn.cursor()
    q = "SELECT   pitchingline.name, pitchingline.id, SUM (pitchingline.k) " \
        "FROM     public.pitchingline " \
        "GROUP BY pitchingline.name, pitchingline.id " \
        "ORDER BY SUM ( pitchingline.k ) DESC;"
    cur.execute(q)
    response = cur.fetchmany(rows)
    cur.close()
    return ( response )




'''
if __name__ == "__main__":
    main()
'''
#exit()

'''
# database
conn = psycopg2.connect(
    dbname   = PG_DB,
    user     = PG_USER,
    password = PG_PASSWORD,
    host     = PG_HOST,
    port     = PG_PORT
    )

# Open a cursor to perform database operations
cur = conn.cursor()


TEAM = "BOS"
GAME = 1

for x in data:
    v = (
        TEAM, x["NAME"], x["ID"], x["AB"], x["H"], x["BB"], x["HR"], GAME
    )
    insert_record( cur, v )

#   W R A P   U P
# Make the changes to the database persistent
conn.commit()

#closing database connection.
if(conn):
    cur.close()
    conn.close()
    print("PostgreSQL connection is closed")
'''


# Print PostgreSQL Connection properties
#print ( conn.get_dsn_parameters(),"\n")


"""
# INSERT A RECORD
postgres_insert_query =(
'''
INSERT INTO BOXLINE (TEAM, NAME, ID, AB, H, BB, HR, fk_game) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )
''')

record_to_insert = ( "Brantley", 10384, 4, 1, 0, 0)

try:
    cur.execute(postgres_insert_query, record_to_insert)
except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while inserting data into PostgreSQL table", error)
"""


"""  CREATE A TABLE
# Execute a command: this creates a new table
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# CREATE the table BOXLINE    
create_table_query = (
    '''CREATE TABLE BOXLINE 
    ( pk_boxline serial PRIMARY KEY,
    NAME varchar,
    ID integer,
    AB integer,
    H integer,
    BB integer,
    HR integer
    );'''
) 

try:
    cur.execute( create_table_query )
except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)

"""

"""
# database
conn = psycopg2.connect(
    dbname   = PG_DB,
    user     = PG_USER,
    password = PG_PASSWORD,
    host     = PG_HOST,
    port     = PG_PORT
    )

# Open a cursor to perform database operations
cur = conn.cursor()


TEAM = "BOS"
GAME = 1

for x in data:
    v = (
        TEAM, x["NAME"], x["ID"], x["AB"], x["H"], x["BB"], x["HR"], GAME
    )
    insert_record( cur, v )

#   W R A P   U P
# Make the changes to the database persistent
conn.commit()

#closing database connection.
if(conn):
    cur.close()
    conn.close()

"""

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
#cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))

# Query the database and obtain data as Python objects
#cur.execute("SELECT * FROM test;")
#result = cur.fetchone()
#(1, 100, "abc'def")
#print (result)



