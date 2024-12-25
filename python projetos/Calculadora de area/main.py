#entrada de dados (calculadora de área)
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura dela? '))
cor_tinta = input('Qual a cor da tinta que quer usar? ')

#processamento de dados (cálculo da área em si)
area = largura * altura
litros_tinta = float(area / 2)

#saída  de dados
print('A área total da parede é {:.2f}m². \nA quantidade de litros de tinta {} é igual a {}l.'.format(area,cor_tinta, litros_tinta))

#fim