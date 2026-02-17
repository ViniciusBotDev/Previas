numero1 = int(input('Digite o primeiro valor:  '))
numero2 = int(input('Digite o segundo valor:  '))
if numero1 > numero2:
    print(f'O Primeiro numero {numero1} é maior que o segundo numero {numero2}')
elif numero2 > numero1:
    print(f'O segundo numero {numero2} é maior que o primeiro numero {numero1}')
else:
    print('Não existe valor maior, eles são iguais')