import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def execute_query(conn, query, params=None):
    cur = conn.cursor()
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)
    conn.commit()
    return cur

def fetch_all(cur):
    return cur.fetchall()

def create_tables(conn):
    create_books_table = """
    CREATE TABLE IF NOT EXISTS Books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author TEXT NOT NULL,
        title TEXT NOT NULL,
        publish_year INTEGER NOT NULL
    );
    """
    create_readers_table = """
    CREATE TABLE IF NOT EXISTS Readers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """
    create_records_table = """
    CREATE TABLE IF NOT EXISTS Records (
        reader_id INTEGER,
        book_id INTEGER,
        taking_date TEXT NOT NULL,
        returning_date TEXT,
        FOREIGN KEY (reader_id) REFERENCES Readers(id),
        FOREIGN KEY (book_id) REFERENCES Books(id)
    );
    """
    execute_query(conn, create_books_table)
    execute_query(conn, create_readers_table)
    execute_query(conn, create_records_table)

def print_books(conn):
    cur = execute_query(conn, "SELECT * FROM Books")
    books = fetch_all(cur)
    for book in books:
        print(f"ID: {book[0]}, Author: {book[1]}, Title: {book[2]}, Year: {book[3]}")

def print_readers(conn):
    cur = execute_query(conn, "SELECT * FROM Readers")
    readers = fetch_all(cur)
    for reader in readers:
        print(f"ID: {reader[0]}, Name: {reader[1]}")

def add_book(conn, author, title, publish_year):
    query = "INSERT INTO Books (author, title, publish_year) VALUES (?, ?, ?)"
    execute_query(conn, query, (author, title, publish_year))

def add_reader(conn, name):
    query = "INSERT INTO Readers (name) VALUES (?)"
    execute_query(conn, query, (name,))

def give_book(conn, reader_id, book_id, taking_date):
    query = "INSERT INTO Records (reader_id, book_id, taking_date) VALUES (?, ?, ?)"
    execute_query(conn, query, (reader_id, book_id, taking_date))

def return_book(conn, reader_id, book_id, returning_date):
    query = "UPDATE Records SET returning_date = ? WHERE reader_id = ? AND book_id = ? AND returning_date IS NULL"
    execute_query(conn, query, (returning_date, reader_id, book_id))

def main():
    conn = create_connection("library.db")
    create_tables(conn)  # Создаем таблицы, если они не существуют

    while True:
        print("\n1. Вывести список книг")
        print("2. Вывести список читателей")
        print("3. Добавить книгу")
        print("4. Добавить читателя")
        print("5. Выдать книгу читателю")
        print("6. Принять книгу")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            print_books(conn)
        elif choice == '2':
            print_readers(conn)
        elif choice == '3':
            author = input("Автор: ")
            title = input("Название: ")
            publish_year = input("Год издания: ")
            add_book(conn, author, title, publish_year)
        elif choice == '4':
            name = input("Имя читателя: ")
            add_reader(conn, name)
        elif choice == '5':
            reader_id = input("ID читателя: ")
            book_id = input("ID книги: ")
            taking_date = input("Дата выдачи (ГГГГ-ММ-ДД): ")
            give_book(conn, reader_id, book_id, taking_date)
        elif choice == '6':
            reader_id = input("ID читателя: ")
            book_id = input("ID книги: ")
            returning_date = input("Дата возврата (ГГГГ-ММ-ДД): ")
            return_book(conn, reader_id, book_id, returning_date)
        elif choice == '7':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    conn.close()

if __name__ == "__main__":
    main()