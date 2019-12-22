# 11-26-2019, 12-12-2019
# for writing data to database

import psycopg2
import json

import db_queries as dbq

PG_USER     = "admin"
PG_DB       = "clibaseball"
PG_PASSWORD = "02468abcd"
PG_HOST     = "localhost"
PG_PORT     = "5432"


#   F U N C T I O N S


def save_box_to_db(box, game_number):
    TEAM = box.team
    #return(True)
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
    # Parse lineup data into records
    alllines = []
    boxlines = []
    processedids = []
    
    for inning in box.lineup:
        for i in inning:
            alllines.append(i)
    for i in alllines:
        if i["ID"] in processedids:
            pass
        else:
            id = i["ID"]
            boxline = {}
            boxline["NAME"] = i["NAME"]
            boxline["POS"] = i["POS"]
            boxline["ID"] = id
            boxline["AB"] = 0
            boxline["H"]  = 0
            boxline["BB"] = 0
            boxline["HR"] = 0
            for j in alllines:
                if j["ID"] == id:
                    boxline["AB"] += j["AB"]
                    boxline["H"]  += j["H"]
                    boxline["BB"] += j["BB"]
                    boxline["HR"] += j["HR"]
            processedids.append(id)
            boxlines.append(boxline)
    for x in boxlines:
        v = ( TEAM, x["NAME"], x["ID"], x["AB"], x["H"], x["BB"], x["HR"], game_number )
        #print ( v )
        insert_record( cur, v )

    # Make the changes to the database persistent
    try:
        conn.commit()
        response = True
    except:
        response = False

    #closing database connection.
    if(conn):
        cur.close()
        conn.close()
    return(response)


def save_pitching_box_to_db(box, game_number):
    TEAM = box.team
    #return(True)
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
    # Parse pitching data into records
    alllines = []
    boxlines = []
    processedids = []
    
    for inning in box.pitching:
        for i in inning:
            alllines.append(i)
    for i in alllines:
        if i["ID"] in processedids:
            pass
        else:
            id = i["ID"]
            boxline = {}
            boxline["NAME"] = i["NAME"]
            boxline["ID"] = id
            boxline["BF"] = 0
            boxline["HA"] = 0
            boxline["K"]  = 0
            boxline["W"]  = 0
            boxline["O"]  = 0
            for j in alllines:
                if j["ID"] == id:
                    boxline["BF"] += 1 #j["BF"]
                    boxline["HA"] += j["HA"]
                    boxline["K"] += j["K"]
                    boxline["W"] += j["W"]
                    boxline["O"] += j["O"]
            processedids.append(id)
            boxlines.append(boxline)
    for x in boxlines:
        v = ( TEAM, x["NAME"], x["ID"], x["BF"], x["HA"], x["K"], x["W"], x["O"], game_number )
        #print (v )
        insert_pitching_record( cur, v )

    # Make the changes to the database persistent
    try:
        conn.commit()
        response = True
    except:
        response = False

    #closing database connection.
    if(conn):
        cur.close()
        conn.close()
    return(response)



def boxline_stats ( box_file ):
    #print ()
    handler = open( box_file ,'r')
    data = handler.read()
    stats=json.loads(data)
    boxlines = []
    processedids = []
    for i in stats:
        if i["ID"] in processedids:
            pass
        else:
            id = i["ID"]
            boxline = {}
#                boxline["BO"] = i["BO"]
            boxline["NAME"] = i["NAME"]
            boxline["POS"] = i["POS"]
            boxline["ID"] = id
            boxline["AB"] = 0
            boxline["H"]  = 0
            boxline["BB"] = 0
            boxline["HR"] = 0
            for j in stats:
                if j["ID"] == id:
                    boxline["AB"] += j["AB"]
                    boxline["H"]  += j["H"]
                    boxline["BB"] += j["BB"]
                    boxline["HR"] += j["HR"]
            processedids.append(id)
            boxlines.append(boxline)
    handler.close()
    return ( boxlines )

def insert_record(cur, v):
    postgres_insert_query =(
    '''
    INSERT INTO BOXLINE (TEAM, NAME, ID, AB, H, BB, HR, fk_game) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )
    ''')
    record_to_insert = v
    try:
        cur.execute(postgres_insert_query, record_to_insert)
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error while inserting data into PostgreSQL table", error)
    return(f'Insert { v[1]}')

def insert_pitching_record(cur, v):
    postgres_insert_query =(
    '''
    INSERT INTO PITCHINGLINE (TEAM, NAME, ID, BF, HA, K, W, O, fk_game) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )
    ''')
    record_to_insert = v
    try:
        cur.execute(postgres_insert_query, record_to_insert)
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error while inserting data into PostgreSQL table", error)
    return(f'Insert { v[1]}')



def main():
    # database
    conn = psycopg2.connect(
        dbname   = PG_DB,
        user     = PG_USER,
        password = PG_PASSWORD,
        host     = PG_HOST,
        port     = PG_PORT
        )

    # Open a cursor to perform database operations
    # cur = conn.cursor()


    print (f"\nHR LEADERS\n==========")
    q = dbq.dbq_hr_max(conn, 10)
    for i in q:
        print (i[0],i[2])

    print (f"\nHITS LEADERS\n============")
    q = dbq.dbq_h_max(conn, 10)
    for i in q:
        print (i[0],i[2])

    print (f"\nAVG LEADERS\n===========")
    q = dbq.dbq_avg_max(conn, 10, 100)
    for i in q:
        print (f'{ i[0]} .{ round(i[2]*1000)}')

    print (f"\nPITCHING K LEADERS\n==================")
    q = dbq.dbq_p_k_max(conn, 10)
    for i in q:
        print (i[0],i[2])


    #   W R A P   U P
    # Make the changes to the database persistent
    conn.commit()

    #closing database connection.
    if(conn):
    #    cur.close()
        conn.close()
        print("PostgreSQL connection is closed")




if __name__ == "__main__":
    main()

