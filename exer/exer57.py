número = int(input('Digite o seu número:  '))
count = número
f = 1
print(f'Calculando {número} = ', end='')
while count > 0:
    print(f'{count}', end='')
    print(' x ' if count > 1 else ' = ', end='')
    f *= count
    count -= 1
print(f'{f}')
