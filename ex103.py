def ficha(n='<DESCONHECIDO>', g=0):
   print('-'*40)
   print(f'O jogador {n} fez um número de {g} gol(s).')
   
nome = str(input('Insira o nome do jogador: '))
quantg = str(input('Quantos gols o jogador marcou: '))
if quantg.isnumeric():
   quantg = int(quantg)
else:
   quantg = 0
if nome.strip() == '':
   ficha(g=quantg)
else:
   ficha(nome, quantg)
