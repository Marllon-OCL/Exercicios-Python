km = float(input("Quantos Km rodados? "))
dias = int(input("Por quantos dias o carro foi alugado? "))
preco = (60 * dias) + (0.15 * km)
print("O toatl a pagar pelo aluguel: R${}".format(preco))