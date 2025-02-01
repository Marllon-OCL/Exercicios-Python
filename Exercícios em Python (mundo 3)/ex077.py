p = ("aprender", "programar", "linguagem", "python", "curso", "gratis", 
     "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")
for i in p:
    print(f"\nNa palavra {i.upper()} temos ",end="")
    for l in i:
        if l.lower() in "aeiou":
            print(l,end=" ")
            