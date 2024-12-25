import  _sqlite3

db_path = "/Users/mac/my_new_database.db"

try:
    conn = _sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test (name) VALUES (?)", ("Example",))
    conn.commit()

    # Fetch data
    cursor.execute("SELECT * FROM test")
    print(cursor.fetchall())
finally:
    conn.close()