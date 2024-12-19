from math import sqrt, pow
catOp = float(input("Digite o comprimento do cateto oposto: "))
catAd = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = sqrt(pow(catOp,2) + pow(catAd,2)) 
print("O comprimento da hipotenusa será de: {}".format(hipotenusa))