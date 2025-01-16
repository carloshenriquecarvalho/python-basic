soma = 0
cont = 0
print('~'*45)
print('Somadora de valores!'.center(45))
print('~'*45)
while True:
  num = int(input('Digite um número para ser somado, ou 999 para sair: '))
  if num == 999:
    break
  soma += num
  cont += 1 
print(f'A soma dos valores é igual a {soma}, a quantidade de números digitados é igual {cont} e a média dos valores é de {float(soma / cont):.2f}.')