l = []
e = str(input('\033[37mDigite uma expressão: '))
for p in e:
    if p == '(':
        l.append('(')
    elif p == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break
if len(l) > 0:
    print('\033[31mSua expressão esta errada!!!')
else:
    print('\033[34mSua expressão esta correta!!!')