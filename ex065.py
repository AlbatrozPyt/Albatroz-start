n = 0
cont = soma = maior = menor = 0
r = str(input('\033[34mQuer começar:[S/N] ')).strip().upper()[0]
while r not in 'Nn':
    n = int(input('\33[31mDigite um valor: '))
    r = str(input('\33[33mQuer continuar:[S/N] ')).strip().upper()[0]
    cont += 1
    soma += n
    if maior <= n:
        maior = n
    elif menor <= maior:
        menor = n
m = soma / cont
print('\33[34mForam digitados {} números e a média entre eles e de {}'.format(cont, m))
print('O maior número foi o {} e o menor foi o {}.'.format(maior, menor))






















