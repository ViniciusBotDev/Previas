pares = []
impares = []
for i in range(1, 8):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'Os números pares digitados foram: {sorted(pares)}')
print(f'Os números ímpares digitados foram: {sorted(impares)}')