#entrada de dados (mostrador do dobro, triplo e raiz quadrada)
print('Qual o valor desejado para a operação: ')
numero = int(input())

#processamento de dados (multiplicação e raiz)
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

#saída de dados
print('O dobro de {} é {}. \nSeu triplo é {}. \nE a raíz quadrada é {:.2f}'.format(numero, dobro, triplo, raiz))

#fim
