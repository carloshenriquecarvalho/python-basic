media = 0
for x in range(1, 3):
  nota = float(input('Digite a sua {}ª nota: '.format(x)))
  media += nota
mfinal = media / 2
match mfinal:
  case mfinal if mfinal < 5:
    print('Você foi \033[1;31mREPROVADO!\033')
  case mfinal if 5 < mfinal < 7:
    print('Você está de \033[1;33mRECUPERAÇÃO!\033') 
  case mfinal if mfinal > 7:
    print('\033[1;32mPARABÉNS! Você foi APROVADO!\033')