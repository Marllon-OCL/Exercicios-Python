peso = float(input('Informe seu peso em Kg: '))
altura = float(input('Informe sua altura em metros: '))

imc = peso / (altura**2)
print(f'IMC calculado: {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
else:
    print('Obesidade Morbida.')