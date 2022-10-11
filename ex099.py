from random import randint
from time import sleep


def maior(*num):
    sleep(2)
    ma = cont = 0
    print(f'-> Entre os números: ',end='')
    for n in num:
        cont += 1
        if n >= ma:
            ma = n
        print(f'{n} ',end='')
        sleep(0.3)
    print()
    print(f'    -> São {cont} número(s) -> E o maior é -> {ma}')
    print('>'*25)
    
    
maior(randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
maior(randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
maior(randint(0,100), randint(0,100), randint(0,100), randint(0,100))
maior(randint(0,100), randint(0,100), randint(0,100))
maior(randint(0,100), randint(0,100))
maior(randint(0,100))
maior()