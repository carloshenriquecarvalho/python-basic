#bibliotecas sendo usadas
from random import randint
vitoria = 0

#iniciar seção re looping
while True:
  # máquina escolhe um número entre 0 e 10
  sort = randint(1, 10)
  
  #jogador escolhe impar ou par
  choice = str(input('Par ou ímpar? '))
  
  #jogador escolhe seu número
  np = int(input('Digite seu número: '))
  
  #soma dos números para verificação se é ímpar ou par o resultado
  soma = np + sort
  
  #verificar se o jogador ganhou ou não
  match choice:
    #verificar se ele selecionou par e o resultado é par
    case choice if choice == 'par' and soma % 2 ==0:
      vitoria += 1 
      print(f'Você ganhou! Está com {vitoria} vitorias!')
      print(f'O número que escolhi foi {sort}.')
      
    #verifica se ele selecionou impar e o resultado é ímpar
    case choice if choice == 'impar' and soma % 2 !=0:
      vitoria += 1 
      print(f'Você ganhou! Está com {vitoria} vitorias!')
      print(f'O número que escolhi foi {sort}.')
      
    #verifica se o usuário selecionou par e o resultado é ímapr
    case choice if choice == 'par' and soma % 2 !=0:
      print(f'Você perdeu com {vitoria} vitórias consecutivas.')
      print(f'O número que escolhi foi {sort}.')
      break
    
    #verifica se o usuário selecionou impar e o resultado é par
    case choice if choice =='impar' and soma % 2 ==0:
      print(f'Você perdeu com {vitoria} vitórias consecutivas.')
      print(f'O número que escolhi foi {sort}.')
      break