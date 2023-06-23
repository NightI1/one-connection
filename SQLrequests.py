import psycopg2
import argparse

def main():
    file_name, no_tables = parse_args()
    conn = connect(*data_return(file_name))
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

def data_return(file_name: str):
    with open(file_name, 'r') as info:
        dbname, user, password = info.readline().strip(), info.readline().strip(), info.readline().strip()
    return dbname, user, password

def connect(dbname: str,user: str,password: str):
    con = psycopg2.connect(dbname=dbname, user=user, password=password)
    return con

def sql_request(con):
    cur = con.cursor()
    request = input('sql> ')
    while ';' not in request:
        request.join(input('sql> '))
    cur.execute(request)
    print_request(cur)
    con.close()

def print_request(cur):
    print(cur.fetchall())

def tables(con):
    cur = con.cursor()
    request = '''SELECT table_name FROM information_schema.tables
WHERE table_schema NOT IN ('information_schema','pg_catalog');'''
    cur.execute(request)
    print(*cur.fetchall())
    con.close()



if '__main__' == __name__:
    main()