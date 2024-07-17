import psycopg2
from contextlib import contextmanager

@contextmanager
def DbConnect():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="your_database",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        yield conn
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

create_table_query = """
CREATE TABLE IF NOT EXISTS Product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    color VARCHAR(50),
    image VARCHAR(255)
);
"""

with DbConnect() as conn:
    with conn.cursor() as cursor:
        cursor.execute(create_table_query)
        conn.commit()
    print("Product table created successfully.")
