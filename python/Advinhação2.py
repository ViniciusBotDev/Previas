from random import randint

numero_secreto = randint(1,50)
tentativas = []
acertou = False
pontos = 100

print('--- Jogo da advinhação 2.0 ---')
print(f'Voçe começa com {pontos} e acada erro perde 10. Cuidado!')
while not acertou and pontos > 0:
    chute = int(input('Digite um número entre 1 e 50:  '))
    tentativas.append(chute)
    if chute == numero_secreto:
        acertou = True
        print('Parabéns voçe acertou!!')
    elif chute > numero_secreto:
        print('É mais para baixo..')
        pontos -= 10
    elif chute < numero_secreto:
        print('É mais para cima..')
        pontos -= 10
print('\n------- Final de Jogo -------')
if pontos <= 0 and not acertou:
    print(f'GAME OVER! Seus pontos acabaram. O número era {numero_secreto}')
if len(tentativas) > 1:
    print(f'Voçe precisou de {len(tentativas)} tentativas.')
    print(f'E voçe terminou o jogo com {pontos} pontos!')
else:
    print(f'Voçe precisou de {len(tentativas)} tentativa.')
    print(f'E voçe terminou o jogo com {pontos} pontos !')
for palpites in tentativas:
    print(f'Suas tentativas foram {palpites}')
