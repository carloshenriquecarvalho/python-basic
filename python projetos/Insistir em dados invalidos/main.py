sexo = str(input('Qual o seu sexo? M/F '))
while sexo not in 'MmFf':
  if sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite M ou F: '))
if sexo in 'Mm':
  print('Masculino')
elif sexo in 'Ff':
  print('Feminino')