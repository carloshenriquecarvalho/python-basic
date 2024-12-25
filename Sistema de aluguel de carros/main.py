#entrada de dados (sistema de aluguel de carros)
d = int(input('Quantos dias o carro foi usado? '))
km = float(input('Qual a quilometragem registrada de percurso para todo este tempo? '))

#saída e processamento de dados
print('O valo a pagar pelos dias é igual a {:.2f}R$.\nPela quilometragem é igual a {:.2f}R$. \nTotal a pagar: {:.2f}R$.'.format((d * 60), (km * 0.15), ((km * 0.15) + (d * 60))))

#fim