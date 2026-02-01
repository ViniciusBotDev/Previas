opcao = 's'
num = int

while opcao in ['s', 'sim']:
 
    num = int(input('Digite um numero na qual deseja ver a tabuada: '))
    print('=' * 13)
    
    for cont in range(1, 11):
        print(f'{num} x {cont:2} = {num * cont}')

    print('=' * 13)
    opcao = input('Digite [S/N] se quiser repitir: ').strip().lower()
