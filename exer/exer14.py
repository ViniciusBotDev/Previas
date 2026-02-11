import random

numero_aleatorio = random.randint(1, 5)
print('Pensando em um número...')
numero_escolhido = int(input('Escolha um número digitando entre 1 a 5 :  '))
if numero_escolhido == numero_aleatorio:
    print('Parabens voçe acertou o numero')
else:
    print(f'Errado o número certo era {numero_aleatorio}, voçe errou')