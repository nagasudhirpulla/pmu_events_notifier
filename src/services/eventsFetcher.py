import pandas as pd
import datetime as dt
import psycopg2
from src.typeDefs.appConfig import IDbConfig


def getEventsBetween(dbConfig: IDbConfig, startDt: dt.datetime, endDt: dt.datetime) -> pd.DataFrame:
    hostStr = dbConfig["host"]
    dbStr = dbConfig["name"]
    uNameStr = dbConfig["username"]
    dbPassStr = dbConfig["password"]
    dbPort = dbConfig["port"]
    records = pd.DataFrame()
    try:
        # get the connection object
        conn = psycopg2.connect(host=hostStr, dbname=dbStr,
                                user=uNameStr, password=dbPassStr, port=dbPort)
        # get the cursor from connection
        cur = conn.cursor()
        # create the query
        postgreSQL_select_Query = "select * from public.event_logs where event_time \
                                    between %s and %s order by event_time desc, scores desc"

        # execute the query
        cur.execute(postgreSQL_select_Query, (startDt, endDt))

        # fetch all the records from cursor
        records = cur.fetchall()

        # get the column names returned from the query
        colNames = [row[0] for row in cur.description]

        # create a dataframe from the fetched records
        records = pd.DataFrame.from_records(records, columns=colNames)
        # =============================================================================
        # iterate through all the fetched records
        # for rowIter in range(records.shape[0]):
        #   print("datetime = ", records['sch_time'].iloc[rowIter])
        #   print("value = ", records['sch_val'].iloc[rowIter])
        # =============================================================================
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching events data from db", error)
        records = pd.DataFrame()
    finally:
        # closing database connection and cursor
        if(conn):
            # close the cursor object to avoid memory leaks
            cur.close()
            # close the connection object also
            conn.close()
    return records
