n = []
ma = me = 0
for c in range(0,5):
    n.append(int(input(f'\033[37mDigite  um número na posição {c}: ')))
    if c == 0:
        ma = me = n[c]
    else:
        if n[c] < me:
            me = n[c]
        if n[c] > ma:
            ma = n[c]

print(f'\033[36mA lista de números digitados é: {n}')
print(f'O maior valor digitado foi o {ma} na posição ',end=' ')
for i,v in enumerate(n):
   if ma == v:
    print(i,end='...')
print()
print(f'O menor valor digitado foi o {me} na posição ',end=' ')
for i,v in enumerate(n):
    if me == v:
        print(i,end='...')