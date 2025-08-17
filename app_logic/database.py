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
            added_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    connection.commit()
    connection.close()

def add_item(item):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO Items (id, type, spelling, transcription, meaning)
        VALUES (NULL, ?, ?, ?, ?);
    ''', (item.type, item.spelling, item.transcription, item.meaning))
    connection.commit()
    connection.close()

def remove_item(item):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        DELETE FROM Items
        WHERE id = ?;
    ''', (item.id,))
    connection.commit()
    connection.close()