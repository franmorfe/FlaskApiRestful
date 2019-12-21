import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = '''CREATE TABLE users (id int, username text, password text)'''
cursor.execute(create_table)

user = (1, 'test 1', '123456')
insert_query = '''INSERT INTO users VALUES (?, ?, ?)'''
cursor.execute(insert_query, user)

users = [
    (2, "test 2", "123456"),
    (3, "test 3", "123456")
]

cursor.executemany(insert_query, users)

select_query = '''SELECT * FROM users'''
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()