aluno = {}
n = str(input('Qual é o nome do aluno: '))
m = float(input(f'Qual foi a média de {n}: '))
if m >= 7:
    s = 'Aprovado'
elif 5 < m < 7:
    s = 'Recuperação'
else:
    s = 'Reprovado'
aluno = {'Nome':n,'Média':m,'Situação':s}
print('+-+'*20)
print('As informações são as seguintes:')
for k, v in aluno.items():
    print(f'{k} - {v}')
