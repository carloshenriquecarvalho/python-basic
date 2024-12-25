#transformar bases de números solicitados
num = int((input('Olá, tudo bem? Digite o número que você quer transformar: ')))
print('Perfeito! Agora escolha a base que quer transformar')
esc = int(input('1 - Binário'
                '\n2 - Octal'
                '\n3 - Hexadecimal '))
if esc == 1:
    print('O valor {} em base binária é igual a {}.'.format(num, bin(num)))
elif esc == 2:
    print('O valor {} em base octal é igual a {}.'.format(num, oct(num)))
elif esc == 3:
    print('O valor {} em base hexadecimal é igual a {}.'.format(num, hex(num)))
print('Obrigado por acessar o Convert.com!')