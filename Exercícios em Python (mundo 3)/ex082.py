lista = []
while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    escolha = " "
    while escolha not in "SN":
        escolha = input("Quer continuar? [S/N] ").strip().upper()[0]
    if escolha == "N":
        break
pares = []
impares = []
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(30*"-=")
print(f"A lista completa é {lista}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")
