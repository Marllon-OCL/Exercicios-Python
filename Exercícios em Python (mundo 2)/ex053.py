print('-= Analisador de Palindromos =-')
frase = input('Digite a frase: ').strip()

letras = []
for letra in frase:
    if letra != ' ':
        letras.append(letra)
semEspaco = ''.join(letras)

if semEspaco.lower() == semEspaco[::-1].lower():
    print('A frase "{}" é um PALINDROMO.'.format(frase.upper()))
else:
    print('A frase "{}" não é um PALINDROMO.'.format(frase.upper()))
print('e seu inverso é "{}".'.format(semEspaco[::-1].upper()))
