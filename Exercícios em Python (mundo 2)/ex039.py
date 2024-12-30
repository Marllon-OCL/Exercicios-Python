from datetime import date

anoAtual = date.today().year
anoNascimeto = int(input('Informe seu ano de nascimento: '))
idade = anoAtual - anoNascimeto

if idade < 18:
    print(f'Ainda vai se alistar ao serviço militar. Falta(m) {18 - idade} anos.')
elif idade == 18:
    print('Está na hora de se alistar ao serviço militar.')
else:
    print(f'Já passou do tempo de alistamento. Se passaram {idade - 18} anos.')