def voto(a):
   from datetime import datetime
   i = datetime.now().year - an
   if i < 16:
       return f'Com {i} anos: VOTO NEGADO'
   if i < 18 or i >= 65:
      return f'Com {i} anos: VOTO OPCIONAL'
   else:
      return f'Com {i} anos: VOTO OBRIGATÓRIO'
  

an = int(input('Insira o ano de nascimento: '))
print('>'*70)
print(voto(an))
