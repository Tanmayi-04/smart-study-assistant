import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the 'users' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    hallticket TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    branch TEXT NOT NULL
)
''')

# Sample user entries
users = [
    ('22EG112D09', 'pass123', 'CSE'),
    ('22EG112D59', 'mypassword', 'IT'),
    ('22EG112D49', 'ece2025', 'ECE')
]


# Insert users (ignores if already present)
cursor.executemany('INSERT OR IGNORE INTO users VALUES (?, ?, ?)', users)

# Save and close
conn.commit()
conn.close()

print("Database initialized and users added.")
