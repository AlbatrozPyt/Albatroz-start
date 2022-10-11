n = s = c = 0
while True:
    n = int(input('\033[33mDigite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print('\033[31mFIM DO PROGRAMA.')
print(f'Foram digitados {c} números e a soma entre eles foi igual {s}.')