from time import sleep

a = int(input('digite um número: '))
b = int(input('digite outro número: '))

c = 0
while c < 1:
    print('''-=-=-=-=-=-=-=-=-=-
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Valores
[5] Fechar Sistema''')
    escolha = int(input('escolha: '))
    if escolha == 1:
        soma = a + b
        print(f'A soma dos valores é {soma}')
    if escolha == 2:
        mult = a * b
        print(f'A multiplicação entre os valores é {mult}')  
    if escolha == 3:
        maior = max([a, b])
        print(f'O maior entre os valores é {maior}')
    if escolha == 4:
        a = int(input('Novo valor: '))
        b = int(input('Novo valor: '))
    if escolha == 5:
        print('Desligando o Sistema...')
        sleep(3)
        c = 1
            