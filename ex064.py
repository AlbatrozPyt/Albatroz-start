soma = cont = 0
n = 0
while n != 999:
    n = int(input('\033[33mDigite um número: '))
    soma += n
    cont += 1
print('\033[31mFim do programa.')
print('Foram digitados {} números e suas somas foram de {}.'.format( cont-1, soma-999))