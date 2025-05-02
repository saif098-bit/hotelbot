import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect("hostel_chatbot.db")
cursor = conn.cursor()

# Create the FAQ table if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS FAQ (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
)
''')

# Insert some sample data
cursor.executemany('INSERT INTO FAQ (question, answer) VALUES (?, ?)', [
    ("What are breakfast timings?", "Breakfast is served from 7:00 AM to 9:00 AM."),
    ("Is Wi-Fi available?", "Yes, free Wi-Fi is available in all rooms."),
    ("Can I check out late?", "Late check-out is available upon request, subject to availability.")
])

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")
