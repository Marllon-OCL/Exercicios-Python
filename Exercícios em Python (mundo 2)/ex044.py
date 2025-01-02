produto = float(input('Informe o valor do produto: '))
print('1 - À vista em dinheiro/cheque \n2 - Cartão')
pagamento = int(input('Escolha a opção de pagamento: '))

if pagamento == 1:
    desconto = produto - (produto * 10/100)
    print(f'\nO valor da compra será de \033[32mR${desconto:.2f}\033[m.')
elif pagamento == 2:
    print('1 - À vista \n2 - Parcelado \033[m')
    escolha = int(input('Escolha a forma de passar o cartão: '))
    if escolha == 1:
        desconto = produto - (produto * 5/100)
        print(f'\nO valor da compra será de \033[32mR${desconto:.2f}\033[m.')
    elif escolha == 2:
        parcelas = int(input('Informe o número de parcelas: ')) 
        if parcelas == 2:
            print('\nO valor do produto será de \033[32mR${:.2f}\033[m.'.format(produto))
        elif parcelas >= 3:
            juros = produto + (produto * 20/100)
            print(f'\nO valor do produto será de \033[32mR${juros:.2f}\033[m.')