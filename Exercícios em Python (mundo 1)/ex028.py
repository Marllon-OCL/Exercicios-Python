import random

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
num = random.randint(0, 5)
chute = int(input('Em que número eu pensei? '))

# Verifica se o chute é correto ou errado
if chute == num:
    print('Parabéns! Você acertou!')
else:
    print(f'Você errou! Eu pensei no número {num}.')