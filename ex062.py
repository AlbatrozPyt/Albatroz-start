p = int(input('\33[33mDigite um número: '))
r = int(input('Razão: '))
t = 0
cont = 1
m = 10
while m != 0:
    t = t + m
    while cont <= m:
        print('\33[31m{}'.format(t), end=' ~ ')
        t += r
        cont += 1
print('FIM.')