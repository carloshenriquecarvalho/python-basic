#entrada de dados (conversor de R$ para U$D)
valor_real = float(input('Quanto você tem em sua carteira? R$'))

#processamento de dados (conversor)
valor_dolar = float(valor_real / 6.07)

#saída de dados
print('Certo! O valor atual do dólar é igual a R$03,27. Assim, R${:.2f} podem comprar U$D{:.2f} dólares.'.format(valor_real, valor_dolar))

#fim