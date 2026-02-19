soma = 0
for c in range(1,8):
    pessoas = int(input(f'Digite a idade da pessoa numero {c}:  '))
    if pessoas >= 18:
        soma += +1
print(f'Pessoas maiores: {soma}')