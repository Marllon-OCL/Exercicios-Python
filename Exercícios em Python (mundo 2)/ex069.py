mais18 = homens = mulheres_menos20 = 0
print(21*"-")
print(" CADASTRO DE PESSOAS ")
while True:
    print(21*"-")
    idade = int(input("Informe sua idade: "))
    if idade > 18:
        mais18 += 1
    sexo = ' '
    while sexo not in "MF":
        sexo = input("Informe seu sexo [F/M] ").strip().upper()[0]
        if sexo == "F":
            if idade < 20:
                mulheres_menos20 += 1
            break
        elif sexo == "M":
            homens += 1
            break
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    while continuar not in "SN":
        print("Resposta inválida! Informe S ou N.")
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break
print(21*"-=")
print(f"Pessoas cadastradas com mais de 18 anos: {mais18}")
print(f"Número de homens cadastrados: {homens}")
print(f"Número de mulheres cadastradas com menos de 20 anos: {mulheres_menos20}")
