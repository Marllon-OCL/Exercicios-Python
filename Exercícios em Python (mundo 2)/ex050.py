pares = []
cont = 0
for i in range(1,7):
    numeros = int(input('Digite o {}° número: '.format(i)))
    if numeros%2 == 0:
        cont += 1
        pares.append(numeros)
print('\nHá {} números inteiros pares e a soma deles é {}. '.format(cont, sum(pares)))
    