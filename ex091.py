from random import randint
from time import sleep
from operator import itemgetter
Jogadores = {'jogador1':randint(1,6),'jogador2':randint(1,6),
             'jogador3':randint(1,6),'jogador4':randint(1,6)}
res = []
print('     <Sorteio>')
for k,v in Jogadores.items():
      print(f'    {k} -- {v}')
      sleep(0.5)
res = sorted(Jogadores.items(), key=itemgetter(1), reverse=True)
print('\n     <Resultado>')
for p, v in enumerate(res):
      print(f'    {p+1}ªlugar: {v[0]} -- {v[1]}')
      sleep(0.5)
f = '<Obrigado por Jogar>'
for l in range(0,len(f)):
      print(f' {f[l]}',end='')
      sleep(0.1)
