import time
from models.produtos import Produtos
import utils

def cadastrar():
    nome = input('Nome do produto\n')
    produto_encontrado = False
    for produto in Produtos.todos():
        if produto.nome == nome:
            print(f"O produto {nome}, ja foi cadastrado")
            produto.quantidade = int(produto["quantidade"]) + int(input(f"Digite a quantidade a acresentar no {nome}\n"))
            produto_encontrado = True
            utils.limpar_tela()
            print("Produto foi atualizado com sucesso !")
            time.sleep(2)
            utils.limpar_tela()
            break
    if produto_encontrado:
        return
produto = Produtos()
produto.nome = nome
produto.preco = input('Preço do produto\n')
produto.quantidade = input('Quantidade do produto\n')
produto.incluir()

utils.limpar_tela()
print("\033[92mProduto cadastrado com sucesso !\033[0m")
time.sleep(2)
utils.limpar_tela()

def listar():
    if len(Produtos.todos()) == 0:
        print("Nenhum produto cadastrado !")
        time.sleep(2)
        utils.limpar_tela()
    else:
        utils.imprimir_tabela(Produtos.todos())

        input("Digite enter para continuar ...")
        utils.limpar_tela()
