import random
import time
v = 0
print('-'*30)
print('IMPAR OU PAR')
print('-'*30)
while True:
    com = random.randint(0,10)
    print('-'*30)
    j = int(input('\033[33mQual o número: '))
    t = j + com
    e = ' '
    while e not in 'PI':
        e = str(input('Impar ou Par:[I/P] ')).strip().upper()[0]
    print('IMPAR')
    time.sleep(1)
    print('OU')
    time.sleep(1)
    print('PAR')
    print(f'Jogador: {j} - Computador: {com}, total {t}')
    print('IMPAR!!!'if t % 2 == 1 else 'PAR!!!', end='')
    if e == 'I':
        if t % 2 == 1:
            print('\033[34mVOCÊ VENCEU!!!, VAMOS MAIS UMA...')
            v += 1
    if e == 'P':
        if t % 2 == 0:
            print('\033[34mVOCÊ VENCEU!!!, VAMOS MAIS UMA...')
            v += 1
    elif e =='I' and t % 2 == 0 or e == 'P' and t % 2 == 1:
        break
print('\033[31mGAME OVER...')
print(f'Você venceu {v} vezes.')
