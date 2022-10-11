def fatorial(n,show=0):
    """
    ***Função de fatorial***
       -> Parâmetro n: Número que vai ser calculado
       -> Parâmetro (OPCIONAL) show: Mostra ou não a conta
       -> Return f: retorna  o resultado
    """
    from time import sleep
    f = 1
    for c in range(n,0,-1): 
        if show:
            print(c,end='')
            if c > 1:
                print(' x ',end='')
                sleep(0.5)
            else:
                print(' = ',end='')
        f *= c
    return f


num = int(input('Digite um número para o seu fatorial: '))
print('>'*70)
print(fatorial(num,show=True))
print('>'*70)
help(fatorial)
