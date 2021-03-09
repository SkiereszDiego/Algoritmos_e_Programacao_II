'''
Construir um algoritmo que contenha 3 listas:
    Nomes de produtos
    Precos de cada produtos
    Quantidade de cada produto
Construir uma funcao para imprimir um dos produtos 
da lista e uma funcao para retirar um dos produtos das listas
'''
#----------------LISTAS----------------
nome_de_produtos= ['LACTA', 'MMS', 'TWIX', 'FANDANGOS']
preco_de_cada_produto=[4.50, 2.99, 4.00, 5.50]
quantidade_de_cada_produto=[2, 5, 20, 2]

#----------------FUNCOES----------------

def menu_principal():
    while True:
        print('Atividade 01')
        escolha = input('''{}Menu{}{}
0-	Finalizar o Programa
1-	Imprimir Produto
2-	Remover Produto
{}{}Escolha: {}'''.format('\033[1;31m', '\033[m','\033[1;30m', '\033[m','\033[1;31m', '\033[m'))
        if escolha == "0": break
        elif escolha == '1': imprimir_produto()
        elif escolha == '2': remover_produto()
        else: input('Opção inválida. [Enter] para voltar') 

def menu_produtos():
    print ('\n----Lista de Produtos----')
    for index, item in enumerate(nome_de_produtos):
        print (index, item)

def index_in_list(list, index):
    return (index < len(list))
    
def imprimir_produto():
    menu_produtos()
    while True:
        indice=int(input('\nDigite o número do produto: '))
        if index_in_list(nome_de_produtos, indice):
            print('\nProduto: %s \nPreço: %s \nQuantidade: %s\n' % (nome_de_produtos[indice],
            preco_de_cada_produto[indice],quantidade_de_cada_produto[indice]))
            break
        else: input('{}Opção inválida.{} [Enter] para voltar'.format('\033[1;31m', '\033[m'))
             
def remover_produto():
    while True:
        menu_produtos()
        remover=int(input('\nDigite o número do produto para remover: '))
        if index_in_list(nome_de_produtos, remover):
            item_removido = nome_de_produtos.pop(remover)
            print('\nProduto: {} \nRemovido com Sucesso!\n'.format(item_removido))
            del preco_de_cada_produto[remover]
            del quantidade_de_cada_produto[remover]
            break
        else: input('{}Produto não cadsatrado.{} [Enter] para voltar'.format('\033[1;31m', '\033[m'))
#----------------MAIN----------------
menu_principal()


