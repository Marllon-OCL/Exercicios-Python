salario = float(input('Informe o valor do seu salário atual R$: '))

# averifica o salário para informar o aumento
if salario <= 1250:
    aumento = (salario * 15/100)
else:
    aumento = (salario * 10/100)
total = salario + aumento
print('Seu aumento é de R${:,.2f} e passará a receber R${:,.2f}'.format(aumento, total))
