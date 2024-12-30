n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

# Verifica qual número é maior
if n1 > n2 and n1 > n3:
    print('\n{} é maior!'.format(n1))
elif n2 > n1 and n2 > n3:
    print('\n{} é maior!'.format(n2))
else:
    print('\n{} é maior!'.format(n3))

# Verifica qual número é menor
if n1 < n2 and n1 < n3:
    print('{} é menor!'.format(n1))
elif n2 < n1 and n2 < n3:
    print('{} é menor!'.format(n2))
else:
    print('{} é menor!'.format(n3))