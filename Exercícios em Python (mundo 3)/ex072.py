por_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", 
               "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
valor = int(input("Digite um número ente 0 e 20: "))
while not 0 <= valor <= 20:
    valor = int(input("Tente novamente. Digite um número entre 0 e 20: "))
print(f"Você digitou o número {por_extenso[valor]}")
    