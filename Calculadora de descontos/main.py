#entrada de dados (descontos)
valor = float(input('Qual o valo atual do produto? R$'))

#processamento de dados
desconto = valor * 5 /100
valor_descontado = valor - desconto

#saída de dados
print('O produto que custava {:.2f}, agora, com 5% de desconto, vale R${:.2f}.'.format(valor, valor_descontado))

#fim