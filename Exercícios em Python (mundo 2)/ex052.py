n = int(input('Digite um número: '))

cont = 0
for i in range(1, n+1):
    if n%i == 0:
        cont += 1
        print('\033[31m{}\033[m'.format(i), end= ' ')
    else:
        print('\033[33m{}\033[m'.format(i), end= ' ')
        
if cont == 2:
    print('\nO número {} É PRIMO.'.format(n))
else:
    print('\nO número {} NÃO É PRIMO, pois tem {} divisores.'.format(n, cont))        
    