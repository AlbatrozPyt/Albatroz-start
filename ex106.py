def tit(txt):
    tam = len(txt)+5
    print('>'*tam)
    print(f'     {txt}')
    print('>'*tam)

def ajuda(c,a='     INTERACTIVE HELP'):
    tam = len(a)+1
    print('-'*tam)
    print(a)
    print('-'*tam)
    help(c)
    print('-'*70)

    
while True:
    tit('CENTRAL DE AJUDA -- PYTHON-help')
    comando = str(input('Digite o comando ou função(DIGITE "FIM" PARA PARAR)-> '))
    if comando.lower() == 'fim':
        break
    ajuda(comando)
tit('FIM DO PROGRAMA')
