matriz = [[0,0,0],[0,0,0],[0,0,0]]
totP = terCol = ma = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'\033[37mDigite um número para linha\033[35m[{l}]\033[37m e coluna\033[35m[{c}]\033[37m: '))
        if matriz[2][c] == 0 or matriz[2][c] > ma:
            ma = matriz[1][c]
print('\033[37m+-+\033[35m'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            totP += matriz[l][c]
        if c == 2:
            terCol += matriz[l][c]
            print()


print('\033[37m+-+\033[35m'*30)
print(f'A soma dos números pares digitados foi {totP}.')
print(f'A soma dos valores da terceira coluna foi {terCol}.')
print(f'O maior valor da segunda linha foi {ma}.')