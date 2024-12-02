import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

print("Книги, находящиеся в данный момент на руках у читателей:")
cursor.execute('''
SELECT Books.id, Books.title
FROM Books
JOIN Records ON Books.id = Records.book_id
WHERE Records.returning_date IS NULL
''')
books_on_hand = cursor.fetchall()
for book in books_on_hand:
    print(book)

print("\nИмена читателей и названия книг, которые они когда либо брали:")
cursor.execute('''
SELECT Readers.name, Books.title
FROM Readers
JOIN Records ON Readers.id = Records.reader_id
JOIN Books ON Records.book_id = Books.id
''')
reader_books = cursor.fetchall()
for record in reader_books:
    print(record)

print("\nКоличество книг для каждого автора:")
cursor.execute('''
SELECT author, COUNT(*) AS book_count
FROM Books
GROUP BY author
''')
author_book_count = cursor.fetchall()
for author in author_book_count:
    print(author)

conn.close()