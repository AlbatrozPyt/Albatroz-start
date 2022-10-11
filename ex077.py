p =('astronauta','paleolitico','dinossauro','calopsita','cachorro')
for v in p:
    print(f'\n\033[33mAs vogais da palavra \033[31m{v.upper()}\033[m \033[33msão:\033[31m',end=' ')
    for l in v:
        if l in 'aeiou':
            print(l,end=' ')