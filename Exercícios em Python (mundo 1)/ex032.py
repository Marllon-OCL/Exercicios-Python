ano = int(input("Digite um ano qualquer no modelo AAAA: "))

# Verifica se é um ano bissexto
if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
    print("{} É um ano bissexto!".format(ano))
else:
    print("{} Não é ano bissexto!".format(ano))