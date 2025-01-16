print('-'*30)
print('Sequência de Fibonacci!'.center(30))
print('-'*30)

n = int(input('Digite a quantidade de termos que quer ver da sequência de Fibonacci: '))
t1 = 0
t2 = 1
print('~'*50)
print('{} ➟ {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
  t3 = t1 + t2
  t1 = t2
  t2 = t3
  print(' ➟ {}'.format(t3), end='')
  cont += 1
