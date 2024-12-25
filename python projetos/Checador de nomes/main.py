#entrada de dados
nome_cidade = str(input('Digite o nome da sua cidade: ')).strip()
nome_separado = nome_cidade.split() #separa as partes do nome da cidade
inicio_nome = nome_separado[0].upper() #transforma todas as letras do primeiro nome em uppercase
situacao = inicio_nome.find('SANTO') #procura pela palavra Santo

#saída de dados
if situacao == 0:
  print('Sua cidade começa sim com Santo!')
else:
  print('Sua cidade não começa com Santo!')

print(nome_cidade[:5].upper() == 'SANTO')


#fim