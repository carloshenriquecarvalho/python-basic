#entrada de dados (calcular a hipotenusa)
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

#processamento de dados
h = hypot(ca, co)

#saída de dados
print('O valor da hipotenusa para cateto oposto {} e cateto adjacente {} é igual a {:.2f}'.format(co, ca, h))

#fim