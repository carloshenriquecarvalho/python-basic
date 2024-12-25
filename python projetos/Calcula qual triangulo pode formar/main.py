#entrada de dados
ca1 = float(input('Digite o valor do primeiro cateto '))
ca2 = float(input('Digite o valor do segundo cateto '))
ca3 = float(input('Digite o valor do terceiro cateto '))

if ca3 == ca2 and ca3 == ca1:
    print('Este triângulo é um equilátero!')
elif ca1 == ca2 and ca1 != ca3:
    print('Es triângulo é um isósceles!')
elif ca1 != ca2 and ca1 != ca3 and ca2 != ca3:
    print('Este triângulo é um escaleno!')