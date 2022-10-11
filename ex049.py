print('\033[31m=======\nTABUADA\n=======')
n = int(input('\033[33mDigite o número que voce quer a tabuada: '))
for c in range(0,10 + 1):
    print('\033[36m{}x{}={}'.format(n, c, c * n))