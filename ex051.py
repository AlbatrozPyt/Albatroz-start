n1 = int(input('Escolha em que número sua PA vai começar: '))
n2 = int(input('Razão: '))
décimo = n1 + (10 - 1) * n2
for c in range(n1,décimo,n2):
    print('{}'.format(c), end='-')
print('ACABOU')