valorCasa = float(input('Informe o valor da residência para compra: '))
salario = float(input('informe seu salário atual: '))
pagamentoAno = int(input('Informe o prazo (em anos) para  o pagamento: '))

prestacao = valorCasa / (pagamentoAno * 12)
if prestacao > (30/100 * salario):
    print(r'Emprestimo negado! O valor da parcela excedeu os 30% do seu salário.')
else: 
    print('Emprestimo aceito! O valor da parcela será de R${:.2f}'.format(prestacao))