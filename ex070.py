import math
total = ma1000 = menor = cont = cont2 = p = 0
cont = 1
barato = ''
nome = ' '
print('='*30)
print('REGISTRO DE PREÇOS')
print('='*30)
while True:
     nome = str(input(f'\033[34mNome do {cont}º produto: ')).strip().upper()
     p = float(input('Qual foi o preço:R$'))
     cont += 1
     total += p
     barato = nome
     if p > 1000:
         ma1000 += 1
     if cont == 1 or p < menor:
         menor = p
         barato = nome
     r = ' '
     r = str(input('Quer continuar: ')).strip().upper()[0]
     if r == 'N':
         break
     cont2 += 1
print(f'\033[31mA soma total de produtos comprados e de R${total:.2f}.')
print(f'Tiveram {ma1000} produtos com o preço maior que R$1000.00.')
print(f'O produto mais barato foi a(o) {barato.capitalize()}.')