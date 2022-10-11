frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de \033[31m{}\033[m é \033[31m{}\033[m.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')