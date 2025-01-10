import random

print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
computador = random.randint(0, 10)
jogador = int(input('Em que número eu pensei? '))

cont = 1
while jogador != computador:
    print('Você errou! Tente novamente.')
    computador = random.randint(0, 10)
    jogador = int(input('Em que número eu pensei agora? '))
    cont += 1
print('Parabéns! Você adivinhou!')
print(f'Tentativas: {cont}')
