'''num = int(input('Digite um número: '))

c = 1
r = 1
while c <= num:
  r *= c
  c += 1
print(r)'''

num = int(input('Digite um número: '))
r = 1
for x in range(1, num + 1):
  r *= x
print(r)