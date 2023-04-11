from random import choice
from time import sleep

Max_linhas = 3
Max_aposta = 100
Min_aposta = 1


Dlinha = 3
Dcoluna = 3


cores = {'Vermelho': '\033[1;31m',
         'Limpa': '\033[m',
         'Amarelo': '\033[1;33m',
         'Verde': '\033[1;32m'}

simbolo_conta = {
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 8
}

simbolo_valor = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def mensagem_inicial():
    print('~' * 102)
    print('\033[1;32m{: ^100}\033[m'.format('Máquina Caça-níqueis simples'))
    sleep(1)
    print('{: ^100}'.format(
        'A maquina roda três vezes, você pode escolher a quantidade de linhas que quer apostar (Vai de 1 a 3)'))
    print('{: ^100}'.format(
        'Caso complete uma linha você recebe o valor que apostou na linha multiplicado pelo simbolo: '))
    print('{: ^100}'.format('Tipos de simbolo'))
    print('{}{:->100}'.format('A ', ' 5 vezes o valor apostado.'))
    print('{}{:->100}'.format('B ', ' 4 vezes o valor apostado.'))
    print('{}{:->100}'.format('C ', ' 3 vezes o valor apostado.'))
    print('{}{:->100}'.format('D ', ' 2 vezes o valor apostado.'))

    print('')
    sleep(1)
    print('~' * 102)


def Chegar_vencedor(colunas, linhas, aposta, valores):
    vencedor = 0
    vencedor_e_linhas = []
    for linha in range(linhas):
        simbolo = colunas[0][linha]
        for coluna in colunas:
            simbolo_p_checar = coluna[linha]
            if simbolo != simbolo_p_checar:
                break
        else:
            vencedor += valores[simbolo] * aposta
            vencedor_e_linhas.append(linhas + 1)
    return vencedor, vencedor_e_linhas


def c_niqueis(Dlinha, Dcoluna,simbolos):

    todos_simbolos = []
    for simbolo, simbolo_conta in simbolos.items():
        for c in range(simbolo_conta):
            todos_simbolos.append(simbolo)
    colunas = []
    for c in range(Dcoluna):
        coluna = []
        simbolos_atuais = todos_simbolos[:]

        for c in range(Dlinha):
            valor = choice(simbolos_atuais)
            simbolos_atuais.remove(valor)
            coluna.append(valor)
        colunas.append(coluna)
    return colunas


def print_cniqueis(colunas):
    print()
    cores1 = ['\033[1;32m', '\033[1;31m', '\033[1;34m', '\033[m']
    for linha in range(len(colunas[0])):
        for c, coluna in enumerate(colunas):
            if c != len(colunas) - 1:
                print(cores1[linha], coluna[linha], cores1[3], end=" | ")
            else:
                print(cores1[linha], coluna[linha], cores1[3], end=" ")
            sleep(0.5)
        print()


def deposito():
    while True:
        montante = input("Quanto você quer depositar: \033[0;32mR$\033[m")
        if montante.isdigit():
            montante = int(montante)
            if montante > 0:
                break
            else:
                print("O valor deve ser maior que zero")
        else:
            print("Por favor entre com um valor...")
    return montante


def pegue_num_de_linha():
    while True:

        linhas = input("Entre com o número de linhas que você quer apostar 1-" + str(Max_linhas) + ")? ")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= Max_linhas:
                break
            else:
                print("Entre com um número válido de linhas")
        else:
            print("Por favor entre com um valor")
    return linhas


def pegue_aposta():
    while True:
        montante = input("Quanto você quer apostar em cada linha? \033[0;32mR$\033[m")
        if montante.isdigit():
            montante = int(montante)
            if Min_aposta <= montante <= Max_aposta:
                break
            else:
                print(f"O valor da aposta deve ser entre \033[0;32mR$\033[m{Min_aposta} - \033[0;32mR$\033[m{Max_aposta}")
        else:
            print("Por favor entre com um valor")
    return montante


def rodar(montante):
    linhas = pegue_num_de_linha()
    while True:
        aposta = pegue_aposta()
        total_aposta = aposta * linhas
        if total_aposta > montante:
            print(f'Você não tem valor suficiente, seu montante atual e: R${montante}')
        else:
            break

    print(f'Você está apostando R${aposta} em {linhas} linhas. Total da sua aposta é igual a: R${total_aposta}')

    slots = c_niqueis(Dlinha, Dcoluna, simbolo_conta)
    print_cniqueis(slots)
    vencedor, vencedor_e_linhas = Chegar_vencedor(slots, linhas, aposta, simbolo_valor)
    print()
    print(f'você ganhou R$ {vencedor}.')

    print()
    print(f'Você ganhou nas linhas: ', *vencedor_e_linhas)
    sleep(1)
    return vencedor - total_aposta


def principal():
    VTotal = cont = 0
    mensagem_inicial()
    montante = deposito()
    VTotal += montante
    while True:
        resposta = verifica = str
        condicional = False
        print(f"O atual montante é: \033[0;32mR$\033[m{montante}")

        while cont > 0:
            print()
            verifica = input('Você quer depositar mais dinheiro pressione ( S ) para sim ou ( N ) para não?').upper()[0]
            if verifica == 'S':
                condicional = True
                break
            elif verifica == "N":
                condicional = False
                break
        if condicional:
            montante += deposito()
            print(f"Seu montante agora é de: \033[0;32mR$\033[m{montante}")
            print()

        while resposta != 'S' and resposta != 'N':
            print()
            resposta = str(input('Pressione ( S ) para iniciar jogada ou ( N ) para sair. ')).upper()[0]

        if resposta == "N":
            break
        montante += rodar(montante)
        cont += 1

    print(f'você saiu do jogo com \033[0;32mR$\033[m{montante}')
    if montante > VTotal:
        print(f'você teve um lucro de \033[0;32mR$\033[m{montante - VTotal}')
    elif VTotal > montante:
        print(f'Você teve um prejuíjo de \033[0;32mR$\033[m{VTotal - montante}')
    else:
        print(f'Você saiu com o mesmo valor que entrou \033[0;32mR$\033[m{montante}')



principal()