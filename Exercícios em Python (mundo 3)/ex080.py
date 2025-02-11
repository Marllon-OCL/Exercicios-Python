lista = []
while True:
    valor = int(input("Digite um valor: "))
    if len(lista) == 0 or valor > lista[-1]:
        lista.append(valor)
        print("Adicionado ao final da lista...")
    elif valor < lista[0] :
        lista.insert(0,valor)
        print("Adicionado na posição 0 da lista...")
    else:
        for i in range(1,len(lista)):
            if valor < lista[i]:
                lista.insert(i,valor)
                print(f"Adicionado na posição {i} da lista...")
    if len(lista) == 5:
        break
print(f"\n{lista}")
