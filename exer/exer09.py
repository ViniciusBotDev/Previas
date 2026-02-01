import random

numpc = random.randint(1, 10)
Tentativas = 0

print('Pensei em um número tente advinhar!')
while True:
    chute = int(input('Qual seu palpite?  '))
    Tentativas += 1

    if chute == numpc:
        print(f'Parabéns voçe acertou o número, e precisou de {Tentativas} tentativas!')
        break
    elif chute < numpc:
        print('Mais alto...')
    else:
        print('Mais baixo...')
