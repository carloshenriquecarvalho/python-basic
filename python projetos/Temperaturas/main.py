#definição de temperatura
temperatura = float(input('Digite a temperatura em graus Celsius: '))

#análise de dados para definir quente, frio ou ambiente
if temperatura < 20:
  print('Está frio.')
elif temperatura < 30:
  print('Está ambiente.')
elif temperatura < 35:
  print('Está quente.')