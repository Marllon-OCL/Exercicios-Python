from datetime import date
atual = date.today().year

menor = 0
maior = 0
for i in range(1,8):
    anos = int(input('Digite o ano de nascimento da {}° pessoa: '.format(i)))
    if (atual - anos) < 21:
        menor += 1
    else:
        maior += 1
            
print(f'''Há {menor} pessoa(s) que não é/são maior de idade 
e há {maior} pessoa(s) que é/são maior de idade.''')
