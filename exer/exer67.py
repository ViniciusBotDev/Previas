print('-'*16, 'BANCO', '-'*16)
valor = int(input("Quanto deseja sacar? R$ "))
print('='*16)
nota50 = valor // 50
valor = valor % 50
nota20 = valor // 20
valor = valor % 20
nota10 = valor // 10
valor = valor % 10
nota1 = valor // 1
print(f"Total de {nota50} cédulas de R$50")
print(f"Total de {nota20} cédulas de R$20")
print(f"Total de {nota10} cédulas de R$10")
print(f"Total de {nota1} cédulas de R$1")
print('='*16)
print('Volte sempre ao banco!')