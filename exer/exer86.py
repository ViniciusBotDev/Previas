from random import randint
from operator import itemgetter
itens = {'Jogador 1': randint(1,6),'Jogador 2' : randint(1,6), 'Jogador 3' : randint(1,6), 'Jogador 4' : randint(1,6)}
ranking = []
for k, v in itens.items():
    print(f'O jogador {k} tirou {v}')
ranking = sorted(itens.items(), key=itemgetter(1), reverse=True)
print('='*30)
for i,v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')