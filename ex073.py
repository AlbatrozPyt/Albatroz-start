times = ('Atlético-MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino','Fluminense',
         'América-MG','Atlético-GO','Santos','Ceará SC','Internacional','São Paulo','Atlético-PR','Cuiabá',
         'Juventude','Grêmio','Bahia','Sport Recife','Chapecoense')
print('-'*265)
print(f'\033[34mOs 5 primeiros colocados são {times[0:5]}')
print('\033[m-'*265)
print(f'\033[31mOs ultimos 4 colocados são {times[-4:]}')
print('\033[m-'*265)
print('\033[33mOs times em ordem alfabética são:')
print(sorted(times))
print('\033[m-'*265)
print(f'\033[32mO Chapecoense está em {times.index("Chapecoense")+1}ºlugar.')
print('\033[m-'*265)