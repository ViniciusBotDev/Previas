from random import randint
vitorias = 0
while True:
    valor_pc = randint(1,10)
    print('=-'*13)
    seu_valor = int(input('Digite um valor:  '))
    soma = seu_valor + valor_pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I]:  ')).strip().upper()[0]
    if soma % 2 == 0:
        print('='*30)
        print(f'Voçe jogou {seu_valor} e o computador {valor_pc}. Total deu {soma} Deu PAR')
        print('='*30)
    else:
        print('='*30)
        print(f'Voçe jogou {seu_valor} e o computador {valor_pc}. Total deu {soma} Deu impar')
        print('='*30)
    if tipo == 'P' and soma % 2 == 0 or tipo == 'I' and soma % 2 == 1:
        print('Voçe VENCEU!')
        print('Vamos jogar novamente...')
        vitorias += 1
    else:
        print('Voçe PERDEU!')
        print('=-'*13)
        print('GAME OVER!')
        print(f'Voçe venceu {vitorias} vezes')
        break
