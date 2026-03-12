pessoas = []
dados = []
maiorpeso = maisleves = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    if len(pessoas) == 0:
        maiorpeso = maisleves = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < maisleves:
            maisleves = dados[1]
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print(f'O total de pessoas cadastradas foi de {len(pessoas)}')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {maisleves}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maisleves:
        print(f'[{p[0]}] ', end='')
