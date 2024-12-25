#entrada de dados (calculadora de média)
nota1 = float(input('Digite a nota do primeiro semestre: '))
nota2 = float(input('Digite a nota do segundo semestre: '))

#processamento de dados (média e status de aprovação)
res = float((nota1 + nota2) / 2)
status = bool(res >= 5)

#saída de dados (resultado e nota)
print('Sua média é {:.1f}! Seu status de aprovação é {:.1f}.'.format(res, status))

#fim