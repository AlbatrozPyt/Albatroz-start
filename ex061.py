print('='*30)
print('GERADOR DE PA')
print('='*30)
p = int(input('\33[31mDigite o 1º termo: '))
r = int(input('Razão: '))
t = p
cont = 1
while cont <= 10:
    print('\33[33m{}'.format(t), end= ' ~ ')
    t += r
    cont += 1
print('Fim.')