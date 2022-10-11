from random import randint
from time import sleep
f = ('   \n<<< ADEUS!!! >>>')
numeros = []

def sorteia(n):
    sleep(1)
    for c in range(0, 5):
        n.append(randint(0, 50))
    print(f'Os valores sorteados foram ',end='')
    for val in n:
        print(f'{val} ',end='')
        sleep(0.5)
    print('>>> FIM !!!')
sorteia(numeros)

def somaPar(np):
    sleep(1)
    totP = 0
    for i in np:
        if i % 2 == 0:
            totP += i
    print(f'A soma de todos os pares é igual a {totP}')
somaPar(numeros)    
for l in range(0, len(f)):
    print(f[l],end='')
    sleep(0.3)
    