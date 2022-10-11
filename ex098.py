from time import sleep
  
def contador(inicio, fim, passo):
    if passo < 0: 
        passo = passo*-1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end=' ')
            sleep(0.3)
            cont += passo
        print('FIM !!!')   
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end=' ')
            sleep(0.3)
            cont -= passo
        print('FIM !!!')
        
print('-'*25)
print('   CONTADOR  ')
print('-'*25)
print('Contagem de 1 a 10 -> ',end=' ')
contador(1, 10, 1)
print('-'*25)
print('Contagem de 10 a 0 -> ',end=' ')
contador(10, 0, 2)
print('-'*25)
print('Agora crie o seu contador -> ')
i = int(input('  Inicio: '))
f = int(input('  Fim: '))
p = int(input('  Passo: '))
print('Contagem personalizada -> ',end=' ')
contador(i, f, p)
print('-'*25)
