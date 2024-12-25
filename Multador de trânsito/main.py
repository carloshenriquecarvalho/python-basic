#entrada de dados
velocidade = float(input('Digite a velocidade do carro: '))
if velocidade <= 80:
    print('Tenha um bom dia e continue dirigindo prudentemente!')
else:
    print('Sua velocidade foi de {}km/h. Você receberá uma multa de R${:.2f}.'.format(velocidade, (velocidade - 80) * 7))

#fim