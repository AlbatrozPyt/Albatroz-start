n = []
cont = 0
for c in range(0,7):
    c = int(input('\033[37mDigite um número: '))
    if c == 0 or c % 2 == 0:
        n.append(c)
    elif c % 2 == 1:
        n.insert(cont,c)
        cont += 1
cont = 0
for i,v in enumerate(n):
    if v % 2 == 0:
        cont = i
        break
print(f'\033[36mOs números pares em ordem crescente são: {sorted(n[cont:])}')
print(f'Os números impares em ordem crescente são: {sorted(n[0:cont])}')
