from time import sleep
apr = {}
g = []
apr['Nome'] = str(input('Nome do jogador: '))
j = int(input(f'Total de jogos de {apr["Nome"]}: '))

print(' -'*30)
for p in range(0, j):
    p = int(input(f'Quantos gols na {p+1:^2}ª partida: '))
    g.append(p)
apr['Gols']= g
apr['Total'] = sum(g)

print(' -'*30)
print(apr)
print(' -'*30)
for k,v in apr.items():
    print(f'O valor de {k} é {v}')
print(' -'*30)
print('<Analise de dados>')
for i,p in enumerate(apr['Gols']):
    print(f'    {i+1:^2}ª Partida -- {p:^2} Gol(s)')
print('-'*30)
print(f'O total de gols foi - {apr["Total"]}')
f = '<Volte Sempre!!!>'
for l in range(0,len(f)):
      print(f' {f[l]}',end='')
      sleep(0.3)

