lista = []
while True:
    valor = int(input("Digite um valor: "))
    if valor not in lista:
        print("Valor adicionado com sucesso...")
        lista.append(valor)
    else:
        print("Valor duplicado! Não vou adicionar...")
    escolha = input("Quer continuar? [S/N] ").strip().upper()[0]
    if escolha in "Nn":
        break
print(30*"-=")
lista.sort()
print(f"Você digitou os valores {lista}")
