listagem = []
while True:
    n = int(input('Digite algum numero: '))
    listagem.append(n)
    r = str(input('Deseja continuar? [S/N] ')).upper()
    if r == 'N':
        break
print(f'A quantidade de numeros digitados foi {len(listagem)}')
listagem.sort()
print(f'Listagem na ordem crescente: {listagem}')
listagem.reverse()
print(f'Listagem em decrescente: {listagem}')
if 5 in listagem:
    print('O numero 5 está na lista!')
else:
    print('O valor 5 não está na lista')