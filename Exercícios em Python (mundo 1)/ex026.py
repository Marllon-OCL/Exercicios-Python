frase = str(input('Digite algo: ')).strip().upper()
print('A letra (A) aparece {} vezes.'.format(frase.count('A')))
print('A letra (A) aparece pela primeira vez na {}° posição.'.format(frase.find('A')+1))
print('A letra (A) aparece pela última vez na {}° posição.'.format(frase.rfind('A')+1))