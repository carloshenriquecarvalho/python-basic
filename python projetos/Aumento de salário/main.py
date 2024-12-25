#entrada de dados (salário com 15% de aumento)
nome_funcionario = input('Qual o nome do funcionário? ')
salario = float(input('Qual o salário atual do funcionário? R$'))

#processamento de dados
novo_salario = salario + (salario * 15 / 100)

#saída de dados
print('O novo salário do funcionário {} agora é igual a R${:.2f}.'.format(nome_funcionario, novo_salario))

#fim