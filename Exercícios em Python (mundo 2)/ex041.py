from datetime import date
anoAtual = date.today().year

anoNascimento = int(input('Informe seu ano de nascimento: '))

idade = anoAtual - anoNascimento
print(f'Idade: {idade}')
if idade <= 9:
    print('Incluído na categoria MIRIM')
elif idade <= 14:
    print('Icluído na categoria INFANTIL')
elif idade <= 19:
    print('Incluído da categoria JUNIOR')
elif idade <= 25:
    print('Incluído na categoria SÊNIOR')
else:
    print('Incluído na categoria MASTER')