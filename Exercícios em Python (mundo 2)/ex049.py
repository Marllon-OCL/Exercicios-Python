n = int(input('Digite um número: '))
print('tabuada do {}.'.format(n))
for i in range(1,11):
    print('{} x {} = {}'.format(i, n, i * n))
    