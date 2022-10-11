from datetime import datetime
from time import sleep
dic = {}
dic['Nome'] = str(input('Qual o seu nome: '))
an = int(input('Ano de nascimento: '))
dic['Idade'] = datetime.now().year - an
dic['CTPS'] = int(input('Carteira de Trabalho (0-se não tiver): '))

if dic['CTPS'] == 0:
    dic['CTPS'] = 'Não tem'
else:
    dic['Ano de Contratação'] = int(input('Ano de contratação: '))
    dic['Salário'] = float(input('Salário: '))
    dic['Aposentadoria'] = dic['Idade']+(dic['Ano de Contratação'] + 35 - datetime.now().year)
    
print('+-+'*20)
print('  <Informações>')
for k,v in dic.items():
    print(f'    {k} -- {v}')
    sleep(0.1)
    
f = '<Adeus>'
for l in range(0,len(f)):
    print(f' {f[l]}',end='')
    sleep(0.3)
