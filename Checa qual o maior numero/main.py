#entrada de dados
print('Olá! É um prazer ter você conosco')
n1 = int(input('Para analisar os dois números, digite o primeiro: '))
n2 = int(input('Agora, digite o segundo número: '))
maior = n1

#processamento de dados
if n1 > n2:
    maior = n1
    print('O número maior é {}.'.format(maior))
elif n1 < n2:
    maior = n2
    print('O número maior é {}.'.format(maior))
elif n1 == n2:
    print('Não existe um valor maior. Todos são iguais.')
