#entrada de dados (conversor de temperaturas)
celcius = float(input('Digite a temperatura em Celcius: '))

#processamento de dados
fahrenheit = float(celcius * 1.8) + 32

#saída de dados
print('A temperatura de {:.1f}ºC em ºF é igual a {:.1f}ºF'.format(celcius, fahrenheit))

#fim