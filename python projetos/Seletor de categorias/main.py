#entrada de dados
idade = int(input('Olá! Por favor, digite sua idade para que seja decidido a sua categoria: '))
if idade < 10:
    print('Sua categoria é MIRIM!')
elif 9 < idade < 15:
    print('Sua categoria é INFANTIL!')
elif 14 < idade < 20:
    print('Sua categoria é JUNIOR!')
elif idade == 20:
    print('Sua categoria é SÊNIOR!')
else:
    print('Sua categoria é MASTER!')

#fim