i = s = r = ma = me = cont1 = cont2 = cont3 = 0
print('\033[31m='*30)
print('REGISTRO DE INFORMAÇÕES.')
print('='*30)
while True:
    print('\033[34m-><-'*11)
    s = str(input('\033[34mQual é o seu sexo:[M/F] ')).strip().upper()[0]
    while s not in 'MmFf':
        print('\033[31mERRO, TENTE DE NOVO.')
        s = str(input('\033[34mQual é o seu sexo:[M/F] ')).strip().upper()[0]
    if s == 'M':
        cont3 += 1
    i = int(input('\033[34mQual sua idade: '))
    if ma <= i:
        ma = i
    if i <= ma:
        me = i
    if ma and me > 18:
        cont2 += 1
    if s == 'F' and  me < 20:
        cont1 += 1
    r = str(input('\033[34mQuer continuar:[S/N] ')).strip().upper()[0]
    while r not in 'SsnN':
        print('\033[31mERRO, TENTE DE NOVO.')
        r = str(input('\033[34mQuer continuar:[S/N] ')).strip().upper()[0]
    if r not in 'Ss':
        break
print('\033[31mFIM DO PROGRAMA.')
print(f'Foram registradas {cont2} maiores de 18 anos.')
print(f'Foram registrados {cont3} homens.')
print(f'E foram registradas {cont1} mulheres com menos de 20 anos.')