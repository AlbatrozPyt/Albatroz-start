notas = []
while True:
    nome = str(input('mNome do aluno: '))
    n1 = float(input('1ª Nota: '))
    n2 = float(input('2ª Nota: '))
    media = (n1 + n2) / 2
    notas.append([nome,[n1,n2],media])
    r = str(input('Quer continuar:[S/N] ')).strip().upper()
    while r not in 'SN':
        r = str(input('Quer continuar:[S/N] ')).strip().upper()
    if r in 'N':
        break
print('+-+'*30)
print('MÉDIAS')
print(f'{"No":<5} {"Nome":^5} {"Média":>5}')
for p,a in enumerate(notas):
    print(f'{p:<5}',end='')
    print(f'{a[0]:^5}',end='')
    print(f'{a[2]:>5}')
while True:
    a = int(input('Qual aluno você quer ver as notas - (999 PARA): '))
    if a == 999:
        break
    else:
        print(f'As notas de {notas[a][0]} foram {notas[a][1]}')
