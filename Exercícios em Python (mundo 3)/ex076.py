produtos_valores = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, 
                    "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, 
                    "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
print(39*"-")
print(f"{'LISTAGEM DE PREÇOS':^39}")
print(39*"-")
for i in range(0,len(produtos_valores),2):
    print(f"{produtos_valores[i]:.<30}R$ {produtos_valores[i+1]:6.2f}")
print(39*"-")
    