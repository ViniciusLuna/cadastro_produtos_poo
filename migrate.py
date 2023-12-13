import sqlite3

#cria uma sessao (conexao) 
conn = sqlite3.connect('db/cadastro_de_produtos.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(150) NOT NULL, preco REAL NOT NULL, quantidade INTEGER NOT NULL)')

#commita a transacao

conn.commit
conn.close
