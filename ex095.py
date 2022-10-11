from time import sleep
time = []
apr = {}
g = []
while True:
    apr.clear()
    print(' -+'*30)
    apr['Nome'] = str(input('Nome do jogador: '))
    j = int(input(f'Total de jogos de {apr["Nome"]}: '))
    print(' -+'*30)
    g.clear()
    for p in range(0, j):
        p = int(input(f'    Quantos gols na {p+1:^2}ª partida: '))
        g.append(p)
    apr['Gols']= g[:]
    apr['Total'] = sum(g)
    time.append(apr.copy())
    while True:
        r = str(input('Quer continuar[S/N]: ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO!!!, apena S ou N')
    if r in 'N':
        break
print(' -'*30)
print('No',end=' ')
for i in apr.keys():
    print(f'{i:<15}',end='')
print()
print(' -+'*30)
for k,v in enumerate(time):
    print(f'{k:>3}',end='')
    for d in v.values():
        print(f' {str(d):<15}',end='')
    print()
while True:
    print(' -+'*30)
    busca = int(input('Digite o número do jogador para mostrar os dados(999-Finaliza): '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO!!!, esse jogador não existe')
    else:
        print(' -'*30)
        print(f'Aproveitamento do jogador - {time[busca]["Nome"]}')
        for i,g in enumerate(time[busca]['Gols']):
            print(' -'*30)
            print(f'    Na {i+1}ª partida marcou {g} Gol(s)')
print(' -'*30)
f = '<Fim!!!>'
for l in range(0,len(f)):
      print(f' {f[l]}',end='')
      sleep(0.3)
