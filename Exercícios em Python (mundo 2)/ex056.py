maiorIdadeHomem = 0
nomeVelho = ''
totMulherMenor20 = 0
somaIdades = 0

for i in range(1, 5):
    print(f'----- {i}° pessoa -----')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Informe seu sexo [M/F]: ')
    somaIdades += idade
    if i == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulherMenor20 += 1
    
mediaIdades = somaIdades / 4
print(f'\nA média das idades é {mediaIdades} anos')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}.')
print(f'Há {totMulherMenor20} mulheres com menos de 20 anos de idade.')
