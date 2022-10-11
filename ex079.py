n = []
r = ''
v = 0
while r != 'N':
    v = int(input('\033[33mDigite um número: '))
    if v not in n:
        print('\033[31mO número foi cadastrado na lista...')
        n.append(v)
    else:
        print('\033[31mO número não foi cadastrado, pois ja foi digitado...')
    r = str(input('\033[33mQuer continuar:[S/N] ')).upper().strip()
    while r not in ('NS'):
        r = str(input('Quer continuar:[S/N] ')).upper().strip()
n.sort()
print('\033[31m-+'*30)
print(f'A lista em ordem crescente é: {n}')

