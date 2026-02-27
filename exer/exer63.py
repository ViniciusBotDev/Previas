while True:
    print('-'*30)
    num = int(input('Quer ver a tabuada de qual número (digite um numero negivo para parar):  '))
    print('-'*30)
    if num < 0:
        break
    for c in range(1,11):
        soma = num*c
        print(f'{num} * {c} = {soma}')
