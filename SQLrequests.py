import psycopg2
import argparse


def main():
    file_name, no_tables = parse_args()
    conn = connect(*readfile(file_name))
    if no_tables:
        sql_request(conn)
    else:
        tables(conn)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', action='store_true')
    parser.add_argument('-p', type=str)
    args = parser.parse_args()
    return args.p, args.a

def readfile(file_name):
    with open(file_name, 'r') as info:
        dbname, user, password = info.readline().strip(), info.readline().strip(), info.readline().strip()
    return dbname, user, password

def connect(dbname: str,user: str,password: str):
    con = psycopg2.connect(dbname=dbname, user=user, password=password)
    return con

def sql_request(con):
    cur = con.cursor()
    request = input('sql> ')
    while ';' not in request[-1]:
        request = request+' ' + input('sql> ')
    cur.execute(request)
    print(cur.fetchall())
    con.close()

def tables(con):
    cur = con.cursor()
    cur.execute('''SELECT table_name FROM information_schema.tables
WHERE table_schema NOT IN ('information_schema','pg_catalog');''')
    print(*cur.fetchall())
    con.close()



if '__main__' == __name__:
    main()