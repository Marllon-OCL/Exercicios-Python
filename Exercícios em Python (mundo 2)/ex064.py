quantidade = 0
soma = 0
numero = int(input('Digite um número (Digite 999 para parar): '))
while numero != 999:
    quantidade += 1
    soma += numero
    numero = int(input('Digite um número (Digite 999 para parar): '))

print(f'Foram digitados {quantidade} números e a soma entre eles é {soma}.')
