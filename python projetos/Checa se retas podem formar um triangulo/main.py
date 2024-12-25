#entrada de dados
a = int(input('Digite o valor da primeira reta: '))
b = int(input('Digite o valor da segunda reta: '))
c = int(input('Digite o valor da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Estes valores podem forma ruma reta!')
else:
    print('Estes valores não podem formar uma reta!')

#fim