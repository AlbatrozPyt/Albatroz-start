n = []
p = n[:]
i = n[:]
while True:
    v = (int(input('\033[37mDigite um número: ')))
    n.append(v)
    if v % 2 == 0:
        p.append(v)
    if v % 2 == 1:
        i.append(v)
    r = str(input('Quer continuar:[S/N] ')).strip().upper()
    while r not in 'SN':
        r = str(input('Quer continuar:[S/N]  ')).strip().upper()
    if r in 'N':
        break
print('\033[35m+-+'*30)
print(f'\033[34mVoce digitou os números: {n}')
print(f'\033[36mOs números pares foram: {p}')
print(f'\033[31mOs números impares foram: {i}')
