n = str(input('Digite seu nome completo: ')).strip()
nome = n.split() 
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[-1]))