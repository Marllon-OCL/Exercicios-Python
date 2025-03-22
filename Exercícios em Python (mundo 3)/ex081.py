lista = []
while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    escolha = input("Quer continuar? [S/N] ").strip().upper()[0]
    if escolha in "Nn":
        break
lista.sort(reverse=True)
print(30*"-=")
print(f"Você digitou {len(lista)} elementos.")
print(f"Os valores em ordem decrescente são {lista}")
print("O valor 5 faz parte da lista!" if 5 in lista else "O valor 5 não foi encontrado na lista!")
