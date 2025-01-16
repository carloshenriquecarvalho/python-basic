from time import sleep 
num1 = int(input('Digite um número: ')) 
num2 = int(input('Digite outro número: ')) 
opcao = 0

print('-=-'*15) 
while opcao != 5: 
  opcao = int(input('[1] Somar' 
                    '\n[2] Multiplicar' 
                    '\n[3] Maior' 
                    '\n[4] Novos números' 
                    '\n[5] Sair do programa\n')) 
  match opcao: 
    case opcao if opcao == 1: 
      print('A soma é {}'.format(num1 + num2)) 
    case opcao if opcao == 2: 
      print('A multiplicação é {}'.format(num1 * num2)) 
    case opcao if opcao == 3: 
      if num1 > num2: 
        print('O maior número é {}'.format(num1)) 
      else: print('O maior número é {}'.format(num2)) 
    case opcao if opcao == 4: 
      num1 = int(input('Digite um número: ')) 
      num2 = int(input('Digite outro número: ')) 
    case opcao if opcao == 5: 
      print('Finalizando...') 
      sleep(2) 
      print('-=-'*15) 
      print('Obrigado por utilizar a calculadora!')