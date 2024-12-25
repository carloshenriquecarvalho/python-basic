#entrada de dados (conversor para ângulos)
import math
a = float(input('Digite o valor do ângulo: '))

#processamento de dados
s = float(math.sin(math.radians(a)))
c = float(math.cos(math.radians(a)))
t = float(math.tan(math.radians(a)))

#saída de dados
print('O seno de {} vale {:.2f}.'
      '\nO cosseno de {} vale {:.2f}.'
      '\nA tangente de {} vale {:.2f}.'.format(a, s, a, c, a, t))

#fim