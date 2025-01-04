lado1 = int(input('Digite a medida da primeira reta: '))
lado2 = int(input('Digite a medida da segunda reta: '))
lado3 = int(input('Digite a medida da terceira reta: '))

# Verifica se a soma de dois lados é maior que o terceiro
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Essas retas FORMAM um triângulo!')
else:
    print('Essas retas NÃO FORMAM um triângulo!')
