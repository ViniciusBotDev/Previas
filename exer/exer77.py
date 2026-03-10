numeros = []
for n in range(0,5):
    num = int(input('Digite um numero: '))
    if n == 0 or num > numeros[-1]:
        numeros.append(num)
        print('adicionado no final da lista')
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(numeros)