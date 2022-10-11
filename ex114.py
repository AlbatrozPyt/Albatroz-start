import urllib.request

try:
    res = urllib.request.urlopen('https://pudim.com.br')
except:
    print('\033[31mERRO, o site <https://pudim.com.br> não está acessivel no momento <[o-o]>')
else:
    print('\033[35mO site <https://pudim.com.br> está funcionando <[0_0]>')
res = urllib.request.urlopen('https://pudim.com.br')
print(res)
