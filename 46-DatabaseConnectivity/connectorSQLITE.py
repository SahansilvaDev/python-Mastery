import sqlite3

# Connect to a database (creates the file if it doesn't exist)
conn = sqlite3.connect('46-DatabaseConnectivity/example.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create a table
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Insert data
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 25))
conn.commit()  # Save (commit) the changes

# Query data
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()

'''
To connect to an SQLite database in Python, use the built-in sqlite3 module. Here’s a simple example:


Key points:

sqlite3.connect('example.db') connects to (or creates) a database file.
Use cursor() to execute SQL commands.
Always commit() after changes.
Use close() to end the connection.


'''