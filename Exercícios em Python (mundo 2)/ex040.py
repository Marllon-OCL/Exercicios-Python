nota2 = float(input('Digite a primera nota: '))
nota1 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Aluno REPROVADO com a média {media} ! ')
elif 7 > media >= 5:
    print(f'Aluno de RECUPERÇÃO com a média {media} !')
else:
    print(f'Aluno APROVADO com a média {media} !')