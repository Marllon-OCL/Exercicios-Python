import random
# Ler o nome dos alunos
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')

# Lista do nome dos alunos
alunos = [aluno1, aluno2, aluno3, aluno4]

# Mensagem do aluno escolhido
print('O aluno sorteado para apagar o quadro é: {}'.format(random.choice(alunos)))