import sqlite3

conn = sqlite3.connect('crime_data.db')
cursor = conn.cursor()

# Check existing tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in DB:", tables)

# Check row count if the table exists
if ('crime_table',) in tables:
    cursor.execute("SELECT COUNT(*) FROM crime_table;")
    print("Rows in crime_table:", cursor.fetchone()[0])
else:
    print("crime_table does not exist!")

conn.close()
