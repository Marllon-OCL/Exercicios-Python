# Tabela do Brasileirão 2023
tabela_br2023 = ("Palmeiras", "Grêmio", "Atlético-MG", "Flamengo", "Botafogo", "Bragantino", "Fluminense", "Athletico_PR", "Internacional", "Fortaleza", "São Paulo", "Cuiabá", "Corinthians", "Cruzeiro", "Vasco da Gama", "Bahia", "Santos", "Goiás", "Coritíba", "América-MG",)

print("{:=^41}".format("RELATÓRIO: BRASILEIRÃO 2023"))
print("Os G5 do campeonato foram:")
for pos,time in enumerate(tabela_br2023[0:5]):
    print(f"{pos+1}° - {time}")
print(41*"-")

print("Os Z4 do campeonato foram:")
for time in tabela_br2023[-4:]:
    print(f"{tabela_br2023.index(time)+1}° - {time}")
print(41*"-")

print("Uma lista com os nomes dos clubes em ordem alfabética:")
ordem_alfabetica = sorted(tabela_br2023)
for i,time in enumerate(ordem_alfabetica):
    print(f"{i+1} - {time}")
print(41*"-")

posicao_clube = tabela_br2023.index("Palmeiras")
print(f"O clube {tabela_br2023[posicao_clube]} está na {(posicao_clube)+1}ª colocação.")
print(41*"-")
