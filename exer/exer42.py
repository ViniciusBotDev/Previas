import random
from time import sleep

lista = ('Pedra Papel Tesoura').split()
print('Faça sua escolha entre Pedra, Papel e Tesoura')
sua_escolha = str(input('Faça sua escolha:  ')).strip().lower()
escolha_maquina = random.choice(lista)
print('Jogando..')
sleep(2)
if sua_escolha == 'papel' and escolha_maquina == 'Pedra':
    print(f'Voce ganhou a maquina escolheu {escolha_maquina}')
elif sua_escolha == 'pedra' and escolha_maquina == 'Tesoura':
    print(f'Voçe ganhou a maquina escolheu {escolha_maquina}')
elif sua_escolha == 'tesoura' and escolha_maquina == 'Papel':
    print(f'Voçe ganhou a maquina escolheu {escolha_maquina}')
elif escolha_maquina == 'Papel' and sua_escolha == 'pedra':
    print(f'Voçe perdeu a maquina escolheu {escolha_maquina}')
elif escolha_maquina == 'Pedra' and sua_escolha == 'tesoura':
    print(f'Voçe perdeu a maquina escolheu {escolha_maquina}')
elif escolha_maquina == 'Tesoura' and sua_escolha == 'papel':
    print(f'Voçe perdeu a maquina escolher {escolha_maquina}')
else:
    print('Voçe escolheu algo inválido...')