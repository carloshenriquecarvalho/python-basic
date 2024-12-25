#entrada de dados
altura = float(input('Digite sua altura, por favor '))
peso = float(input('Digite o seu peso '))
imc = peso / pow(altura, 2)
if imc < 18.5:
    print('Você está abaixo do peso. Tome cuidado!')
elif 18.5 < imc < 25:
    print('Você está com peso ideal!')
elif 25 < imc < 30:
    print('Você está com sobrepeso!')
elif 30 < imc < 40:
    print('Você está no estágio de obesidade!')
else:
    print('Você está com obesidade mórbida!')