import sqlite3
class Produtos:
    
    def __init__(self, id = 0, nome="", preco=0, quantidade=0):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    produtos = []

    def incluir(self):
        conn = sqlite3.connect('db/cadastro_de_produtos.db')
        cursor = conn.cursor()
        #Insert no sqlite
        cursor.execute('INSERT INTO produtos (id, nome, preco, quantidade) VALUES (?, ?, ?)', (self.nome, self.preco, self.quantidade))

        conn.commit()
        conn.close
    
    @staticmethod
    def todos():
        #select no sqlite
        conn = sqlite3.connect('db/cadastro_de_produtos.db')
        cursor = conn.cursor
        cursor.execute('SELECT * from produtos')
        produtos_db = cursor.fetchall()
        conn.close
        #precisa retornar os dados tipados com obj produto
        
        return [Produtos(id=id, nome=nome, preco=preco, quantidade=quantidade) for id, nome, preco, quantidade in produtos_db]