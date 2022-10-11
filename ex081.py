n = []
while True:
    n.append(int(input('\033[37mDigite um número: ')))
    r = str(input('Quer continuar:[S/N] ')).strip().upper()
    if r in 'N':
        break
    while r not in 'NS':
        r = str(input('Quer continuar:[S/N] ')).strip().upper()
n.sort(reverse=True)
print('\033[36m+-+'*30)
print(f'Foram digitados {len(n)} números.')
print(f'Os valores em ordem decrescente são: {n}')
if 5 in n:
    print(f'O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')