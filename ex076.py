p = ('Arroz',7.00,'Feijão',10.00,'Refrigerante',12.00,'Detergente',2.00,'Ração',5.00,
    'Amaciante',8.00,'Salgadinho',3.50,'Açucar',15.00,'Suco',1.50,'Cloro',9.00)
print(30*'\033[34m-')
print('LISTA DE PREÇOS')
print(30*'-')
for c in range(0,len(p)):
    if c % 2 == 0:
        print(f'\033[33m{p[c]:.<30}',end='')
    else:
        print(f'R${p[c]:>5.2f}')
print(30*'\033[34m-')

