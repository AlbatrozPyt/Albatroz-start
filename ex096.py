def area(c, l):
    a = comprimento * largura
    print(f'A área do terreno de {l}x{c}, mede {a}m')
    

print(' -'*25)
print('    CÁLCULO DE ÁREA RETANGULAR')
print(' -'*25)
largura = float(input('Qual é a largura do terreno (m): '))
comprimento = float(input('Qual é o comprimento do terreno (m): '))
print(' -'*25)
area(comprimento, largura)
