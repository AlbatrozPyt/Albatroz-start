def lin(nl):
    nl = len(p)+4
    print('>'*nl)


def msg(txt):
    print()
    lin(p)
    print(f'  {txt}  ')
    lin(p)
    print()
    
  
while True:
    p = str(input('Escreva uma qualquer coisa: '))
    msg(p)
    r = str(input('Quer continuar:[S/N] ')).upper()[0]
    while True:
        if r in 'SN':
            print()
            break
        print('   ERRO, apenas S ou N')
        r = str(input('Quer continuar:[S/N] ')).upper()[0]
    if r in 'N':
        break