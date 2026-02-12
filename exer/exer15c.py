salario_atual = float(input('Digite o valor do salario: R$'))
if salario_atual <= 1250:
    novo_salario = salario_atual + (salario_atual * 15 / 100)
else:
    novo_salario = salario_atual + (salario_atual * 10 / 100)
print(f'O novo salario será de R${novo_salario:.2f}')
