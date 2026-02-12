from time import sleep

numero1 = int(input('Digite o primeiro numero:  '))
numero2 = int(input('Digite o segundo numero:  '))
numero3 = int(input('Digite o terceiro numero:  '))

menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3

maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero2 and numero3 > numero1:
    maior = numero3
print('Pensando..')
sleep(1)
print(f'O menor valor digitado foi: {menor}')
print(f'O maior valor digitado foi: {maior}')