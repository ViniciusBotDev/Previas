alguel_dia = 60
valor_km = 0.15

print('Alguel de carros')
print('Cada alguel diário custa R$60 \n E a cada km percorrido será cobrado R$0.15 ')
dias_comprados = int(input('Quantos dias deseja alugar?   '))
km_percorrido = float(input('Quantos km voçe percorreu com o carro alugado?  '))

total_dias = alguel_dia * dias_comprados
total_km = valor_km * km_percorrido
valor_total = total_km + total_dias

print(f'Valor dos dias alugados R${total_dias} e valor dos km rodados R${total_km:.2f}')
print(f'E o valor total de km e dias percorridos é de R${valor_total}')