import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

print("Содержимое таблицы Books:")
cursor.execute("SELECT * FROM Books")
books = cursor.fetchall()
for book in books:
    print(book)

print("\nСодержимое таблицы Readers:")
cursor.execute("SELECT * FROM Readers")
readers = cursor.fetchall()
for reader in readers:
    print(reader)

print("\nСодержимое таблицы Records:")
cursor.execute("SELECT * FROM Records")
records = cursor.fetchall()
for record in records:
    print(record)

conn.close()