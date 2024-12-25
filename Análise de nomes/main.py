#entrada de dados
nome = str(input('Digite seu nome completo: ')).strip()
#processamento e saída de dados
print('O seu nome com todas as letras maiúsculas é igual a {}.'.format(nome.upper()))
print('O seu nome com todas as letras minúsculas é igual a {}.'.format(nome.lower()))
print('A quantidade de letras em seu nome, sem contar espaços, é igual a {}.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))

#fim