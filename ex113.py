
def leiaINT(msg):
    num = 0 
    while True:
        v = str(input(msg))
        try:
           num = int(v)
           break
        except:
            print('\033[31mERRO, digite um valor INTEIRO valido\033[m')
    return num


def leiaFLOAT(msg):
    num = 0
    while True:
        v = str(input(msg))
        try:
            num = float(v)
            break
        except:
            print('\033[31mERRO, digite um valor REAL valido\033[m')
    return num

i = leiaINT('\033[34mDigite um valor inteiro: ')
r = leiaFLOAT('\033[34mDigite um valor real: ')
print('-'*40)
print(f'\033[32m    -> NÚMERO INTEIRO: {i}')
print(f'\033[33m    -> NÚMERO REAL: {r}')
