import utils
import tela_produtos as tela_produtos

while(True):
    print("Selecione a opção abaixo:")
    print("1 - cadastrar produto")
    print("2 - listar produtos")
    print("3 - sair")

    opcao = int(input())
    utils.limpar_tela()

    if opcao == 1:
        tela_produtos.cadastrar()
    elif opcao == 2:
        tela_produtos.listar()
    elif opcao == 3:
        break
