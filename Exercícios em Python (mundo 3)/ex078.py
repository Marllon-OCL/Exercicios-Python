lista = []
for v in range(0,5):
    lista.append(int(input(f"Digite um valor para a Posição {v}: ")))
print(30*"=-")
print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {max(lista)} nas posições ",end="")
for i in range(0,len(lista)):
    if lista[i] == max(lista):
        print(i,end="... ")
print(f"\nO menor valor digitado foi {min(lista)} nas posições ",end="")
for i in range(0,len(lista)):
    if lista[i] == min(lista):
        print(i,end="... ")
