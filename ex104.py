def leiaInt(msg):
    res = False
    num = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            num = int(n)
            res = True
        else:
            print('Você NÃO DIGITOU um valor númerico!!!')
        if res:
            break
    return num

n = leiaInt('Digite um número: ')
print('-'*40)
print(f'Você DIGITOU o valor númerico {n}!!!')
