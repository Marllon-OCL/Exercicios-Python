lado1 = int(input('Digite a medida da primeira reta: '))
lado2 = int(input('Digite a medida da segunda reta: '))
lado3 = int(input('Digite a medida da terceira reta: '))

if lado1 + lado2 > lado3:
    print('\nEssas retas formam um triângulo!')
    if lado1 == lado2 == lado3:
        print('E é um triângulo EQULÁTERO.')
    elif lado1 != lado2 != lado3 != lado1:
        print('E é um trinângulo ESCALENO.')
    else:
        print('E é um triâmgulo ISÓCELES.')
else:
    print('\nEssas retas não formam um triângulo!')