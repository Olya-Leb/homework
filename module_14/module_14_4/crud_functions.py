import sqlite3

def initiate_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    """)
    connection.commit()
    # for i in range(1, 5):
    #     cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
    #                    (f"{i}", f"Продукт {i}", f"Описание {i}", f"{i}00"))
    # connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    for i in range(1, 5):
        cursor.execute("SELECT title, description, price FROM Products")
    all_products = cursor.fetchall()
    connection.close()
    return all_products

def main():
    # initiate_db()
    print(get_all_products())

if __name__ == "__main__":
    main()
