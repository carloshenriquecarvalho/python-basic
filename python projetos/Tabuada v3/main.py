from time import sleep
multiplicadores = 10
while True:
  num = int(input('Digite a tabuada que quer ver (ou 0 para finalizar o preocesso): '))
  if num == 0:
    print('Finalizando processo...')
    sleep(2)
    print('Processo finalizado. Obrigado por utilizar a caulculadora!')
    break
  print('-'*30)
  for x in range(1, 11):
    print(f'{num} x {x} = {num * x}'.center(30))
  print('-'*30)