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

def remove_item(item_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        DELETE FROM Items
        WHERE id = ?;
    ''', (item_id))
    connection.commit()
    connection.close()

def update_item(item_id, new_item):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE Items
        SET type = ?, spelling = ?, transcription = ?, meaning = ?
        WHERE id = ?;
    ''', (new_item.type, new_item.spelling, new_item.transcription, new_item.meaning, item_id))
    connection.commit()
    connection.close()

def get_item(param):
    connection = get_connection()
    cursor = connection.cursor()
    if param:
        cursor.execute('''
            SELECT id, type, spelling, transcription, meaning, added_at
            FROM Items
            WHERE spelling = ? OR meaning = ?;
        ''', (param, param))
    else:
        cursor.execute('''
            SELECT *
            FROM Items
        ''')
    rows = cursor.fetchall()
    connection.close()
    return rows
