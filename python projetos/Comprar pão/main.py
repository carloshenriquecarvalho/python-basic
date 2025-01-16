#defini o valor de um pão para 50 centavos
pao = float(0.50)

dinheiro_cliente = int(input('Quantos reais você tem? R$'))
if dinheiro_cliente < pao:
  print('Você não tem dinheiro suficiente para comprar pão.')
else:
  qnt = dinheiro_cliente / pao
  print('Você tem dinheiro para comprar pão e pode levar até {:.0f} pães.'.format(qnt))