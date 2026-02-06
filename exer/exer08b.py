from random import shuffle, choice

lista = input('Digite os 4 nomes separados por espaço:  ').split()

escolhido = choice(lista)
print(f'O nome escolhido para apagar o quadro foi {escolhido}')

shuffle(lista)
print(f'E a ordem de apresentação é {', '.join(lista)}')