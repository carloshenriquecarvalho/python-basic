#entrada de dados
nota1 = float(input('Olá, tudo bem? Para sabermos de sua situação, digite quanto você tirou na primeira prova: '))
nota2 = float(input('Digite quanto você tirou na segunda prova: '))
media = float((nota1 + nota2) / 2)
if media < 5:
    print('Sua média é {:.1f}. Infelizmente você reprovou'.format(media))
elif media >= 7:
    print('Parabén! Sua média foi {:.1f}! Você foi aprovado!'.format(media))
else:
    print('Sua média é {:.1f}. Você está de recuperação'.format(media))

#fim