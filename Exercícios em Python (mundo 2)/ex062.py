n = int(input('digite o primeiro termo: '))
r = int(input('digite o valor da razão: '))
an = n
cont = 1
limite = 0
mais = 10
while mais != 0:
    limite += mais
    while cont <= limite:
        print(f'{an}', end= ' - ')
        an += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos mais: '))
print('Fim')
print(f'Numero de termos apresentados: {limite}')
