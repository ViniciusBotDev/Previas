print(f'{' LOJA ':=^40}')
Preço_compras = float(input('Preço das compras: R$'))
Forma = int(input('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/pix
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção?  '''))
if Forma == 1:
    total = Preço_compras - (Preço_compras*10/100)
    print(f'Sua compra de R${Preço_compras:.2f} ficará no valor final de R${total:.2f}')
elif Forma == 2:
    total = Preço_compras - (Preço_compras*5/100)
    print(f'Sua compra de R${Preço_compras:.2f} ficará no valor final de R${total:.2f}')
elif Forma == 3:
    total = Preço_compras / 2
    print(f'Sua comrpra de R${Preço_compras:.2f} ficará no valor final de 2x de R${total:.2f}')
elif Forma == 4:
    parcelas = int(input('Quantas parcelas?  '))
    total = Preço_compras + (Preço_compras*20/100)
    totparcelas = total / parcelas
    print(f'Sua compra parcelada em {parcelas}x de R${totparcelas} COM JUROS')
    print(f'Sua compra de R${Preço_compras:.2f} vai custar {total:.2f}')
else:
    print('Opção inválida...')