c = v = d = u = 0
print('\033[34m******SUPER BANCO******')
di = int(input('Qual o valor que vai ser sacado: '))
while True:
    if di >= 50:
        di -= 50
        c += 1
    if di < 50 and di >= 20:
        di -= 20
        v += 1
    if di < 20 and di >= 10:
        di -= 10
        d += 1
    if di < 10 and di >= 1:
        di -= 1
        u += 1
    if di <= 0:
        break
print(f'\033[33mForam entregues.\n'
      f'\033[31m{c} \033[33mnotas de 50.\n'
      f'\033[31m{v} \033[33mnotas de 20.\n'
      f'\033[31m{d} \033[33mnotas de 10.\n'
      f'\033[31m{u} \033[33mnotas de 1.')