import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

print("Результат FULL OUTER JOIN:")
cursor.execute('''
SELECT Readers.id AS reader_id, Readers.name AS reader_name, Books.id AS book_id, Books.title AS book_title
FROM Readers
LEFT JOIN Records ON Readers.id = Records.reader_id
LEFT JOIN Books ON Records.book_id = Books.id

UNION ALL

SELECT Readers.id AS reader_id, Readers.name AS reader_name, Books.id AS book_id, Books.title AS book_title
FROM Books
LEFT JOIN Records ON Books.id = Records.book_id
LEFT JOIN Readers ON Records.reader_id = Readers.id
WHERE Readers.id IS NULL
''')
full_outer_join_result = cursor.fetchall()
for record in full_outer_join_result:
    print(record)

conn.close()