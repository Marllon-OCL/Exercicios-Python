quantidade = 0
soma = 0
cont = 0
while cont < 1:
    numero = int(input('Digite um número (Digite 999 para parar): '))
    if numero < 999:
        soma += numero
        quantidade += 1
    else:
        cont = 1
print(f'Foram digitados {quantidade} números e a soma entre eles é {soma}.')
