import random
e = 0
n = random.randint(1,10)
r = int(input('\033[33mEm que número pensei: '))
while r != n:
    print('\033[31mVOCE ERROU, TENTE DE NOVO')
    r = int(input('\033[33mEm que número pensei:'))
    e += 1
print('\033[34mVOCE ACERTOU')
print('\33[34mForam necessarias {} chances.'.format(e))