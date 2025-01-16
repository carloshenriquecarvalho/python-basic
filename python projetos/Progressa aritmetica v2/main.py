p = int(input('Digite o primeiro termo da progressão: '))
p1 = p
razao = int(input('Digite a razão: '))
c = 0
print(p1, end=' ➝')
qnt = 10
while c != qnt:
  p += razao
  c += 1
  print(p, end=' ➝')
qnt = int(input('\nQuer ver mais algum termo?\n'
                '[0] Não'
                '\n Ou digite a quantidade de novos termos:\n'))
print('fim')
while c != qnt + 10 and c != 0:
  p += razao
  c += 1
  print(p, end=' ➝')
print('Fim')