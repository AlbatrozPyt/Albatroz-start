ne = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze',
      'Doze','Treze','Quatorze','Quinze','Dezesseis','Dezesete','Dezoito','Dezenove','Vinte')
r = ''
while r != 'N':
      n = int(input('\033[33mDigite um número entre 0 e 20: '))
      if n < 0 or n > 20:
            n = int(input('ERRO, Digite novamente: '))
      print(f'O número {n} por extenso é \033[31m{ne[n]}\033[m')
      r = str(input('\033[33mQuer continuar: ')).upper()