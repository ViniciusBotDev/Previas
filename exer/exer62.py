soma = cont = 0
while True:
    num = int(input('Digite um numero e (999 para parar):  '))
    if num == 999:
        break
    valores += 1
    soma += num
print(f'A soma foi {soma} e foi utilizado {valores} valores')
