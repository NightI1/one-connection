import psycopg2
import argparse


def main():
    conn = connect(*readfile(read()))
    all_table(conn)

def read():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=str)
    args = parser.parse_args()
    return args.p
def readfile(file_name):
    with open(file_name, 'r') as info:
        dbname, user, password = info.readline().strip(), info.readline().strip(), info.readline().strip()
    return dbname, user, password

def connect(dbname,user,password):
    con = psycopg2.connect(dbname=dbname, user=user, password=password)
    return con

def all_table(con):
    cur = con.cursor()
    cur.execute('''SELECT table_name FROM information_schema.tables
WHERE table_schema NOT IN ('information_schema','pg_catalog');''')
    print(*cur.fetchall())
    con.close()



if '__main__' == __name__:
    main()
