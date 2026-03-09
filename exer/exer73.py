listagem = ('Pão', 1.00, 'Leite', 4.50, 'Estojo', 25.00, 'Nata', 5.00, 'Frango', 10.90, 'Caderno', 4.99)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')