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


class Product:
    def __init__(self, name, price, color=None, image=None):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
        insert_query = """
        INSERT INTO Product (name, price, color, image)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
        """
        with DbConnect() as conn:
            if conn:
                with conn.cursor() as cursor:
                    cursor.execute(insert_query, (self.name, self.price, self.color, self.image))
                    self.id = cursor.fetchone()[0]
                    conn.commit()
                print(f"Product '{self.name}' saved successfully with ID {self.id}.")
            else:
                print("Failed to connect to the database.")


create_table_query = """
CREATE TABLE Product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    color VARCHAR(50),
    image VARCHAR(255)
);
"""

with DbConnect() as conn:
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(create_table_query)
            conn.commit()
        print("Product table created successfully.")
    else:
        print("Error")

new_product = Product(name="Laptop", price=999.99, color="Silver", image="laptop.png")
new_product.save()
