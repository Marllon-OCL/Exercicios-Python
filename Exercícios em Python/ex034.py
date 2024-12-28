salario = float(input('Informe o valor do seu salário atual: '))

# averifica o salário para informar o aumento
if salario > 1250:
    aumento = (salario * 10/100)
elif salario <= 1250:
    aumento = (salario * 15/100)
print('Seu aumento é de R${:,.2f}'.format(aumento))