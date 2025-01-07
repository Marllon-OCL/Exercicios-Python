pesos = []
for i in range(1,6):
    peso = float(input(f'Informe o peso da {i}° pessoa: '))
    pesos.append(peso)
    
maior = max(pesos)
menor = min(pesos)
print(f'O maior peso é de {maior} Kg')
print(f'O menor peso é de {menor} Kg')
    