numero_escolhido = int(input('Digite um numero:  '))
resultado = numero_escolhido % 2
if resultado == 0:
    print(f'O numero {numero_escolhido} é PAR')
else:
    print(f'O numero {numero_escolhido} é IMPAR')