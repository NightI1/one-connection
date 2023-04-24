import psycopg2


def con():
    global conn
    conn = psycopg2.connect(dbname='main', user='postgres', password='admin')
    return conn

def curs():
    return con().cursor()


def all_table():
    with curs() as cursor:
        cursor.execute('''SELECT table_name FROM information_schema.tables
WHERE table_schema NOT IN ('information_schema','pg_catalog');''')
        print(*cursor.fetchall())
    conn.close()



all_table()
