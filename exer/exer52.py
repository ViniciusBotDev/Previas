maxx = 0
minn = 0
for p in range(1,6):
    peso = float(input(f'Digite o peso da pessoa n{p}:  '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'A pessoa mais magra é {menor} e gordo {maior}')