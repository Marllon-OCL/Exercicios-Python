from math import hypot
catOp = float(input("Digite o comprimento do cateto oposto: "))
catAd = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = hypot(catOp, catAd)
print("O comprimento da hipotenusa será de: {}".format(hipotenusa))