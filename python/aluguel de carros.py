print('Alguel de carros')
print('Cada alguel diário custa R$60   ')
dias_comprados = int(input('Quantos dias deseja alugar?   '))
km_percorrido = float(input('Quantos km voçe percorreu com o carro alugado?  '))

total_dias = 60 * dias_comprados
total_km = 0.15 * km_percorrido
valor_total = total_km + total_dias

print(f'Valor dos dias alugados R${total_dias} e valor dos km rodados R${total_km:.2f}')
print(f'E o valor total a ser pagado é de R${valor_total:.2f}')