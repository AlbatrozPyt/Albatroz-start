SOMAidade = 0
MEDIAidade = 0
MAIORidadeHOMEM = 0
nomeVelho = ' '
tm20 = 0
for p in range(1, 5):
    print('\033[33m----{}ºPESSOA----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:\033[m '))
    SOMAidade += idade
    if p == 1 and sexo in 'Mm':
        MAIORidadeHOMEM = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > MAIORidadeHOMEM:
        MAIORidadeHOMEM = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        tm20 += 1
MEDIAidade = SOMAidade / 4
print('\033[31mA média de idade do grupo é {} anos.'.format(MEDIAidade))
print('\033[36mO homem mais velho tem {} anos e seu nome é {}.'.format(MAIORidadeHOMEM, nomeVelho))
print('\033[34mAo todo são {} mulheres com menos de 20 anos.'.format(tm20))