print('\33[31m='*30)
print('FATORIAL!')
print('='*30)
n = int(input('\33[33mDigite um número para calcular se fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))