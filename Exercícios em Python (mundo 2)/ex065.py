soma = 0
maior = 0
menor = 0
quantidade = 0
l = 1
c = 0
while c < l:
    print('-='*12)
    numeros = int(input('Digite um valor: '))
    soma += numeros
    quantidade += 1
    if c == 0:
        maior = numeros
    if numeros > maior:
        maior = numeros
    if numeros < maior:
        menor = numeros
    continuar = input('Quer continuar? [S ou N]: ').upper()
    if continuar == 'S':
        l += 1
        c += 1
    elif continuar == 'N':
        c = l
    else:
        print('Escolha inválida!')
media = soma / quantidade
print('=-'*20)
print(f'A média entre os valores fornecidos é {media}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor fornecido foi {menor}')
