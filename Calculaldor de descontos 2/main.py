#entrada de dados
valor_primario = float(input('Digite o valor do produto: R$'))
metodo_de_pagamento = int((input('Escolha a forma de pagamento: '
                             '\n1 - À vista com dinheiro com 10% de desconto'
                             '\n2 - À vista no cartão com 5% de desconto'
                             '\n3 - 2x no cartão sem juros'
                             '\n4 - 3x ou mais no cartão com 20% de juros ')))
if metodo_de_pagamento == 1:
    print('Total a pagar será de R${:.2f}'.format(valor_primario - (valor_primario * 10 / 100)))
elif metodo_de_pagamento == 2:
    print('Total a pagar será de R${:.2f}'.format(valor_primario - (valor_primario * 5 / 100)))
elif metodo_de_pagamento == 3:
    print('Você pagará em duas vezes de R${:.2f}'.format(valor_primario / 2))
elif metodo_de_pagamento == 4:
    print('Você pagará 3 parcelas de R${:.2f}'.format((valor_primario + (valor_primario * 20 /100)) / 3))