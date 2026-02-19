import random
from time import sleep

lista = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('Faça sua escolha entre Pedra, Papel e Tesoura')
print('''Faça sua escolha:'
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
sua_escolha = int(input('Qual é a sua jogada?  '))
print('Jogando..')
print('-=' * 15)
sleep(2)
print(f'Computador {(lista[computador])}')
print(f'Jogador {(lista[sua_escolha])}')
print('-=' * 15)
if computador == 0: 
    if sua_escolha == 0:
        print('EMPATE!')
    elif sua_escolha == 1:
        print('Jogador Ganhou!')
    elif sua_escolha == 2:
        print('Computador ganhou!')
    else:
        print('Jogada inválida..')
elif computador == 1: 
    if sua_escolha == 0:
        print('Computador ganhou!')
    elif sua_escolha == 1:
        print('EMPATE!')
    elif sua_escolha == 2:
        print('Jogador ganhou!')
    else:
        print('Jogada inválida..')
elif computador == 2: 
    if sua_escolha == 0:
        print('Jogador ganhou!')
    elif sua_escolha == 1:
        print('Computador ganhou!')
    elif sua_escolha == 2:
        print('EMPATE!')
else:
    print('Voçe escolheu algo inválido...')