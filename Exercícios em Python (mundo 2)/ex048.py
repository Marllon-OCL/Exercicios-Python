soma = 0
for i in range(1, 501):
    if i%2 != 0 and i%3 == 0:
        soma += i
            
print('''A soma de todos os números ímpares, 
múltiplos de três, entre 1 e 500: ({})'''.format(soma))
            