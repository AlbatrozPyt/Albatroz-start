soma = 0
cont = 0
for c in range(1, 6+1):
    n = int(input('\033[33mDigite o {}º número: '.format(c)))
    if n % 2 == 0:
     soma += n
     cont += 1
print('\033[31mVoce informou {} números pares e a soma deles foi igual a {}.'.format(cont, soma))
