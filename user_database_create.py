import sqlite3

conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Try to create table
try:
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            authority TEXT NOT NULL
        )
    ''')
except sqlite3.OperationalError:
    print("Table already exists.")

# Define users
users = [
    ('adityaanand', 'adityaanand', 'student'),
    ('teacher1', 'teacher1', 'teacher'),
    ('teacher2', 'teacher2', 'teacher'),
    ('teacher3', 'teacher3', 'teacher'),
    ('teacher4', 'teacher4', 'teacher'),
    ('teacher5', 'teacher5', 'teacher'),
    ('teacher6', 'teacher6', 'teacher'),
    ('hod', 'hod', 'hod'),
    ('admin', 'admin', 'admin')
]

# Insert users, skip if already exists
for user in users:
    try:
        cursor.execute("INSERT INTO users (username, password, authority) VALUES (?, ?, ?)", user)
    except sqlite3.IntegrityError:
        print(f"User {user[0]} already exists. Skipping...")

conn.commit()
conn.close()
