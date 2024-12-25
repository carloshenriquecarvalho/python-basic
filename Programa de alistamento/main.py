#entrada de dados
print('Seja bem-vindo(a) ao sistema de alistamento do Governo Nacional.')
nome = str(input('Primeiro, qual é o seu nome? '))
nascimento = int(input('Certo, {}. Agora me diga em que ano nasceu? '.format(nome)))
idade = 2024 - nascimento
if idade < 18:
    tf = 18 - idade
    if tf == 1:
        print('Você ainda não se encaixa no padrão de alistamento este ano. Falta 1 ano para que você possa se alistar efetivamente.')
    else:
        print('Você ainda não se encaixa no padrão de alistamento este ano. Faltam {} anos para que você possa se alistar efetivamente.'.format(tf))
elif idade == 18:
    print('Está na hora de se alistar, cidadão.')
elif idade > 18:
    tp = idade - 18
    print('O seu período de alistamento já passou tem {} anos! Procure por uma agência de serviços do exército para '
          'ficar em dias com seus deveres!'.format(tp))

#fim