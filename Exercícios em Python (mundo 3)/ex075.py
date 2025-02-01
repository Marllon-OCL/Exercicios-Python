valores = ()
cont = 0
while True:
    n = int(input("Digite um valor: "))
    valores += (n,)
    cont += 1
    if len(valores) == 4: 
        break
print(f"O valor 9 apareceu {valores.count(9)} vezes.")
print(f"O valor 3 apareceu na {valores.index(3)+1}ª posição," if 3 in valores else "O valor três não foi digitado em nenhuma posição.")
print(f"Os valores pares digitados foram: ", end="")
for n in valores:
    if n%2 == 0:
        print(f"{n}", end=" ")
