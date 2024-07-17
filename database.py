import psycopg2

db_params = {
    'database': '6',
    'user': 'postgres',
    'password': '1202',
    'host': 'localhost',
    'port': 5432
}

class DBConnect:
    def __init__(self, params):
        self.params = params

    def __enter__(self):
        self.connection = psycopg2.connect(**self.params)
        self.cursor = self.connection.cursor()
        return self.connection, self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

with DBConnect(db_params) as (conn, cur):
    update_query = '''UPDATE book SET description = 'hello' WHERE id = 1;'''
    cur.execute(update_query)
    conn.commit()
