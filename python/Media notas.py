import os

opção = 's'

while desejo in ['s', 'sim']:
    
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Contador de Médias')

    n1 = float(input('Digite sua primeira nota: '))
    n2 = float(input('Digite sua segunda nota: '))
    n3 = float(input('Digite sua terceira nota: '))
    
    nota = (n1 + n2 + n3) / 3

    print(f'Sua nota média final é {nota:.1f}')
    if nota >= 9.0:
        print('\033[1;32mParabéns sua nota está otima!\033[m')
    elif nota >= 7.0:
        print('\033[1;34mEstá bom mas pode ser melhor!\033[m')
    elif nota >= 6.0:
        print('\033[1;33mCuidado da Próxima vez, melhore!\033[m')
    elif nota >= 5:
        print('\033[1;33mVoçe está de recuperação!\033[m')
    else:
        print('\033[1;31mVoçe não consegiu a média, melhore da próxima\033[m')
    opção = input('Deseja continuar? [S/N] ').strip().lower()
    