import random
from time import sleep

numero_aleatorio = random.randint(1, 5)
print('Pensando em um número...')
while True:
    numero_escolhido = int(input('Escolha um número digitando entre 1 a 5 :  '))
    print('Verificando...')
    sleep(2)
    if numero_escolhido == numero_aleatorio:
        print('Parabens voçe acertou o numero')
    else:
        print(f'Voçe errou o numero tente novamente')

