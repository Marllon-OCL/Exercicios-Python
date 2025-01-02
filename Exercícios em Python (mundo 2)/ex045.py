import random
jokenpo = ['Pedra','Papel','Tesoura']

print('Vamos jogar Jokenpo.')
print('- Pedra; \n- Papel; \n- Tesoura.')

while True:
    escolha = input('Faça sua escolha: ').capitalize()
    system = random.choice(jokenpo)
    if escolha in jokenpo:
        print(f'\nSua escolha: \033[33m{escolha}.\033[m')
        print(f'Escolha do Computador: \033[33m{system}.\033[m')
        if escolha == system:
            print('Houve um \033[34mEMPATE!\033[m\n')
        elif escolha == 'Pedra' and system == 'Tesoura':
            print('Você \033[32mVENCEU!\033[m\n')
        elif escolha == 'Papel' and system == 'Pedra':
            print('Você \033[32mVENCEU!\033[m\n')
        elif escolha == 'Tesoura' and system == 'Papel':
            print('Você \033[32mVENCEU!\033[m\n')
        else:
            print('Você \033[31mPERDEU!\033[m\n')
    else:
        print('\033[31mOpção Inválida.\033[m\n')
    print('- Sim \n- Não')
    continuar = input('Quer continuar: ').capitalize()
    if continuar == 'Sim':
        input('Pressione Enter para continuar: ')
    else:
        print('Até mais!!!')
        break