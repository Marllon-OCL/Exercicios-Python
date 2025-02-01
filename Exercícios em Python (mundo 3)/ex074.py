from random import randint
numeros = ()
cont = 0
print("Os valores sorteados foram: ",end="")
while True:
    numeros += (randint(0, 100),)
    print(f"{numeros[cont]}",end=" ")
    cont += 1
    if len(numeros) == 5:
        break
maior = max(numeros)
menor = min(numeros)
print(f"\nO maior valor sorteado foi {maior}")
print(f"O menor valor sorteado foi {menor}")