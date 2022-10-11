matriz = []
lin = 0
col = 0
while True:
    n = int(input(f'Digite um número para linha \033[33m[{lin}]\033[m e coluna \033[33m[{col}]\033[m: '))
    matriz.append(n)
    col += 1
    if col == 3:
        lin += 1
        col = 0
    if lin == 3 and col == 0:
        break
print('+-+'*30)
print('A matriz formada foi:')
for p,i in enumerate(matriz):
    print(f'[{i:^5}]',end=' ')
    if p == 2 or p == 5:
        print()
