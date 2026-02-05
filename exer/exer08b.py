import random

nomes = input('Digite os 4 nomes separados por espaço:  ').split()

escolhido = random.choice(nomes)
print(f'O nome escolhido para apagar o quadro foi {escolhido}')

random.shuffle(nomes)
print(f'E a ordem de apresentação é {', '.join(nomes)}')