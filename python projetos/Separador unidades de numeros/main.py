#entrada de dados
num = int(input('Digite um número entre 0 e 9999: '))
#definir que sempre haja 4 dígitos em qualquer número digitado

#definir cada um dos números
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#imprimir os números e suas respectivas unidades
print('Unidade: {} \n'
      'Dezena: {} \n'
      'Centena: {} \n'
      'Milhar: {}'.format(u, d, c, m))

#fim