#entrada de dados
km = int(input('Quantos quilômetros é a sua viagem? '))
print('Você está prestes a começar uma viagem com {}km,'.format(km))
if km <= 200:
    print('O valor total a pagar é R${:.2f}.'.format(km * 0.50))
else:
    print('O valor total a pagar é R${:.2f}.'.format(km * 0.45))
#fim