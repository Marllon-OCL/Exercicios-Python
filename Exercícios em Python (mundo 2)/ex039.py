from datetime import date

anoAtual = date.today().year
anoNascimeto = int(input('Informe seu ano de nascimento: '))
idade = anoAtual - anoNascimeto

print('Quem nasceu em {} tem {} anos em {}'.format(anoNascimeto, idade, anoAtual))
if idade < 18:
    saldo = 18 - idade
    print(f'Ainda vai se alistar ao serviço militar. Falta(m) {saldo} anos.')
    ano = anoAtual + saldo
    print(f'Você vai se alistar em {ano}')
elif idade == 18:
    print('Está na hora de se alistar ao serviço militar.')
else:
    saldo = idade - 18
    print(f'Já deveria ter se alistado há {saldo} anos.')
    ano = anoAtual - saldo
    print(f'O ano do seu alistamento foi em {ano}')