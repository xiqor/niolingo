from app_logic import dictionary, database

database.create_tables

new_kata = dictionary.Item(1, 'хирагана', 'す', 'су', 'глоток', '', '2025-08-10 14:35:00')
new_kata.remove()