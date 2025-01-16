#competições olímpicas
idade = int(input('Qual a sua idade? '))
permissão = str(input('Você tem permissão médica para competir? S/N '))
condicionamento_físico = str(input('Você está em bom estado físico? S/N '))

if 18 < idade < 36 and permissão in 'Ss' or condicionamento_físico in 'Ss':
  print('Você pode competir!')
else:
  print('Você não pode competir!')