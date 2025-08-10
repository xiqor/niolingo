import sqlite3

def get_connection():
    return sqlite3.connect('niolingo_db.db')

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Items (
            id INTEGER PRIMARY KEY,
            type TEXT NOT NULL,
            spelling TEXT,
            transcription TEXT,
            meaning TEXT,
            note TEXT,
            added_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    connection.commit()
    connection.close()

def add_item(item):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO Items (id, type, spelling, transcription, meaning, note, added_at)
        VALUES (?, ?, ?, ?, ?, ?, ?);
    ''', (item.id, item.type, item.spelling, item.transcription, item.meaning, item.note, item.added_at))
    connection.commit()
    connection.close()