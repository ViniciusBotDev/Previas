galera = []
dicionario = {}
soma = media = 0
while True:
    dicionario['nome'] = str(input('Digite seu nome:'))
    dicionario['sexo'] = str(input('Digite seu sexo: [M/F]')).upper()
    while dicionario['sexo'] not in 'MF':
        dicionario['sexo'] = str(input('Dados inválidos. Por favor, digite seu sexo: [M/F]')).upper()
    dicionario['idade'] = int(input('Digite sua idade: '))
    soma += dicionario['idade']
    galera.append(dicionario.copy())
    resposta = str(input('Quer continuar? [S/N]')).upper()
    while resposta not in 'SN':
        resposta = str(input('Dados inválidos. Por favor, quer continuar? [S/N]')).upper()
    if resposta == 'N':
        break
print('-='*30)
print(f'Ao todo, temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:.2f} anos.')
print(f'As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print(f'As pessoas com idade acima da média são: ', end='')
for p in galera:
    if p['idade'] > media:
        print(f'{p["nome"]} ', end='')
