expressao = input("Digite uma expressão: ")
pilha = []
for c in expressao:
    if c == "(":
        pilha.append(c)
    elif c == ")":
        if pilha.count("(") == 0:
            pilha.append(c)
        else:
            pilha.pop()
if len(pilha) > 0:
    print("Expressão inválida!")
else:
    print("Expressão válida!")
