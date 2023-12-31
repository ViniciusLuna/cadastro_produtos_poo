import os
import platform
from prettytable import PrettyTable

from models.produtos import Produtos

def limpar_tela():
    #Verifica o sistema operacional
    if platform.system() == "Windowns":
        os.system('cls')
    else:
        os.system('clear')

def imprimir_tabela():
    tabela = PrettyTable()
    tabela.field_names = ["Nome", "Preço", "Quantidade"]

    #adciona linhas a tabela
    for produto in Produtos:
        tabela.add_row([produto.nome, produto.preco, produto.quantidade])

    #Exibindo a tabela
    print(tabela)