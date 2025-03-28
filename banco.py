import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        concluida INTEGER DEFAULT 0
    )
''')

conn.commit()
conn.close()

print('banco de dados criado com sucesso')
