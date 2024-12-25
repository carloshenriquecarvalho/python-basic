#entrada de dados
from random import shuffle
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
alunos = [a, b, c, d]

#processamento de dados
shuffle(alunos)

#saída de dados
print('A ordem de apresentação será: {}'.format(alunos))

#fim