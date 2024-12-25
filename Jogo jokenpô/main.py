#entrada de dados
import random
print('Vamos jogar Jokenpô!')
lista = ['pedra', 'papel', 'tesoura']
jogador = input('Quando estiver pronto, digite 1')
escolha = random.choice(lista)
print('Preparado? 1... 2... 3... '
      '\nEu escolho {}'.format(escolha))