numero = int(input('Digite um número: '))
print('- 1 para Binário; \n- 2 para Octal; \n- 3 para Hexadecimal.')
escolha = int(input('Escolha a forma de converção: '))

if escolha == 1:
    print('O número informado convertido para binário é {:b}'.format(numero))
elif escolha == 2: 
    print('O número informado convertido para octal é {:o}'.format(numero))
elif escolha == 3:
   print('O número informado convertido para hexadecimal é {:x}'.format(numero))
        