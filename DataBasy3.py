import sqlite3

conn = sqlite3.connect('Notas.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Boletim_Academico (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Aluno TEXT NOT NULL,
    Disciplina TEXT NOT NULL,
    Unidade TEXT NOT NULL,
    Notas TEXT NOT NULL
    
);
""")

print('Conectado ao banco de dados!')