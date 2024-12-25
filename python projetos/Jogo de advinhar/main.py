#entrada de dados
from random import randint
sort = randint(0, 5)
num = int(input('Eu irei pensar em um número. Tente acertar... \n Digite um número: '))
if num == sort:
    print('Parabéns, você acertou!!')
else:
    print('Que pena, você errou. :(')
print('O número era {}.'.format(sort))
print('Fim da brincadeira')