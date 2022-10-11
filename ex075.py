n = ( int(input('Digite um número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite o ultimo número: ')))

print(f'O número 9 aparece {n.count(9)} vezes/vez.')
if 3 in n:
    print(f'O número 3 aparece na {n.index(3)}º posição.')
else:
    print('O número 3 não foi digitado.')
print(f'Os números pares são: ',end='')
if n % 2 == 0:
     print(f'{n} ',end=' ')

