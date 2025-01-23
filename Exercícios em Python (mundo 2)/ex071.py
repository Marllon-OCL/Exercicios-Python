print(29*"=")
print("          BANCO OCL          ")
print(29*"=")
valor = int(input("Que valor você quer sacar? R$"))
cinquenta = valor // 50
resto = valor % 50
vinte = resto // 20
resto = resto % 20
dez = resto // 10
resto = resto % 10
um = resto // 1
while True:
    if cinquenta > 0:
        print(f"Total de {cinquenta} cédulas de R$50.00")
    if vinte > 0:
        print(f"Total de {vinte} cédulas de R$20.00")
    if dez > 0:
        print(f"Total de {dez} cédulas de R$10.00")
    if um > 0:
        print(f"Total de {um} moedas de R$1.00")    
    break
print(29*"=")
print("Volte sempre ao BANCO OCL! Tenha um bom dia!")    