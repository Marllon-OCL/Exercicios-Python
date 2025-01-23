total = mais_mil = 0
preco_mais_barato = float('inf')
nome_mais_barato = ""
print(21*"-")
print(" LOJA SUPER BARATÃO ")
while True:
    print(21*"-")
    while True:
        produto = input("Nome do produto: ").strip()
        if produto == "":
            print("Campo Vazio!")
            continue
        break
    while True:
        preco = float(input("Preço: R$"))
        if preco > 1000:
            mais_mil += 1
        total += preco
        if preco < preco_mais_barato:
            nome_mais_barato = produto
            preco_mais_barato = preco
        break
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    while continuar not in "SN":
        print("Resposta inválida! Informe S ou N.")
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break
print("----------- FIM DO PROGRAMA -----------")
print(f"Total da compra foi R${total:.2f}")
print(f"Temos {mais_mil} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {nome_mais_barato} que custa R${preco_mais_barato}")