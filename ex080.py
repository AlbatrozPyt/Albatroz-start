n = []
for c in range(0,5):
    v = int(input('\033[37mDigite um número: '))
    if c == 0 or v > n[-1]:
        n.append(v)
        print('Ultimo número da lista...')
    else:
        pos = 0
        while pos < len(n):
            if v <= n[pos]:
                n.insert(pos,v)
                print(f'{pos+1}ª posição da lista...')
                break
            pos += 1
print('\033[36m<>'*30)
print(n)
