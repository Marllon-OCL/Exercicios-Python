import random

# Lista do nome dos alunos
alunos = []

# Ler o nome dos alunos
while True:
    nomes = input("Digite o nome do aluno: ")
    alunos.append(nomes)
    random.shuffle(alunos)
    if len(alunos) == 4:
        break

# Sortear a ordem de apresentação
print("\nAlunos sorteados: ")
for i, nomes in enumerate(alunos):
    print("{}° aluno(a): {}".format(i+1, nomes))