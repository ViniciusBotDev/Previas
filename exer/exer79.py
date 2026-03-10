listagem = []
listapar= []
listaimpar = []
while True:
    n = int(input('Digite algum numero: '))
    listagem.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    r = str(input('Deseja continuar? [S/N] ')).upper()
    if r == 'N':
        break
print(f'Valores pares digitados: {listapar}')
print(f'Valores impares digitados: {listaimpar}')
print(f'Valores totais digitados: {listagem}')