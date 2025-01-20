sexo = input('Informe seu sexo [M ou F]: ').strip().upper()[0]
while sexo not in 'MF':
    print('Resposta inválida!')
    sexo = input('Informe seu sexo [M ou F]: ').strip().upper()[0]
print(f'Sexo {sexo} cadstrado com sucesso.')
print('Obrigado pela a atenção.')
