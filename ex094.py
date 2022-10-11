from time import sleep
dic  = {}
lis = []
s = m = 0
while True:
    dic.clear()
    dic['Nome'] = str(input('Nome: '))
    while True:
        dic['Sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if dic['Sexo'] in 'MF':
            break
        print('ERRO!!!, apenas M ou F')
    dic['Idade'] = int(input('Idade: '))
    s += dic['Idade']
    lis.append(dic.copy())
    while True:
        r = str(input('Quer continuar[S/N]: ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO!!!, apenas S ou N')
    if r in 'N':
        break
print(' -'*30)
print(f'O número de pessoas cadastradas foi {len(lis)}. ')
m = s / len(lis)
print(f'A média de idade é {m:5.2f} Anos.')
print('As mulheres são: ',end='')
for p in lis:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}',end='; ')
print()
print('As pessoas acima da Média são: ')
for p in lis:
    if p['Idade'] >= m:
        print(f'    {p["Nome"]} - {p["Sexo"]} - {p["Idade"]}')
f = '<Volte Sempre!!!>'
for l in range(0,len(f)):
      print(f' {f[l]}',end='')
      sleep(0.3)

