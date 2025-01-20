import random

print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
computador = random.randint(0, 10)
acertou = False
cont = 0
while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    cont += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Erro! Um pouco maior.')
        else:
            print('Errou! Um pouco menor.')
print('Parabéns! Você adivinhou!')
print(f'Tentativas: {cont}')
