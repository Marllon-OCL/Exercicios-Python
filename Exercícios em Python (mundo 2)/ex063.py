print('-= Criador de sequência de Fibonacci =-')
n = int(input('Digite um valor de limite da sequência: '))
print(f'Os {n} primeiros termos dessa sequência.')
cont = 3
t1 = 0
t2 = 1
print(f'{t1} - {t2}', end=" - ")
while cont <= n:
    t3 = t1 + t2
    print(t3, end=" - ")
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')