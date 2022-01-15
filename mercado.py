from re import L
from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    '''
    Funcao que mostra o menu para o usuario e executa a funcao correspondente.
    '''
    print('=======================================')
    print('============ Bem vindo (a) ============')
    print('=========== Mercado do Julio ==========')
    print('=======================================')

    print('Selecione um das opções abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')
    
    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos() 
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte Sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção Inválida!')
        sleep(1)
        menu()

def cadastrar_produto() -> None:
    '''
    Funcao que cadastra um produto no sistema.
    '''
    print('Cadastro de Produto')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preco do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produtos() -> None:
    '''
    Funcao que verifica se ha produtos cadastrados e mostra uma lista com todos eles caso existam.
    '''
    if len(produtos) > 0:
        print('Listagem de Produtos')
        print('====================')

        for produto in produtos:
            print(produto)
            print('----------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()

def comprar_produto() -> None:
    '''
    Funcao que verifica se existem produtos cadastrados, mostra a lista de produtos e 
    interage com o usuario pedindo um codigo. Caso o carrinho nao esteja vazio, 
    verifica se o produto ja foi adicionado, se sim, incrementa uma unidade ao carrinho
    do respectivo produto, se nao adiciona o produto ao carrinho.
    Caso o carrinho esteja vazio, cria o carrinho adicionando o primeiro item.
    '''
    if len(produtos) > 0:
        print('Informe o codigo do produto que deseja adicionar ao carrinho: ')
        print('--------------------------------------------------------------')
        print('=================== Produtos Disponíveis =====================')
        for produto in produtos:
            print(produto)
            print('--------------------------------------------------------------')
            sleep(1)
        codigo: int = int(input())
        produto: Produto = pega_produto_codigo(codigo)

        if produto:
            # verificando se o carrinho nao esta vazio
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False

                for item in carrinho: # se eu ja tiver comprado uma unidade do item
                    qtde: int = item.get(produto)
                    if qtde:
                        item[produto] = qtde + 1
                        print(f'O produto {produto.nome} agora possui {qtde + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho: # caso seja a primeira compra do item
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
                
            else: 
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()

    else:
        print('Ainda não existem produtos para vender.')
    sleep(2)
    menu()

def visualizar_carrinho() -> None:
    '''
    Funcao que verifica se o carrinho esta vazio. Caso nao esteja, imprime o carrinho.
    '''
    if len(carrinho) > 0:
        print('Produtos no Carrinho: ')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    '''
    Funcao que verifica todos os produtos selecionados no carrinho, mostra os itens,
    calcula o valor total, mostra ao cliente e, no final, limpa o carrinho.
    '''
    if len(carrinho) > 0:
        valor_total: float = 0
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1] # preco * qtde
                print('------------------------')
                sleep(1)
        print(f'A sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte Sempre!')
        carrinho.clear()
        sleep(5)

    else:
        print('Ainda não existem produtos no carrinho.')
    
    sleep(2)
    menu()


def pega_produto_codigo(codigo: int) -> Produto:
    '''
    Funcao que verifica se o produto esta cadastrado na lista e retorna ele.
    '''
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()
