valores = []
maior = 0
menor = 0
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para posição {cont+1}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'Voçe digitou os valores{valores}')
print(f'Maior valor digitado foi {maior} na posiçao ',end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i+1}...', end='')    
print(f'\nMenor valor digitado foi {menor} na posiçao ',end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i+1}...', end='')
        