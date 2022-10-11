import time

c = n = 0
while n >= 0:
    c = 0
    n = int(input('\033[33mdigite um número para ver sua tabuada: '))
    if n < 0:
        break
    while c < 10:
        c += 1
        print(f'\33[31m{n}x{c} = {n*c}')
        time.sleep(0.1)
print('FIM DO PROGRAMA.')