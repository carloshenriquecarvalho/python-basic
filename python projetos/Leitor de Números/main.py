n = 0
c = 0
while n != 999:
  n = int(input('Digite um valor.'
                '\nOu digite 999 para sair do programa:'))
  if n != 999:
    soma = n + n
    c += 1
print('A soma é igual a {} e a quantidade de números digitas foi igual a {}'.format(soma, c))