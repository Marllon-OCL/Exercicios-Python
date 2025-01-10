print('-= Criador de sequência de Fibonacci =-')
limite = int(input('Digite um valor de limite da sequência: '))
print(f'Os {limite} primeiros termos dessa sequência.')
sequencia = 1
soma = 0
cont = 0
while cont < limite:
    print(soma, end=' - ')
    soma += sequencia
    sequencia = soma - sequencia
    cont += 1
print('FIM')