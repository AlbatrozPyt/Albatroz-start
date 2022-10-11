sexo = str(input('\033[33mDigite seu sexo[M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('\033[31mRESPOSTA INVALIDA, TENTE DE NOVO')
    sexo = str(input('\033[33mDigite seu sexo [M/F]: ')).strip().upper()[0]
print('SEXO {} REGISTRADO, FIM DO PROGRAMA'.format(sexo))
