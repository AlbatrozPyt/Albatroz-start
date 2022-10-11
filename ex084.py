info = []
cadastros = []
ma = me = 0
while True:
    info.append(str(input('\033[37mDigite seu nome: ')))
    info.append(float(input('Digite seu peso: ')))
    if len(cadastros) == 0:
        ma = me = info[1]
    else:
        if info[1] > ma:
            ma = info[1]
        if info[1] < me:
            me = info[1]
    cadastros.append(info[:])
    info.clear()
    r = str(input('Quer continuar:[S/N] ')).strip().upper()
    while r not in 'SN':
        r = str(input('Quer continuar:[S/N] ')).strip().upper()
    if r in 'N':
        break
print('+-+'*30)
print(f'\033[36mForam cadastradas {len(cadastros)} pessoas.')
print(f'O maior peso foi {ma}KG, esse peso é de: ',end='')
for i in cadastros:
    if i[1] == ma:
        print(i[0],end='; ')
print()
print(f'O menor peso foi {me}, esse peso é de: ',end='')
for i in cadastros:
    if i[1] == me:
        print(i[0],end='; ')