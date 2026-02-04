preço_produto = float(input('Digite o preço do produto: '))

produto_descontado = preço_produto - (preço_produto * 5 / 100)

print(f'Seu produto custa {preço_produto:.2f} mas com 5% de desconto ele irá ficar {produto_descontado:.2f}')