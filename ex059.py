import time

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
e = 0
while e != 5:
    time.sleep(1)
    print('''\033[36m  ESCOLHA:
    [1]Somar
    [2]Multiplicação
    [3]Maior
    [4]Novos números
    [5]Sair do programa
        ''')
    e = int(input('Escolha uma operação: '))
    time.sleep(2)
    print('\033[33m=================')
    if e == 1:
        print('\033[33mADIÇÃO')
        print('\033[34mA soma entre os valores {} e {} é igual a \033[31m{}\033[m.'.format(n1, n2, n1+n2))
    if e == 2:
        print('\033[33mMULTIPLICAÇÃO')
        print('\033[34mA multiplicação dos valores {} e {} é igual a \033[31m{}\033[m.'.format(n1, n2, n1*n2))
    if e == 3:
        print('\033[33mMAIOR NÚMERO')
        if n1 > n2:
            print('\033[34mO maior número entre {} e {} é \033[31m{}\033[m.'.format(n1, n2, n1))
        else:
            print('\033[34mO maior número entre {} e {} é \033[31m{}\033[m.'.format(n1, n2, n2))
    if e == 4:
        print('NOVOS NÚMEROS')
        n1 = int(input('\033[mDigite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    time.sleep(3)
    print('\033[33m=================')
time.sleep(2)
print('FINALIZANDO...')
time.sleep(3)
print('\033[31mPROGRAMA ENCERRADO.')