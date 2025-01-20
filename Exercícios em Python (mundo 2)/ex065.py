soma = 0
maior = 0
menor = 0
cont = 0
continuar = "S"
while continuar == "S":
    print('-='*12)
    numeros = int(input('Digite um valor: '))
    soma += numeros
    if cont == 0:
        maior = numeros
        menor = numeros
    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros
    continuar = input('Quer continuar? [S ou N]: ').upper()
    if continuar == "S":
        cont += 1
    
media = soma / cont
print('=-'*20)
print(f'A média entre os valores fornecidos é {media}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor fornecido foi {menor}')
