A1 = int(input('Digite o primeiro termo de uma PA: '))
r = int (input('Informe o valor da razão: '))

print('Os 10 primeiros termos dessa PA:')
for n in range(1, 11):
    An = A1 + (n - 1) * r
    print(An, end=" ")
