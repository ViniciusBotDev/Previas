salário = float(input("Digite o salário do funcionário: "))

novo_salário = salário + (salário * 15 / 100)

print(f'O salário do funcionário de R${salário:.2f}, com 15% de aumento ficará R${novo_salário:.2f}')