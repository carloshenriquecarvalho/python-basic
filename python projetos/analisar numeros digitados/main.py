c = 0
num = -1
soma = 0
lista = []
while num != 0:
  num = int(input('Digite um valor: '))
  soma += int(num)
  if num != 0:
    c += 1
    lista.append(num)
print('O valor da média dos números é igual a {:.2f} e a quantidade de números digitados foi {}.'.format((soma / c), c))
print('O maior número é {} e o menor é {}.'.format(max(lista), min(lista)))
