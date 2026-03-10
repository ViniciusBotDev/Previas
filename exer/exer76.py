listagem = []
while True:
    n = int(input('Digite um valor:  '))
    if n not in listagem:
        listagem.append(n)
        print('Valor adicionado..')
    else:
        print('Valor duplicado! Não adicionado...')
    r = str(input('Quer continuar?[S/N]:  ')).upper()
    if r == 'N':
        break
listagem.sort()
print(f'Voçe digitou os valores: {listagem}')
