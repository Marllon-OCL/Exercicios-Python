from random import randint

print("VAMOS JOGAR PAR OU ÍMPAR")
v = 0
while True:
    jogador = int(input("Diga um valor: "))
    escolha = input("Par ou Ímpar? [P/I] ").strip().upper()[0]
    computador = randint(1,10)
    soma = computador + jogador
    print(f"Você jogou {jogador} e o computador {computador}. Total de {soma}", end=" ")
    if escolha == "P":
        if soma % 2 == 0:
            print("DEU PAR")
            print("Você VENCEU!")
            v += 1
        else:
            print("DEU ÍMPAR")
            print("Você PERDEU!")
            break
    elif escolha == "I":
        if soma % 2 == 1:
            print("DEU ÍMPAR")
            print("Você VENCEU!")
            v += 1
        else:
            print("DEU PAR")
            print("Você PERDEU!")
            break
    print("Vamos jogar de novo...")        
print(f"GAME OVER! Você venceu {v} vezes")     
    