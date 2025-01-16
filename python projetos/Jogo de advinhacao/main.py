from random import randint

tot_tentativas = 0
sort_n = randint(0, 10)
tentativa = -1
while tentativa != sort_n:
  tentativa = int(input('Digite um número entre 0 e 10: '))
  tot_tentativas += 1
  if tentativa != sort_n:
    print('Você errou! Tente novamente.')
  else:
    print('Você acertou!')
print('O número de tentativas foi de {}.'.format(tot_tentativas))