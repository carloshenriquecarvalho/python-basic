#entrada de dados
nome = str(input('Digite seu nome completo, por favor: ')).strip()
nome.split()
nome.upper()
silva = 'Silva' in nome
if silva :
  print('Você tem Silva no nome.')
else:
  print('Você não tem Silva no nome.')


print('Seu nome tem Silva? {}.'.format('SILVA' in nome.upper()))
#fim