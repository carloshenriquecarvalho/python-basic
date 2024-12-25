#entrada de dados (tabuada dos números)

numero = int(input('Olá, tudo bem?\nVamos descobrir a tabuada do seu número preferido. \nPara começar, digite seu número escolhido: '))

#processamento de dados (tabuada de 0 a 10)

m1 = numero * 0
m2 = numero * 1
m3 = numero * 2
m4 = numero * 3
m5 = numero * 4
m6 = numero * 5
m7 = numero * 6
m8 = numero * 7
m9 = numero * 8
m10 = numero * 9
m11 = numero * 10


#saída de dados (tabuada completa)
print('Maravilha! Esta é a tabuada do número que você escolheu!\n')
print('-' * 11)
print('{} X 0  = {}\n'
      '{} X 1  = {}\n'
      '{} X 2  = {}\n'
      '{} X 3  = {}\n'
      '{} X 4  = {}\n'
      '{} X 5  = {}\n'
      '{} X 6  = {}\n'
      '{} X 7  = {}\n'
      '{} X 8  = {}\n'
      '{} X 9  = {}\n'
      '{} X 10 = {}'.format(numero, m1, numero, m2, numero, m3, numero, m4, numero, m5,
                            numero, m6, numero, m7, numero, m8, numero, m9, numero, m10, numero, m11))
print('-' * 11)
