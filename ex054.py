from datetime import date
atual = date.today().year
tma = 0
tme = 0
for c in range(1, 8):
    nasc = int(input('\033[33mEm que ano a {}º pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 18 :
        tma += 1
    else:

        tme += 1
print('\033[31mAo todo tivemos {} pessoas maiores de idade.'.format(tma))
print('\033[31mTambem tivemos {} pessoas menores de idade.'.format(tme))
