soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('\33[36mA soma de todos os números impares e multiplos de 3 e igual {}.'.format(soma))
print('Ao todo são {} números impares e multiplos de 3.'.format(cont))