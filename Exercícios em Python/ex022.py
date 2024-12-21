# Ler o nome completo
nome = str(input('Digite seu nome completo: ')).strip()

# Transformar as letras em maiúsculas
print('\nSeu nome com todas as letras maiúsculas: {}'.format(nome.upper()))

# Transformar as letras em minúsculas
print('Seu nome com todas a letras minúsculas: {}'.format(nome.lower()))

# Contar quantas letras, mas sem contar os espaços
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))

# Contar quantas letas tem o primeiro nome
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))