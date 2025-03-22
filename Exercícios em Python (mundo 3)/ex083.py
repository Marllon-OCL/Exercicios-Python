expressao = input("Digite uma expressão: ")
pilha = []
for c in expressao:
    if c == "(":
        pilha.append(c)
    elif c == ")":
        if pilha:
            pilha.pop()
        else:
            pilha.append(c)
if pilha:
    print("Expressão inválida!")
else:
    print("Expressão válida!")
