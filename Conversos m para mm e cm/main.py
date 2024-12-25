#entrada de dados (conversor de metros para centímetros e milímetros)
valor_m = float(input('Digite o valor em metros: '))

#processamento de dados
#conversor de metros para centímetros
valor_cm = float(valor_m * 100)

#conversor de metros para milímetros
valor_mi = float(valor_m * 1000)

#saída de dados
#valor em centímetros
print('{} metros em centímetro equivale a {:.2f}cm'.format(valor_m, valor_cm))

#valor em milímetros
print('{} metros em milímetros equivale a {:.2f}mm'.format(valor_m, valor_mi))

#fim