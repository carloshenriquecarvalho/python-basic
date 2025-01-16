#operadores de condições
idade = int(input('Qual a sua idade? '))
tem_carteira_motorista = str(input('Você tem carteira? S/N '))

#analisa os dados recebidos
if tem_carteira_motorista in 'Ss':
  tem_carteira_motorista = True
elif tem_carteira_motorista in 'Nn':
  tem_carteira_motorista = False

#resulta a possibilidade de dirigir
if idade >= 18 and tem_carteira_motorista:
  print('Pode dirigir, chefia!')
else:
  print('Você não pode dirigir segundo as leis do Brasil!')