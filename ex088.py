from random import randint
from time import sleep
jogos = []
j = []
numJ = int(input('Qual será o número de jogos? '))
for c in range(0,numJ):
    for c in range(0,6):
        n = randint(1,60)
        while n in j:
            n = randint(1,60)
        j.append(n)
        if len(j) == 6:
            jogos.append(j[:])
            j.clear()
for p,c in enumerate(jogos):
    sleep(0.5)
    print(f'O {p+1:^2}ª jogo foi: {sorted(jogos[p])}')
print('<<< BOA SORTE >>>')
