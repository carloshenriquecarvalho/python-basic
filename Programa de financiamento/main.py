'''
Perguntar:
valor da casa
salário
quantos anos pagando

não pode exceder 30% do salário ou será negado
'''
#entrada de dados e interação com usuário
print('Olá! Seja bem-vindo(a) ao Financiamento Online da CAIXA!')
valor = int(input('Para começarmos, digite o valor da casa que quer financiar em questão: R$'))
print('Perfeito!')
salario = int(input('Agora, preciso que digite quanto é seu salário líquido mensal: R$'))
print('Maravilha!')
anos = int(input('Agora, para finalizar e saber se foi aprovado, digite em quantos anos pretende pagar pelo financiamento: '))

#processamento de dados
tempo_mes = anos * 12
prestacao = valor / tempo_mes
if prestacao <= salario * 30 /100:
    print('PARABÉNS! Seu financiamento foi aprovado.')
    print('Sua prestação será de {:.2f}, durante {} meses.'.format(prestacao, tempo_mes))
else:
    print('Infelizmente não será possível realizar a operação.')
    print('Mas não desanime! Quando as coisas melhorarem, volte aqui e tente mais uma vez!. \nAté logo.')

#fim