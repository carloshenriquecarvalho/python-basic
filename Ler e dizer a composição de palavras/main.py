#entrada de dados
s = input('Digite algo: ')

#saída de dados
print('O termo "{}" é'.format(s), type(s), '. Possui os seguintes valores: ') #tipo primitivo
print('É um numérico? ', s.isnumeric())
print('É um alfanumérico? ', s.isalnum())
print('É um alfabético? ',s.isalpha())
print('Caracteres ASCII? ' ,s.isascii())
print('É um digito? ' ,s.isdigit())
print('É um decimal? ' ,s.isdecimal())
print('É um identificador? ', s.isidentifier())
print('É em minúscula? ',s.islower())
print('É em maiúscula? ', s.isupper())
print('É imprimível? ', s.isprintable())
print('Somente espaços? ', s.isspace())
print('Está capitalizado? ', s.istitle())

