salario = int(input('Digite o valor do seu salário: '))
if salario <= 1250:
    print('O seu aumento será de 15%. O total é R${}.'.format(salario + (salario * 15 / 100)))
else:
    print('O seu aumento será de 10%. O total é R${}.'.format(salario + (salario * 10 /100)))
print('Obrigado por utilizar esta ferramenta! \nTe vejo na próxima!')

#fim