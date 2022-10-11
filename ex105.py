from time import sleep
cont = 1
va = []
turma = {}

def notas(n,v,situação=0):
    """
    ***Informações das notas***
        -> O programa vai analisar uma ou mais notas e vai mostrar a Maior nota, a Menor, a Média e a Situação(OPCIONAL)
        -> Parâmetro n: São as notas lidas
        -> Parametro v: A lista onde são guardadas as notas
        -> Parâmetro situação(OPCIONAL): Mostra a situação da turma ou aluno, de acordo com a Média
    """
    turma['Número de notas'] = cont
    turma['Maior nota'] = max(v)
    turma['Menor nota'] = min(v)
    turma['Média'] = sum(v) / cont
    if situação:
        if turma['Média'] >= 7:
            turma['Situação'] = 'BOA'
        if 5 < turma['Média'] < 7:
            turma['Situação'] = 'MÉDIA'
        if turma['Média'] <= 5:
            turma['Situação'] = 'RUIM'

while True:    
    nota = float(input('Insira a nota do aluno: '))  
    r = str(input('Quer continuar:[S/N] ')).upper()[0]
    print('-'*50)
    va.append(nota)
    while r not in 'SN':
        print('  ERRO, apenas S ou N')
        r = str(input('Quer continuar:[S/N] ')).upper()[0]
        print('-'*50)
    fun = notas(nota,va,situação=True)
    cont += 1
    if r == 'N':     
        break
    
print(turma)
print('-'*50)
print('   AJUDA INTERATIVA')
print('-'*50)
help(notas)
print('-'*50)
f = 'FIM DO PROGRAMA'
for l in enumerate(f):
    print(l[1],end='')
    sleep(0.1)
