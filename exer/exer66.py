total_gasto = produtos1000 = preço = 0
menor_preço = None
produtomaisbarato = ''
while True:
    produtos = str(input('Nome do produto: '))
    preço = float(input('Preço: '))
    total_gasto += preço
    if preço >= 1000:
        produtos1000 += 1
    if menor_preço == None or preço < menor_preço:
        menor_preço = preço
        produtomaisbarato = produtos
    escolha = input('Deseja continuar [S/N]: ').strip().upper()[0]
    while escolha not in "SN":
        print('Digite algo válido..')
        escolha = input('Deseja continuar [S/N]: ').strip().upper()[0]
    if escolha == 'N':
        break
print('-'*15, 'FIM DO PROGRAMA', '-'*15)
print(f'''O total gasto da compra foi R${total_gasto:.2f}
Temos {produtos1000} produtos custando mais de R$1000.00
O produto mais barato foi {produtomaisbarato} que custou R${menor_preço}''')
